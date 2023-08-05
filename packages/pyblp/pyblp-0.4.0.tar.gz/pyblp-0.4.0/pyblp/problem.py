"""Configuration of the BLP problem and routines used to solve it."""

import time
import functools

import numpy as np
import scipy.linalg

from . import options, exceptions
from .configurations import Iteration, Optimization, Formulation
from .utilities import output, compute_2sls_weights, ParallelItems, IV
from .primitives import Products, Agents, Economy, Market, NonlinearParameters


class Problem(Economy):
    r"""A BLP problem.

    This class is initialized with relevant data and solved with :meth:`Problem.solve`.

    In both `product_data` and `agent_data`, fields with multiple columns can be either matrices or can be broken up
    into multiple one-dimensional fields with column index suffixes that start at zero. For example, if there are three
    columns of demand-side instruments, the `demand_instruments` field in `product_data`, which in this case should be a
    matrix with three columns, can be replaced by three one-dimensional fields: `demand_instruments0`,
    `demand_instruments1`, and `demand_instruments2`.

    Parameters
    ----------
    product_formulations : `Formulation or tuple of Formulation`
        :class:`Formulation` configuration or tuple of up to three :class:`Formulation` configurations for the matrix
        of linear product characteristics, :math:`X_1`, for the matrix of nonlinear product characteristics,
        :math:`X_2`, and for the matrix of cost characteristics, :math:`X_3`, respectively. If the formulation for
        :math:`X_3` is not specified or is ``None``, a supply side will not be estimated. Similarly, if the formulation
        for :math:`X_2` is not specified or is ``None``, the Logit model will be estimated.

        Variable names should correspond to fields in `product_data`. The ``shares`` variable should not be included in
        any of the formulations and ``prices`` should be included in the formulation for :math:`X_1` or :math:`X_2` (or
        both). The `absorb` argument of :class:`Formulation` can be used to absorb fixed effects into :math:`X_1` and
        :math:`X_3`, but not :math:`X_2`.

    product_data : `structured array-like`
        Each row corresponds to a product. Markets can have differing numbers of products. The following fields are
        required:

            - **market_ids** : (`object`) - IDs that associate products with markets.

            - **shares** : (`numeric`) - Market shares, :math:`s`.

            - **prices** : (`numeric`) - Product prices, :math:`p`.

            - **demand_instruments** : (`numeric`) - Demand-side instruments, :math:`Z_D`.

        If a formulation for :math:`X_3` is specified in `product_formulations`, the following fields are also required,
        since they will be used to estimate the supply side of the problem:

            - **firm_ids** : (`object, optional`) - IDs that associate products with firms. Any columns after the first
              can be used to compute post-estimation outputs for firm changes, such as mergers.

            - **supply_instruments** : (`numeric, optional`) - Supply-side instruments, :math:`Z_S`.

        In addition to supply-side estimation, the `firm_ids` field is also needed to compute some post-estimation
        outputs. If `firm_ids` are specified, custom ownership matrices can be specified as well:

            - **ownership** : (`numeric, optional`) - Custom stacked :math:`J_t \times J_t` ownership matrices,
              :math:`O`, for each market :math:`t`, which can be built with :func:`build_ownership`. By default,
              standard ownership matrices are built only when they are needed. If specified, each stack is associated
              with a `firm_ids` column and must have as many columns as there are products in the market with the most
              products.

        Finally, clustering groups can be specified to account for arbitrary within-group correlation while computing
        standard errors and weighting matrices:

            - **clustering_ids** (`object, optional`) - Cluster group IDs, which will be used when estimating standard
              errors and updating weighting matrices if `se_type` in :meth:`Problem.solve` is ``'clustered'``.

        Along with `market_ids`, `firm_ids`, and `prices`, the names of any additional fields can be used as variables
        in `product_formulations`.

    agent_formulation : `Formulation, optional`
        :class:`Formulation` configuration for the matrix of observed agent characteristics called demographics,
        :math:`d`, which will only be included in the model if this formulation is specified. Since demographics are
        only used if there are nonlinear product characteristics, this formulation should only be specified if
        :math:`X_2` is formulated in `product_formulations`. Variable names should correspond to fields in `agent_data`.
    agent_data : `structured array-like, optional`
        Each row corresponds to an agent. Markets can have differing numbers of agents. Since simulated agents are only
        used if there are nonlinear product characteristics, agent data should only be specified if :math:`X_2` is
        formulated in `product_formulations`. If agent data are specified, market IDs are required:

            - **market_ids** : (`object`) - IDs that associate agents with markets. The set of distinct IDs should be
              the same as the set of IDs in `product_data`. If `integration` is specified, there must be at least as
              many rows in each market as the number of nodes and weights that are built for each market.

        If `integration` is not specified, the following fields are required:

            - **weights** : (`numeric, optional`) - Integration weights, :math:`w`.

            - **nodes** : (`numeric, optional`) - Unobserved agent characteristics called integration nodes,
              :math:`\nu`. If there are more than :math:`K_2` columns, only the first :math:`K_2` will be used.

        Along with `market_ids`, the names of any additional fields can be used as variables in `agent_formulation`.

    integration : `Integration, optional`
        :class:`Integration` configuration for how to build nodes and weights for integration over agent utilities,
        which will replace any `nodes` and `weights` fields in `agent_data`. This configuration is required if `nodes`
        and `weights` in `agent_data` are not specified. It should not be specified if :math:`X_2` is not formulated
        in `product_formulations`.

    Attributes
    ----------
    product_formulations : `Formulation or tuple of Formulation`
        :class:`Formulation` configurations for :math:`X_1`, :math:`X_2`, and :math:`X_3`, respectively.
    agent_formulation : `Formulation`
        :class:`Formulation` configuration for :math:`d`.
    products : `Products`
        Product data structured as :class:`Products`, which consists of data taken from `product_data` along with
        matrices build according to :attr:`Problem.product_formulations`.
    agents : `Agents`
        Agent data structured as :class:`Agents`, which consists of data taken from `agent_data` or built by
        `integration` along with any demographics formulated by `agent_formulation`.
    unique_market_ids : `ndarray`
        Unique market IDs in product and agent data.
    N : `int`
        Number of products across all markets, :math:`N`.
    T : `int`
        Number of markets, :math:`T`.
    K1 : `int`
        Number of linear product characteristics, :math:`K_1`.
    K2 : `int`
        Number of nonlinear product characteristics, :math:`K_2`.
    K3 : `int`
        Number of cost product characteristics, :math:`K_3`.
    D : `int`
        Number of demographic variables, :math:`D`.
    MD : `int`
        Number of demand-side instruments, :math:`M_D`.
    MS : `int`
        Number of supply-side instruments, :math:`M_S`.
    ED : `int`
        Number of absorbed demand-side fixed effects, :math:`E_D`.
    ES : `int`
        Number of absorbed supply-side fixed effects, :math:`E_S`.

    Example
    -------
    The following code initializes a very simple problem with some of the automobile product data from
    :ref:`Berry, Levinsohn, and Pakes (1995) <blp95>`:

    .. ipython:: python

       products = np.recfromcsv(pyblp.data.BLP_PRODUCTS_LOCATION)
       products = {n: products[n] for n in products.dtype.names}
       products['demand_instruments'] = pyblp.build_blp_instruments(
           pyblp.Formulation('hpwt + air + mpg + space'),
            products
       )
       problem = pyblp.Problem(
           product_formulations=(
               pyblp.Formulation('prices + hpwt + air + mpg + space'),
               pyblp.Formulation('hpwt + air')
           ),
           product_data=products,
           integration=pyblp.Integration('monte_carlo', 50, seed=0)
       )
       problem

    After choosing to optimize over the diagonal variance elements in :math:`\Sigma` and choosing starting values, the
    initialized problem can be solved. For simplicity, the following code halts estimation after one GMM step:

    .. ipython:: python

       initial_sigma = np.eye(3)
       results = problem.solve(initial_sigma, steps=1)
       results

    """

    def __init__(self, product_formulations, product_data, agent_formulation=None, agent_data=None, integration=None):
        """Initialize the underlying economy with structured product and agent data."""
        if isinstance(product_formulations, Formulation):
            product_formulations = [product_formulations]
        elif not isinstance(product_formulations, (list, tuple)) or len(product_formulations) > 3:
            raise TypeError("product_formulations must be a Formulation instance or a tuple of up to three instances.")
        product_formulations = list(product_formulations) + [None] * (3 - len(product_formulations))
        products = Products(product_formulations, product_data)
        agents = Agents(products, agent_formulation, agent_data, integration)
        super().__init__(product_formulations, agent_formulation, products, agents)

    def solve(self, sigma=None, pi=None, sigma_bounds=None, pi_bounds=None, delta=None, WD=None, WS=None, steps=2,
              optimization=None, error_behavior='revert', error_punishment=1, delta_behavior='last', iteration=None,
              fp_type='linear', costs_type='linear', costs_bounds=None, se_type='robust', center_moments=True,
              processes=1):
        r"""Solve the problem.

        The problem is solved in one or more GMM steps. During each step, any unfixed nonlinear parameters in
        :math:`\hat{theta}` are optimized to minimize the GMM objective value. If all nonlinear parameters are fixed or
        if there are no nonlinear parameters (as in the Logit model), the objective is evaluated once during the step.

        If there are nonlinear parameters, the mean utility, :math:`\delta(\hat{\theta})` is computed market-by-market
        with fixed point iteration. Otherwise, it is computed analytically according to the solution of the Logit model.
        If a supply side is to be estimated, marginal costs, :math:`c(\hat{\theta})`, are also computed
        market-by-market. Linear parameters are then estimated, which are used to recover structural error terms, which
        in turn are used to form the objective value. By default, the objective gradient is computed as well.

        Parameters
        ----------
        sigma : `array-like, optional`
            Configuration for which elements in the Cholesky decomposition of the covariance matrix that measures
            agents' random taste distribution, :math:`\Sigma`, are fixed at zero and starting values for the other
            elements, which, if not fixed by `sigma_bounds`, are in the vector of unknown elements, :math:`\theta`. Rows
            and columns correspond to columns in :math:`X_2`, which is formulated according `product_formulations` in
            :class:`Problem`. If :math:`X_2` was not formulated, this should not be specified, since the Logit model
            will be estimated.

            Values below the diagonal are ignored. Zeros are assumed to be zero throughout estimation and nonzeros are,
            if not fixed by `sigma_bounds`, starting values for unknown elements in :math:`\theta`.

        pi : `array-like, optional`
            Configuration for which elements in the matrix of parameters that measures how agent tastes vary with
            demographics, :math:`\Pi`, are fixed at zero and starting values for the other elements, which, if not fixed
            by `pi_bounds`, are in the vector of unknown elements, :math:`\theta`. Rows correspond to the same product
            characteristics as in `sigma`. Columns correspond to columns in :math:`d`, which is formulated according to
            `agent_formulation` in :class:`Problem`. If :math:`d` was not formulated, this should not be specified.

            Zeros are assumed to be zero throughout estimation and nonzeros are, if not fixed by `pi_bounds`, starting
            values for unknown elements in :math:`\theta`.

        sigma_bounds : `tuple, optional`
            Configuration for :math:`\Sigma` bounds of the form ``(lb, ub)``, in which both ``lb`` and ``ub`` are of the
            same size as `sigma`. Each element in ``lb`` and ``ub`` determines the lower and upper bound for its
            counterpart in `sigma`. If `optimization` does not support bounds, these will be ignored. By default, if
            bounds are supported, the only unfixed elements that are bounded are those on the diagonal of `sigma`, which
            are bounded below by zero. That is, the diagonal of ``lb`` is all zeros by default.

            Values below the diagonal are ignored. Lower and upper bounds corresponding to zeros in `sigma` are set to
            zero. Setting a lower bound equal to an upper bound fixes the corresponding element. Both ``None`` and
            ``numpy.nan`` are converted to ``-numpy.inf`` in ``lb`` and to ``numpy.inf`` in ``ub``.

        pi_bounds : `tuple, optional`
            Configuration for :math:`\Pi` bounds of the form ``(lb, ub)``, in which both ``lb`` are ``ub`` are of the
            same size as `pi`. Each element in ``lb`` and ``ub`` determines the lower and upper bound for its
            counterpart in `pi`. If `optimization` does not support bounds, these will be ignored. By default, if bounds
            are supported, all unfixed elements are unbounded.

            Lower and upper bounds corresponding to zeros in `pi` are set to zero. Setting a lower bound equal to an
            upper bound fixes the corresponding element. Both ``None`` and ``numpy.nan`` are converted to ``-numpy.inf``
            in ``lb`` and to ``numpy.inf`` in ``ub``.

        delta : `array-like, optional`
            Initial values for the mean utility, :math:`\delta`. If there are any nonlinear parameters, these are the
            values at which the fixed point iteration routine will start during the first objective evaluation. By
            default, :math:`\delta_{jt} = \log s_{jt} - \log s_{0t}` is used, which is the estimated :math:`\delta`
            under the Logit model when there are no nonlinear parameters.
        WD : `array-like, optional`
            Starting values for the demand-side weighting matrix, :math:`W_D`. By default, the 2SLS weighting matrix,
            :math:`W_D = (Z_D'Z_D)^{-1}`, is used.
        WS : `array-like, optional`
            Starting values for the supply-side weighting matrix, :math:`W_S`, which is only used if :math:`X_3` was
            formulated by `product_formulations` in :class:`Problem`. By default, the 2SLS weighting matrix,
            :math:`W_S = (Z_S'Z_S)^{-1}`, is used.
        steps : `int, optional`
            Number of GMM steps. By default, two-step GMM is used.
        optimization : `Optimization, optional`
            :class:`Optimization` configuration for how to solve the optimization problem in each GMM step, which is
            only used if there are unfixed nonlinear parameters over which to optimize. By default,
            ``Optimization('l-bfgs-b')`` is used. Routines that do not support bounds will ignore `sigma_bounds` and
            `pi_bounds`. Choosing a routine that does not use analytic gradients will slow down estimation.
        error_behavior : `str, optional`
            How to handle any errors. For example, it is common to encounter overflow when computing
            :math:`\delta(\hat{\theta})` at a large :math:`\hat{\theta}`. The following behaviors are supported:

                - ``'revert'`` (default) - Revert problematic :math:`\delta(\hat{\theta})` elements to their last
                  computed values and use reverted values to compute :math:`\partial\xi / \partial\theta`, and, if the
                  supply side is considered, to compute both :math:`\tilde{c}(\hat{\theta})` and
                  :math:`\partial\omega / \partial\theta` as well. If there are problematic elements in
                  :math:`\partial\xi / \partial\theta`, :math:`\tilde{c}(\hat{\theta})`, or
                  :math:`\partial\omega / \partial\theta`, revert these to their last computed values as well. If there
                  are problematic elements in the first objective evaluation, revert values in
                  :math:`\delta(\hat{\theta})` to their starting values; in :math:`\tilde{c}(\hat{\theta})`, to prices;
                  and in Jacobians, to zeros.

                - ``'punish'`` - Set the objective to ``1`` and its gradient to all zeros. This option along with a
                  large `error_punishment` can be helpful for routines that do not use analytic gradients.

                - ``'raise'`` - Raise an exception.

        error_punishment : `float, optional`
            How to scale the GMM objective value after an error. By default, the objective value is not scaled.
        delta_behavior : `str, optional`
            Configuration for the values at which the fixed point computation of :math:`\delta(\hat{\theta})` in each
            market will start. This configuration is only relevant if there are unfixed nonlinear parameters over which
            to optimize. The following behaviors are supported:

                - ``'last'`` (default) - Start at the values of :math:`\delta(\hat{\theta})` computed during the last
                  objective evaluation, or, if this is the first evaluation, at the values configured by `delta`. This
                  behavior tends to speed up computation but may introduce noise into gradient computation, especially
                  when the fixed point iteration tolerance is low.

                - ``'first'`` - Start at the values configured by `delta` during the first GMM step, and at the values
                  computed by the last GMM step for each subsequent step. This behavior is more conservative and will
                  often be slower.

        iteration : `Iteration, optional`
            :class:`Iteration` configuration for how to solve the fixed point problem used to compute
            :math:`\delta(\hat{\theta})` in each market. This configuration is only relevant if there are nonlinear
            parameters, since :math:`\delta` can be estimated analytically in the Logit model. By default,
            ``Iteration('squarem', {'tol': 1e-14})`` is used.
        fp_type : `str, optional`
            Configuration for the type of contraction mapping used to compute :math:`\delta(\hat{\theta})`. The
            following types of contraction mappings are supported:

                - ``'linear'`` (default) - Standard linear contraction mapping,

                  .. math:: \delta \leftarrow \delta + \log s - \log s(\delta, \hat{\theta}),

                  which is the most popular type.

                - ``'nonlinear'`` - Exponentiated version,

                  .. math:: \exp(\delta) \leftarrow \exp(\delta)s / s(\delta, \hat{\theta}),

                  which can be faster because fewer logarithms need to be calculated. It can also help mitigate problems
                  stemming from any negative integration weights.

            This option is only relevant if there are nonlinear parameters, since :math:`\delta` can be estimated
            analytically in the Logit model.

        costs_type : `str, optional`
            Marginal cost specification. The following specifications are supported:

                - ``'linear'`` (default) - Linear specification: :math:`\tilde{c} = c`.

                - ``'log'`` - Log-linear specification: :math:`\tilde{c} = \log c`.

            This specification is only relevant if :math:`X_3` was formulated by `product_formulations` in
            :class:`Problem`.

        costs_bounds : `tuple, optional`
            Configuration for :math:`c` bounds of the form ``(lb, ub)``, in which both ``lb`` and ``ub`` are floats.
            This is only relevant if :math:`X_3` was formulated by `product_formulations` in :class:`Problem`. By
            default, marginal costs are unbounded. When `costs_type` is ``'log'``, nonpositive :math:`c(\hat{\theta})`
            values can create problems when computing :math:`\tilde{c}(\hat{\theta}) = \log c(\hat{\theta})`. One
            solution is to let ``lb`` equal some small number; however, doing so introduces error into gradient
            computation. Both ``None`` and ``numpy.nan`` are converted to ``-numpy.inf`` in ``lb`` and to ``numpy.inf``
            in ``ub``.
        se_type : `str, optional`
            How to compute standard errors. The following types of standard errors are supported:

                - ``'robust'`` (default) - Robust standard errors.

                - ``'unadjusted'`` - Unadjusted standard errors computed under the assumption that weighting matrices
                  are optimal.

                - ``'clustered'`` - Clustered standard errors, which account for arbitrary within-group correlation.
                  Clusters must be defined by the `clustering_ids` field of `product_data` in :class:`Problem`.
                  If there is more than one GMM `step`, weighting matrices will be updated to account for clustering
                  as well.

        center_moments : `bool, optional`
            Whether to center the sample moments before using them to update weighting matrices. By default, sample
            moments are centered.
        processes : `int, optional`
            Number of Python processes that will be used during estimation. By default, multiprocessing will not be
            used. For values greater than one, a pool of that many Python processes will be created during each
            GMM objective evaluation. Market-by-market computation of :math:`\delta(\hat{\theta})` and, if :math:`X_3`
            was formulated by `product_formulations` in :class:`Problem`, of :math:`\tilde{c}(\hat{\theta})`, along with
            associated Jacobians, will be distributed among these processes. Using multiprocessing will only improve
            estimation speed if gains from parallelization outweigh overhead from creating process pools.

        Returns
        -------
        `Results`
            :class:`Results` of the solved problem.

        """

        # record the amount of time it takes to solve the problem
        step_start_time = time.time()

        # configure or validate configurations
        if optimization is None:
            optimization = Optimization('l-bfgs-b')
        if iteration is None:
            iteration = Iteration('squarem', {'tol': 1e-14})
        if not isinstance(optimization, Optimization):
            raise TypeError("optimization must be None or an Optimization instance.")
        if not isinstance(iteration, Iteration):
            raise TypeError("iteration must be None or an Iteration instance.")

        # validate behaviors and types
        if error_behavior not in {'revert', 'punish', 'raise'}:
            raise ValueError("error_behavior must be 'revert', 'punish', or 'raise'.")
        if delta_behavior not in {'last', 'first'}:
            raise ValueError("delta_behavior must be 'last' or 'first'.")
        if fp_type not in {'linear', 'nonlinear'}:
            raise ValueError("fp_type must be 'linear' or 'nonlinear'.")
        if costs_type not in {'linear', 'log'}:
            raise ValueError("costs_type must be 'linear' or 'log'.")
        if se_type not in {'robust', 'unadjusted', 'clustered'}:
            raise ValueError("se_type must be 'robust', 'unadjusted', or 'clustered'.")
        if se_type == 'clustered' and 'clustering_ids' not in self.products.dtype.names:
            raise ValueError("se_type can only be 'clustered' if clustering_ids were specified in product_data.")

        # configure or validate costs bounds
        if costs_bounds is None:
            costs_bounds = (-np.inf, +np.inf)
        else:
            costs_bounds = list(np.asarray(costs_bounds, options.dtype).flatten())
            if len(costs_bounds) != 2 or costs_bounds[0] > costs_bounds[1]:
                raise ValueError("costs_bounds must be a tuple of the form (lb, ub).")
            if not np.isfinite(costs_bounds[0]):
                costs_bounds[0] = -np.inf
            if not np.isfinite(costs_bounds[1]):
                costs_bounds[1] = +np.inf

        # compress sigma and pi into theta but retain information about the original matrices
        nonlinear_parameters = NonlinearParameters(
            self, sigma, pi, sigma_bounds, pi_bounds, optimization._supports_bounds
        )
        theta = nonlinear_parameters.compress()
        if self.K2 > 0:
            output("")
            output("Initial Nonlinear Parameters:")
            output(nonlinear_parameters.format())
            output("")
            output("Lower Bounds on Nonlinear Parameters:")
            output(nonlinear_parameters.format_lower_bounds())
            output("")
            output("Upper Bounds on Nonlinear Parameters:")
            output(nonlinear_parameters.format_upper_bounds())

        # compute or load the demand-side weighting matrix
        if WD is None:
            WD, WD_errors = compute_2sls_weights(self.products.ZD)
            self._handle_errors(error_behavior, WD_errors)
        else:
            WD = np.asarray(WD, options.dtype)
            if WD.shape != (self.MD, self.MD):
                raise ValueError(f"WD must have {self.MD} rows and columns.")

        # compute or load the supply-side weighting matrix
        if self.MS == 0:
            WS = np.full((0, 0), np.nan, options.dtype)
        elif WS is None:
            WS, WS_errors = compute_2sls_weights(self.products.ZS)
            self._handle_errors(error_behavior, WS_errors)
        else:
            WS = np.asarray(WS, options.dtype)
            if WS.shape != (self.MS, self.MS):
                raise ValueError(f"WS must have {self.MS} rows and columns.")

        # compute or load initial delta values
        if delta is None:
            true_delta = np.log(self.products.shares)
            for t in self.unique_market_ids:
                shares_t = self.products.shares[self.products.market_ids.flat == t]
                true_delta[self.products.market_ids.flat == t] -= np.log(1 - shares_t.sum())
        else:
            true_delta = np.c_[np.asarray(delta, options.dtype)]
            if true_delta.shape != (self.N, 1):
                raise ValueError(f"delta must be a vector with {self.N} elements.")

        # initialize marginal costs as prices
        true_tilde_costs = np.full((self.N, 0), np.nan, options.dtype)
        if self.K3 > 0:
            if costs_type == 'linear':
                true_tilde_costs = self.products.prices
            else:
                assert costs_type == 'log'
                true_tilde_costs = np.log(self.products.prices)

        # initialize Jacobians of xi and omega with respect to theta as all zeros
        true_xi_jacobian = np.zeros((self.N, nonlinear_parameters.P), options.dtype)
        true_omega_jacobian = np.full_like(true_xi_jacobian, 0 if self.K3 > 0 else np.nan, options.dtype)

        # iterate over each GMM step
        last_results = None
        for step in range(1, steps + 1):
            # initialize IV models for demand- and supply-side linear parameter estimation
            demand_iv = IV(self.products.X1, self.products.ZD, WD)
            supply_iv = IV(self.products.X3, self.products.ZS, WS)
            self._handle_errors(error_behavior, demand_iv.errors | supply_iv.errors)

            # wrap computation of objective information with step-specific information
            compute_step_info = functools.partial(
                self._compute_objective_info, nonlinear_parameters, demand_iv, supply_iv, WD, WS, error_behavior,
                error_punishment, delta_behavior, iteration, fp_type, costs_type, costs_bounds, processes
            )

            # define the objective function for the optimization routine, which also outputs progress updates
            def wrapper(new_theta, current_iterations, current_evaluations):
                info = wrapper.cache = compute_step_info(new_theta, wrapper.cache, optimization._compute_gradient)
                wrapper.iteration_mappings.append(info.iteration_mapping)
                wrapper.evaluation_mappings.append(info.evaluation_mapping)
                if optimization._universal_display:
                    output(info.format_progress(
                        step, current_iterations, current_evaluations, wrapper.smallest_objective,
                        wrapper.smallest_gradient_norm
                    ))
                wrapper.smallest_objective = min(wrapper.smallest_objective, info.objective)
                wrapper.smallest_gradient_norm = min(wrapper.smallest_gradient_norm, info.gradient_norm)
                return (info.objective, info.gradient) if optimization._compute_gradient else info.objective

            # initialize optimization progress
            wrapper.iteration_mappings = []
            wrapper.evaluation_mappings = []
            wrapper.smallest_objective = wrapper.smallest_gradient_norm = np.inf
            wrapper.cache = ObjectiveInfo(
                self, nonlinear_parameters, WD, WS, theta, true_delta, true_delta, true_tilde_costs, true_xi_jacobian,
                true_omega_jacobian
            )

            # optimize theta
            iterations = evaluations = 0
            optimization_start_time = optimization_end_time = time.time()
            if nonlinear_parameters.P > 0:
                output("")
                output(f"Starting optimization for step {step} out of {steps} ...")
                output("")
                bounds = [(p.lb, p.ub) for p in nonlinear_parameters.unfixed]
                theta, converged, iterations, evaluations = optimization._optimize(theta, bounds, wrapper)
                status = "completed" if converged else "failed"
                optimization_end_time = time.time()
                optimization_time = optimization_end_time - optimization_start_time
                if not converged:
                    self._handle_errors(error_behavior, {exceptions.ThetaConvergenceError})
                output("")
                output(f"Optimization {status} after {output.format_seconds(optimization_time)}.")

            # use objective information computed at the optimal theta to compute results for the step
            output("")
            output(f"Computing results for step {step} ...")
            step_info = compute_step_info(theta, wrapper.cache, compute_gradient=nonlinear_parameters.P > 0)
            results = step_info.to_results(
                last_results, step_start_time, optimization_start_time, optimization_end_time, iterations,
                evaluations + 1, wrapper.iteration_mappings, wrapper.evaluation_mappings, center_moments, se_type
            )
            self._handle_errors(error_behavior, results._errors)
            output(f"Computed results after {output.format_seconds(results.total_time - results.optimization_time)}.")
            output("")
            output(results)

            # store the last results and return results from the final step
            last_results = results
            if step == steps:
                return results

            # update vectors and matrices
            true_delta = step_info.true_delta
            true_tilde_costs = step_info.true_tilde_costs
            true_xi_jacobian = step_info.true_xi_jacobian
            true_omega_jacobian = step_info.true_omega_jacobian
            WD = results.updated_WD
            WS = results.updated_WS
            step_start_time = time.time()

    def _compute_objective_info(self, nonlinear_parameters, demand_iv, supply_iv, WD, WS, error_behavior,
                                error_punishment, delta_behavior, iteration, fp_type, costs_type, costs_bounds,
                                processes, theta, last_objective_info, compute_gradient):
        """Compute demand- and supply-side contributions. Then, form the GMM objective value and its gradient. Finally,
        handle any errors that were encountered before structuring relevant objective information.
        """
        sigma, pi = nonlinear_parameters.expand(theta)

        # compute demand-side contributions
        true_delta, true_xi_jacobian, delta, xi_jacobian, beta, true_xi, iterations, evaluations, demand_errors = (
            self._compute_demand_contributions(
                nonlinear_parameters, demand_iv, iteration, fp_type, processes, sigma, pi, last_objective_info,
                compute_gradient
            )
        )

        # compute supply-side contributions
        supply_errors = set()
        gamma = np.full((self.K3, 1), np.nan, options.dtype)
        true_tilde_costs = tilde_costs = true_omega = np.full((self.N, 0), np.nan, options.dtype)
        true_omega_jacobian = omega_jacobian = np.full((self.N, nonlinear_parameters.P), np.nan, options.dtype)
        if self.K3 > 0:
            true_tilde_costs, true_omega_jacobian, tilde_costs, omega_jacobian, gamma, true_omega, supply_errors = (
                self._compute_supply_contributions(
                    nonlinear_parameters, demand_iv, supply_iv, costs_type, costs_bounds, processes, beta, sigma, pi,
                    true_delta, true_xi_jacobian, xi_jacobian, last_objective_info, compute_gradient
                )
            )

        # compute the objective value
        objective = (true_xi.T @ self.products.ZD) @ WD @ (self.products.ZD.T @ true_xi)
        if self.K3 > 0:
            objective += (true_omega.T @ self.products.ZS) @ WS @ (self.products.ZS.T @ true_omega)

        # compute its gradient
        gradient = np.full_like(theta, np.nan, options.dtype)
        if compute_gradient:
            gradient = 2 * ((xi_jacobian.T @ self.products.ZD) @ WD @ (self.products.ZD.T @ true_xi))
            if self.K3 > 0:
                gradient += 2 * ((omega_jacobian.T @ self.products.ZS) @ WS @ (self.products.ZS.T @ true_omega))

        # handle any errors
        errors = demand_errors | supply_errors
        if errors:
            if error_behavior == 'raise':
                raise exceptions.MultipleErrors(errors)
            if error_behavior == 'revert':
                if error_punishment != 1:
                    objective *= error_punishment
            else:
                assert error_behavior == 'punish'
                objective = np.array(error_punishment)
                if compute_gradient:
                    gradient = np.zeros_like(theta)

        # select the delta that will be used in the next objective evaluation
        if delta_behavior == 'last':
            next_delta = true_delta
        else:
            assert delta_behavior == 'first'
            next_delta = last_objective_info.next_delta

        # structure objective information
        return ObjectiveInfo(
            self, nonlinear_parameters, WD, WS, theta, next_delta, true_delta, true_tilde_costs, true_xi_jacobian,
            true_omega_jacobian, delta, tilde_costs, xi_jacobian, omega_jacobian, true_xi, true_omega, beta, gamma,
            objective, gradient, iterations, evaluations, errors
        )

    def _compute_demand_contributions(self, nonlinear_parameters, demand_iv, iteration, fp_type, processes, sigma, pi,
                                      last_objective_info, compute_gradient):
        """Compute delta and the Jacobian of xi (equivalently, of delta) with respect to theta market-by-market. If
        necessary, revert problematic elements to their last values. Lastly, recover beta and compute xi.
        """
        errors = set()

        # initialize delta and its Jacobian along with fixed point information so that they can be filled
        iterations = {}
        evaluations = {}
        true_delta = np.zeros((self.N, 1), options.dtype)
        true_xi_jacobian = np.full((self.N, nonlinear_parameters.P), np.nan, options.dtype)

        # if there are only linear parameters, use the initial delta
        if self.K2 == 0:
            true_delta = last_objective_info.next_delta
        else:
            # define a function that builds a market along with arguments used to compute delta and its Jacobian
            def market_factory(s):
                market_s = DemandProblemMarket(self, s, sigma, pi)
                initial_delta_s = last_objective_info.next_delta[self.products.market_ids.flat == s]
                return market_s, initial_delta_s, nonlinear_parameters, iteration, fp_type, compute_gradient

            # compute delta and its Jacobian market-by-market
            with ParallelItems(self.unique_market_ids, market_factory, DemandProblemMarket.solve, processes) as items:
                for t, (true_delta_t, true_xi_jacobian_t, errors_t, iterations[t], evaluations[t]) in items:
                    true_delta[self.products.market_ids.flat == t] = true_delta_t
                    true_xi_jacobian[self.products.market_ids.flat == t] = true_xi_jacobian_t
                    errors |= errors_t

        # replace invalid elements in delta with their last values
        bad_indices = ~np.isfinite(true_delta)
        if np.any(bad_indices):
            true_delta[bad_indices] = last_objective_info.true_delta[bad_indices]
            errors.add(lambda: exceptions.DeltaReversionError(bad_indices.sum()))

        # replace invalid elements in its Jacobian with their last values
        if compute_gradient:
            bad_indices = ~np.isfinite(true_xi_jacobian)
            if np.any(bad_indices):
                true_xi_jacobian[bad_indices] = last_objective_info.true_xi_jacobian[bad_indices]
                errors.add(lambda: exceptions.XiJacobianReversionError(bad_indices.sum()))

        # absorb any demand-side fixed effects
        delta = true_delta
        xi_jacobian = true_xi_jacobian
        if self.ED > 0:
            delta, delta_errors = self._absorb_demand_ids(delta)
            errors |= delta_errors
            if compute_gradient:
                xi_jacobian, jacobian_errors = self._absorb_demand_ids(xi_jacobian)
                errors |= jacobian_errors

        # recover beta and compute xi
        beta, true_xi = demand_iv.estimate(delta)
        return true_delta, true_xi_jacobian, delta, xi_jacobian, beta, true_xi, iterations, evaluations, errors

    def _compute_supply_contributions(self, nonlinear_parameters, demand_iv, supply_iv, costs_type, costs_bounds,
                                      processes, beta, sigma, pi, true_delta, true_xi_jacobian, xi_jacobian,
                                      last_objective_info, compute_gradient):
        """Compute transformed marginal costs and the Jacobian of omega (equivalently, of transformed marginal costs)
        with respect to theta market-by-market. If necessary, revert problematic elements to their last values. Lastly,
        recover gamma and compute omega.
        """
        errors = set()

        # compute the Jacobian of beta with respect to theta, which is needed to compute other Jacobians
        beta_jacobian = np.full((self.K1, nonlinear_parameters.P), np.nan, options.dtype)
        if compute_gradient:
            beta_jacobian = demand_iv.estimate(xi_jacobian, compute_residuals=False)

        # initialize transformed marginal costs and their Jacobian so that they can be filled
        true_tilde_costs = np.zeros((self.N, 1), options.dtype)
        true_omega_jacobian = np.full((self.N, nonlinear_parameters.P), np.nan, options.dtype)

        # define a function that builds a market along with arguments used to compute transformed marginal costs and
        #   their Jacobian
        def market_factory(s):
            market_s = SupplyProblemMarket(self, s, sigma, pi, beta, true_delta)
            last_true_tilde_costs_s = last_objective_info.true_tilde_costs[self.products.market_ids.flat == s]
            true_xi_jacobian_s = true_xi_jacobian[self.products.market_ids.flat == s]
            return (
                market_s, last_true_tilde_costs_s, true_xi_jacobian_s, beta_jacobian, nonlinear_parameters,
                costs_type, costs_bounds, compute_gradient
            )

        # compute transformed marginal costs and their Jacobian market-by-market
        with ParallelItems(self.unique_market_ids, market_factory, SupplyProblemMarket.solve, processes) as items:
            for t, (true_tilde_costs_t, true_omega_jacobian_t, errors_t) in items:
                true_tilde_costs[self.products.market_ids.flat == t] = true_tilde_costs_t
                true_omega_jacobian[self.products.market_ids.flat == t] = true_omega_jacobian_t
                errors |= errors_t

        # replace invalid transformed marginal costs with their last values
        bad_indices = ~np.isfinite(true_tilde_costs)
        if np.any(bad_indices):
            true_tilde_costs[bad_indices] = last_objective_info.true_tilde_costs[bad_indices]
            errors.add(lambda: exceptions.CostsReversionError(tilde_costs.sum()))

        # replace invalid elements in their Jacobian with their last values
        if compute_gradient:
            bad_indices = ~np.isfinite(true_omega_jacobian)
            if np.any(bad_indices):
                true_omega_jacobian[bad_indices] = last_objective_info.true_omega_jacobian[bad_indices]
                errors.add(lambda: exceptions.OmegaJacobianReversionError(bad_indices.sum()))

        # absorb any supply-side fixed effects
        tilde_costs = true_tilde_costs
        omega_jacobian = true_omega_jacobian
        if self.ES > 0:
            tilde_costs, tilde_costs_errors = self._absorb_supply_ids(tilde_costs)
            errors |= tilde_costs_errors
            if compute_gradient:
                omega_jacobian, jacobian_errors = self._absorb_supply_ids(omega_jacobian)
                errors |= jacobian_errors

        # recover gamma and compute omega
        gamma, true_omega = supply_iv.estimate(tilde_costs)
        return true_tilde_costs, true_omega_jacobian, tilde_costs, omega_jacobian, gamma, true_omega, errors

    @staticmethod
    def _handle_errors(error_behavior, errors):
        """Either raise or output information about any errors."""
        if errors:
            if error_behavior == 'raise':
                raise exceptions.MultipleErrors(errors)
            output("")
            output(exceptions.MultipleErrors(errors))
            output("")


class ObjectiveInfo(object):
    """Structured information about a completed iteration of the optimization routine."""

    def __init__(self, problem, nonlinear_parameters, WD, WS, theta, next_delta, true_delta, true_tilde_costs,
                 true_xi_jacobian, true_omega_jacobian, delta=None, tilde_costs=None, xi_jacobian=None,
                 omega_jacobian=None, true_xi=None, true_omega=None, beta=None, gamma=None, objective=None,
                 gradient=None, iteration_mapping=None, evaluation_mapping=None, errors=None):
        """Initialize objective information. Optional parameters will not be specified when preparing for the first
        objective evaluation.
        """
        self.problem = problem
        self.nonlinear_parameters = nonlinear_parameters
        self.WD = WD
        self.WS = WS
        self.theta = theta
        self.next_delta = next_delta
        self.true_delta = true_delta
        self.true_tilde_costs = true_tilde_costs
        self.true_xi_jacobian = true_xi_jacobian
        self.true_omega_jacobian = true_omega_jacobian
        self.delta = delta
        self.tilde_costs = tilde_costs
        self.xi_jacobian = xi_jacobian
        self.omega_jacobian = omega_jacobian
        self.true_xi = true_xi
        self.true_omega = true_omega
        self.beta = beta
        self.gamma = gamma
        self.objective = objective
        self.gradient = gradient
        self.iteration_mapping = iteration_mapping
        self.evaluation_mapping = evaluation_mapping
        self.errors = errors
        with np.errstate(invalid='ignore'):
            self.gradient_norm = None if gradient is None or gradient.size == 0 else np.abs(gradient).max()

    def format_progress(self, step, current_iterations, current_evaluations, smallest_objective,
                        smallest_gradient_norm):
        """Format optimization progress as a string. The first iteration will include the progress table header. If
        there are any errors, information about them will be formatted as well. The smallest_objective is the smallest
        objective value encountered so far during optimization.
        """
        lines = []
        header = [
            ("GMM", "Step"), ("Optimization", "Iterations"), ("Objective", "Evaluations"),
            ("Fixed Point", "Iterations"), ("Contraction", "Evaluations"), ("Objective", "Value"),
            ("Objective", "Improvement"), ("Gradient", "Infinity Norm"), ("Gradient", "Improvement")
        ]
        widths = [max(len(k1), len(k2), options.digits + 6 if i > 4 else 0) for i, (k1, k2) in enumerate(header)]
        formatter = output.table_formatter(widths)

        # if this is the first iteration, include the header
        if current_evaluations == 1:
            lines.extend([formatter([k[0] for k in header]), formatter([k[1] for k in header], underline=True)])

        # include information about any errors
        if self.errors:
            lines.extend(["", str(exceptions.MultipleErrors(self.errors)), ""])

        # include the progress update
        objective_improved = np.isfinite(smallest_objective) and self.objective < smallest_objective
        gradient_improved = np.isfinite(smallest_gradient_norm) and self.gradient_norm < smallest_gradient_norm
        lines.append(formatter([
            step,
            current_iterations,
            current_evaluations,
            sum(self.iteration_mapping.values()),
            sum(self.evaluation_mapping.values()),
            output.format_number(self.objective),
            output.format_number(smallest_objective - self.objective) if objective_improved else "",
            output.format_number(self.gradient_norm),
            output.format_number(smallest_gradient_norm - self.gradient_norm) if gradient_improved else "",
        ]))

        # combine the lines into one string
        return "\n".join(lines)

    def to_results(self, *args):
        """Convert this information about an iteration of the optimization routine into full results."""
        from .results import Results
        return Results(self, *args)


class DemandProblemMarket(Market):
    """A single market in a problem, which can be solved to compute delta-related information."""

    def get_unneeded_product_fields(self, fields):
        """Collect fields that will be dropped from product data."""
        return fields - {'shares', 'X2'}

    def solve(self, initial_delta, nonlinear_parameters, iteration, fp_type, compute_gradient):
        """Compute the mean utility for this market that equates market shares to observed values by solving a fixed
        point problem. Then, if compute_gradient is True, compute the Jacobian of xi (equivalently, of delta) with
        respect to theta. If necessary, replace null elements in delta with their last values before computing its
        Jacobian.
        """

        # configure NumPy to identify floating point errors
        errors = set()
        with np.errstate(divide='call', over='call', under='ignore', invalid='call'):
            np.seterrcall(lambda *_: errors.add(exceptions.DeltaFloatingPointError))

            # define a custom log wrapper that identifies issues with taking logs
            def custom_log(x):
                with np.errstate(all='ignore'):
                    if np.any(x <= 0):
                        errors.add(exceptions.NonpositiveSharesError)
                    return np.log(x)

            # solve the fixed point problem
            if fp_type == 'linear':
                log_shares = np.log(self.products.shares)
                contraction = lambda d: d + log_shares - custom_log(self.compute_probabilities(d) @ self.agents.weights)
                delta, converged, iterations, evaluations = iteration._iterate(initial_delta, contraction)
            else:
                assert fp_type == 'nonlinear'
                compute_probabilities = functools.partial(self.compute_probabilities, mu=np.exp(self.mu), linear=False)
                contraction = lambda d: d * self.products.shares / (compute_probabilities(d) @ self.agents.weights)
                exp_delta, converged, iterations, evaluations = iteration._iterate(np.exp(initial_delta), contraction)
                delta = custom_log(exp_delta)

            # if the gradient is to be computed, replace invalid values in delta with the last computed values before
            #   computing its Jacobian
            xi_jacobian = np.full((self.J, nonlinear_parameters.P), np.nan, options.dtype)
            if compute_gradient:
                valid_delta = delta.copy()
                bad_delta_indices = ~np.isfinite(delta)
                valid_delta[bad_delta_indices] = initial_delta[bad_delta_indices]
                xi_jacobian = self.compute_xi_by_theta_jacobian(valid_delta, nonlinear_parameters)

        # determine whether the fixed point converged
        if not converged:
            errors.add(exceptions.DeltaConvergenceError)
        return delta, xi_jacobian, errors, iterations, evaluations

    def compute_xi_by_theta_jacobian(self, delta, nonlinear_parameters):
        """Use the Implicit Function Theorem to compute the Jacobian of xi (equivalently, of delta) with respect to
        theta.
        """
        probabilities = self.compute_probabilities(delta)
        shares_by_xi_jacobian = self.compute_shares_by_xi_jacobian(probabilities)
        shares_by_theta_jacobian = self.compute_shares_by_theta_jacobian(probabilities, nonlinear_parameters)
        try:
            return scipy.linalg.solve(-shares_by_xi_jacobian, shares_by_theta_jacobian)
        except (ValueError, scipy.linalg.LinAlgError):
            return np.full_like(shares_by_theta_jacobian, np.nan)

    def compute_shares_by_xi_jacobian(self, probabilities):
        """Compute the Jacobian of shares with respect to xi (equivalently, to delta)."""
        square_shares = np.diagflat(self.products.shares)
        square_weights = np.diagflat(self.agents.weights)
        return square_shares - probabilities @ square_weights @ probabilities.T

    def compute_shares_by_theta_jacobian(self, probabilities, nonlinear_parameters):
        """Compute the Jacobian of shares with respect to theta."""
        jacobian = np.zeros((self.J, nonlinear_parameters.P), options.dtype)
        for p, parameter in enumerate(nonlinear_parameters.unfixed):
            x, v = parameter.get_characteristics(self.products, self.agents)
            jacobian[:, [p]] = probabilities * v.T * (x - x.T @ probabilities) @ self.agents.weights
        return jacobian


class SupplyProblemMarket(Market):
    """A single market in a problem, which can be solved to compute marginal cost-related information."""

    def solve(self, initial_tilde_costs, xi_jacobian, beta_jacobian, nonlinear_parameters, costs_type, costs_bounds,
              compute_gradient):
        """Compute transformed marginal costs for this market. Then, if compute_gradient is True, compute the Jacobian
        of omega (equivalently, of transformed marginal costs) with respect to theta. If necessary, replace null
        elements in transformed marginal costs with their last values before computing their Jacobian.
        """

        # configure NumPy to identify floating point errors
        errors = set()
        with np.errstate(divide='call', over='call', under='ignore', invalid='call'):
            np.seterrcall(lambda *_: errors.add(exceptions.CostsFloatingPointError))

            # compute marginal costs
            try:
                costs = self.products.prices - self.compute_eta()
            except scipy.linalg.LinAlgError:
                errors.add(exceptions.CostsSingularityError)
                costs = np.full((self.J, 1), np.nan, options.dtype)

            # clip marginal costs that are outside of acceptable bounds
            costs = np.clip(costs, *costs_bounds)

            # take the log of marginal costs under a log-linear specification
            if costs_type == 'linear':
                tilde_costs = costs
            else:
                assert costs_type == 'log'
                with np.errstate(all='ignore'):
                    if np.any(costs <= 0):
                        errors.add(exceptions.NonpositiveCostsError)
                    tilde_costs = np.log(costs)

            # if the gradient is to be computed, replace invalid transformed marginal costs with their last computed
            #   values before computing their Jacobian
            omega_jacobian = np.full((self.J, nonlinear_parameters.P), np.nan, options.dtype)
            if compute_gradient:
                valid_tilde_costs = tilde_costs.copy()
                bad_costs_indices = ~np.isfinite(tilde_costs)
                valid_tilde_costs[bad_costs_indices] = initial_tilde_costs[bad_costs_indices]
                omega_jacobian = self.compute_omega_by_theta_jacobian(
                    valid_tilde_costs, xi_jacobian, beta_jacobian, nonlinear_parameters, costs_type
                )
            return tilde_costs, omega_jacobian, errors

    def compute_omega_by_theta_jacobian(self, tilde_costs, xi_jacobian, beta_jacobian, nonlinear_parameters,
                                        costs_type):
        """Compute the Jacobian of omega (equivalently, of transformed marginal costs) with respect to theta."""
        costs_jacobian = -self.compute_eta_by_theta_jacobian(xi_jacobian, beta_jacobian, nonlinear_parameters)
        if costs_type == 'linear':
            return costs_jacobian
        assert costs_type == 'log'
        return costs_jacobian / np.exp(tilde_costs)

    def compute_eta_by_theta_jacobian(self, xi_jacobian, beta_jacobian, nonlinear_parameters):
        """Compute the Jacobian of the markup term in the BLP-markup equation with respect to theta."""

        # compute the intermediate matrix V that shows up in the decomposition of eta
        probabilities = self.compute_probabilities()
        derivatives = self.compute_utility_by_variable_derivatives('prices')
        V = probabilities * derivatives

        # compute the matrix A, which, when inverted and multiplied by shares, gives eta (negative the intra-firm
        #   Jacobian of shares with respect to prices)
        ownership_matrix = self.get_ownership_matrix()
        square_weights = np.diagflat(self.agents.weights)
        capital_gamma = V @ square_weights @ probabilities.T
        capital_lambda = np.diagflat(V @ self.agents.weights)
        A = ownership_matrix * (capital_gamma - capital_lambda)

        # compute the inverse of A and use it to compute eta
        try:
            A_inverse = scipy.linalg.inv(A)
        except (ValueError, scipy.linalg.LinAlgError):
            A_inverse = np.full_like(A, np.nan)
        eta = A_inverse @ self.products.shares

        # compute the tensor derivative of V with respect to xi (equivalently, to delta), indexed with the first axis
        probabilities_by_xi_tensor = -probabilities[np.newaxis] * probabilities[np.newaxis].swapaxes(0, 1)
        probabilities_by_xi_tensor[np.diag_indices(self.J)] += probabilities
        V_by_xi_tensor = probabilities_by_xi_tensor * derivatives

        # compute the tensor derivative of A with respect to xi
        capital_gamma_by_xi_tensor = (
            V @ square_weights @ probabilities_by_xi_tensor.swapaxes(1, 2) +
            V_by_xi_tensor @ (square_weights @ probabilities.T)
        )
        capital_lambda_by_xi_tensor = np.zeros_like(capital_gamma_by_xi_tensor)
        V_by_xi_tensor_times_weights = np.squeeze(V_by_xi_tensor @ self.agents.weights)
        capital_lambda_by_xi_tensor[:, np.arange(self.J), np.arange(self.J)] = V_by_xi_tensor_times_weights
        A_by_xi_tensor = ownership_matrix[np.newaxis] * (capital_gamma_by_xi_tensor - capital_lambda_by_xi_tensor)

        # compute the product of the tensor and eta
        A_by_xi_tensor_times_eta = np.squeeze(A_by_xi_tensor @ eta)

        # compute derivatives of X1 and X2 with respect to prices
        X1_derivatives = self.compute_X1_by_variable_derivatives('prices')
        X2_derivatives = self.compute_X2_by_variable_derivatives('prices')

        # fill the Jacobian of eta with respect to theta parameter-by-parameter
        eta_jacobian = np.zeros((self.J, nonlinear_parameters.P), options.dtype)
        for p, parameter in enumerate(nonlinear_parameters.unfixed):
            # compute the tangent of V with respect to the parameter
            x, v = parameter.get_characteristics(self.products, self.agents)
            probabilities_tangent = probabilities * v.T * (x - x.T @ probabilities)
            derivatives_tangent = (
                X1_derivatives @ beta_jacobian[:, [p]] +
                X2_derivatives[:, [parameter.location[0]]] @ v.T
            )
            V_tangent = probabilities_tangent * derivatives + probabilities * derivatives_tangent

            # compute the tangent of A with respect to the parameter
            capital_gamma_tangent = (
                V @ square_weights @ probabilities_tangent.T +
                V_tangent @ square_weights @ probabilities.T
            )
            capital_lambda_tangent = np.diagflat(V_tangent @ self.agents.weights)
            A_tangent = ownership_matrix * (capital_gamma_tangent - capital_lambda_tangent)

            # extract the tangent of xi with respect to the parameter and compute the associated tangent of eta
            eta_jacobian[:, [p]] = -A_inverse @ (A_tangent @ eta + A_by_xi_tensor_times_eta.T @ xi_jacobian[:, [p]])

        # return the filled Jacobian
        return eta_jacobian

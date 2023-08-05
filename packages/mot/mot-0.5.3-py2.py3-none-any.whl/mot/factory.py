from mot.cl_routines.optimizing.multi_step_optimizer import MultiStepOptimizer
from mot.cl_routines.optimizing.random_restart import RandomRestart
from mot.cl_routines.optimizing.sbplex import SBPlex
from mot.cl_routines.sampling.amwg import AdaptiveMetropolisWithinGibbs
from mot.cl_routines.sampling.scam import SingleComponentAdaptiveMetropolis
from .cl_routines.optimizing.levenberg_marquardt import LevenbergMarquardt
from .cl_routines.optimizing.nmsimplex import NMSimplex
from .cl_routines.optimizing.powell import Powell
from .load_balance_strategies import EvenDistribution, RuntimeLoadBalancing, PreferGPU, PreferCPU, \
    PreferSpecificEnvironment

__author__ = 'Robbert Harms'
__date__ = "2015-07-06"
__maintainer__ = "Robbert Harms"
__email__ = "robbert.harms@maastrichtuniversity.nl"


optimizers = [LevenbergMarquardt, Powell, NMSimplex, SBPlex, MultiStepOptimizer, RandomRestart]
samplers = [AdaptiveMetropolisWithinGibbs, SingleComponentAdaptiveMetropolis]
load_balance_strategies = [EvenDistribution, RuntimeLoadBalancing, PreferGPU, PreferCPU, PreferSpecificEnvironment]


def get_optimizer_by_name(name):
    """ Get the class by the given name.

    This does not instantiate the class, only returns a reference to it.

    Args:
        name: the name of the optimizer we want to return

    Returns:
        class: the class of the optimizer requested
    """
    return _get_item(name, optimizers, 'optimizers')


def get_sampler_by_name(name):
    """ Get the class by the given name.

    This does not instantiate the class, only returns a reference to it.

    Args:
        name: the name of the optimizer we want to return

    Returns:
        class: the class of the sampler requested
    """
    return _get_item(name, samplers, 'samplers')


def get_load_balance_strategy_by_name(name):
    """ Get the class by the given name.

    This does not instantiate the class, only returns a reference to it.

    Args:
        name: the name of the load balance strategy we want to return

    Returns:
        class: the class of the load balance strategy requested
    """
    return _get_item(name, load_balance_strategies, 'load balancers')


def _get_item(name, item_list, factory_type):
    for item in item_list:
        if item.__name__ == name:
            return item
    raise ValueError('The item with the name {0} could not be found in the {1} factory.'.format(name, factory_type))

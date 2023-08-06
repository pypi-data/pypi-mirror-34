# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 11:53:51 2016

@author: Villanueva
"""

# notTODO: INCLUDE .CIF FILE GENERATION OF LATTICE -> doesn't work with multiple sites...
# TODO: cooperative sensitization: in progress: SSA works for up and downconversion

import sys
import logging
import logging.config
from docopt import docopt
# nice debug printing of settings
import pprint
import os
from pkg_resources import resource_string
from typing import Any, Union, List, Optional, Dict

#import numpy as np
import matplotlib.pyplot as plt
import ruamel.yaml as yaml

import simetuc.lattice as lattice
import simetuc.simulations as simulations
import simetuc.settings as settings
import simetuc.optimize as optimize
from simetuc.util import disable_loggers

from simetuc import VERSION
from simetuc import DESCRIPTION

usage = f'''{DESCRIPTION}, version {VERSION}

Usage:
    simetuc (-h | --help)
    simetuc --version
    simetuc <config_filename> [options]
    simetuc <config_filename> -l [options]
    simetuc <config_filename> -d [options]
    simetuc <config_filename> -s [options]
    simetuc <config_filename> -p [options]
    simetuc <config_filename> -c [-d | --dynamics] [options]
    simetuc <config_filename> -o [-c | --concentration] [options]
    simetuc plot <saved_simulation.hdf5>
    
Commands:
    plot                              plots the results stored in saved_simulation.hdf5

Arguments:
    config_filename                   configuration filename for the simulation
    saved_simulation.hdf5             saved file to plot

Simulation types:
    -l, --lattice                     generate the lattice
    -d, --dynamics                    simulate dynamics
    -s, --steady-state                simulate steady state
    -p, --power-dependence            simulate power dependence of steady state
    -c, --concentration-dependence    simulate concentration dependence of the steady state or dynamics (with -d)
    -o, --optimize                    optimize the parameters of the dynamics for one or all concentrations (with -c)

Options:
    -v, --verbose                     show warnings and progress information
    -q, --quiet                       show only errors
    --no-plot                         don't show plots
    --average                         use average rate equations instead of microscopic
    --no-save                         don't save results
    -N, --N-samples N_SAMPLES         number of samples
'''

def parse_args(args: Any) -> Dict:
    d = docopt(usage, argv=args, help=True, version=VERSION, options_first=False)
    #print(d)
    return d

def _setup_logging(console_level: int, only_console: bool = False) -> None:
    '''Load logging settings from file and apply them.'''
    # read logging settings from file
    # use the file located where the package is installed
    _log_config_file = 'log_config.cfg'
    # resource_string opens the file and gets it as a string. Works inside .egg too
    try:
        _log_config_location = resource_string(__name__, os.path.join('config', _log_config_file))
    except NotImplementedError:  # pragma: no cover
        print('ERROR! Logging settings file ({}) not found!'.format(_log_config_file))
        print('Logging won\'t be available!!')
        # minimum settings without errors
        log_settings = {'version': 1}  # type: dict
    else:
        try:
            log_settings = yaml.safe_load(_log_config_location)
            # modify logging to console that the user wants
            log_settings['handlers']['console']['level'] = console_level
        except OSError:  # pragma: no cover
            print('ERROR! Logging settings file not found at {}!'.format(_log_config_location))
            print('Logging won\'t be available!!')
            log_settings = {'version': 1}  # minimum settings without errors
        else:
            os.makedirs('logs', exist_ok=True)
            
    if only_console:
        log_settings['handlers'] = {'console': log_settings['handlers']['console']}
        log_settings['root']['handlers'] = ['console']

    # load settings and rollover any rotating file handlers
    # so each execution of this program is logged to a fresh file
    logging.config.dictConfig(log_settings)
    logger = logging.getLogger('simetuc')
    for handler in logging.getLogger().handlers:  # pragma: no cover
        if isinstance(handler, logging.handlers.RotatingFileHandler):  # type: ignore
            handler.doRollover()

    logger.debug('Log settings dump:')
    logger.debug(pprint.pformat(log_settings))
    
def _stop_logging() -> None:
    for handler in logging.getLogger('simetuc').handlers:  # pragma: no cover
        handler.flush()
        handler.close()
        
    logging.shutdown()

def command_plot(args: Dict) -> None:
    '''User invoked the command plot'''
    logger = logging.getLogger('simetuc')

    filename = args['<saved_simulation.hdf5>']
    
    logger.info('Plotting saved file: ' + filename + '.')
    
    with disable_loggers(['simetuc.settings', 'settings_parser.settings']):
        if 'dynamics' in filename:
            sol = simulations.DynamicsSolution.load(filename)
        elif 'conc_dep' in filename:
            sol = simulations.ConcentrationDependenceSolution.load(filename)
        elif 'pow_dep' in filename:
            sol = simulations.PowerDependenceSolution.load(filename)
            
    sol.log_errors()
    sol.plot()
    logger.info('Close the plot window to exit.')
    plt.show()


def command_simulation(args: Dict) -> None:
    '''User invoked one of the simulation commands'''

    if args['--verbose']:
        no_console = False
    elif args['--quiet']:
        no_console = True
    else:
        no_console = False

    # show plots or not
    if args['--no-plot']:
        no_plot = True
    else:
        no_plot = False

    # load config file
    logger = logging.getLogger('simetuc')
    logger.info('Loading configuration...')
    cte = settings.load(args['<config_filename>'])
    cte['no_console'] = no_console
    cte['no_plot'] = no_plot
    N_samples = args.get('--N-samples', None)
    N_samples = int(N_samples) if N_samples else None
    cte['N_samples'] = N_samples

    # solution of the simulation
    solution: Union[simulations.Solution, simulations.SolutionList, optimize.OptimSolution, None] = None

    # choose what to do
    if args['--lattice']:  # create lattice
        logger.info('Creating and plotting lattice...')
        lattice.generate(cte)

    elif args['--dynamics'] and not args['--concentration-dependence']:  # simulate dynamics
        logger.info('Simulating dynamics...')
        sim = simulations.Simulations(cte)
        if args['--N-samples'] is not None:
            solution = sim.sample_simulation(sim.simulate_dynamics, N_samples=N_samples,
                                             average=args['--average'])
        else:
            solution = sim.simulate_dynamics(average=args['--average'])
        solution.log_errors()

    elif args['--steady-state']:  # simulate steady state
        logger.info('Simulating steady state...')
        sim = simulations.Simulations(cte)
        solution = sim.simulate_steady_state(average=args['--average'])
        solution.log_populations()

    elif args['--power-dependence']:  # simulate power dependence
        logger.info('Simulating power dependence...')
        sim = simulations.Simulations(cte)
        power_dens_list = cte.power_dependence
        solution = sim.simulate_power_dependence(power_dens_list, average=args['--average'])
        print('')

    elif args['--concentration-dependence'] and not args['--optimize']:  # simulate concentration dependence
        logger.info('Simulating concentration dependence...')
        sim = simulations.Simulations(cte)
        conc_list = cte.concentration_dependence['concentrations']
        N_uc_list = cte.concentration_dependence['N_uc_list']

        if args['--N-samples'] is not None:
            solution = sim.sample_simulation(sim.simulate_concentration_dependence,
                                             N_samples=N_samples,
                                             concentrations=conc_list, N_uc_list=N_uc_list, 
                                             dynamics=args['--dynamics'], average=args['--average'])
        else:
            solution = sim.simulate_concentration_dependence(conc_list, N_uc_list,
                                                             dynamics=args['--dynamics'],
                                                             average=args['--average'])
        solution.log_errors()

    elif args['--optimize']:  # optimize
        logger.info('Optimizing parameters...')
        if args['--concentration'] or args['--concentration-dependence']:
            solution = optimize.optimize_concentrations(cte, average=args['--average'],
                                                        N_samples=N_samples)
        else:
            solution = optimize.optimize_dynamics(cte, average=args['--average'],
                                                  N_samples=N_samples)

    # save results to disk
    if solution is not None and not args['--no-save']:
        logger.info('Saving results to file.')
        solution.save()
        solution.save_txt(cmd=' '.join(sys.argv))

    logger.info('Program finished!')

    # show all plots
    # the user needs to close the window to exit the program
    if not args['--no-plot']:
        if solution is not None:
            solution.plot()
        logger.info('Close the plot window to exit.')
        plt.show()


def main(ext_args: Optional[List[str]] = None) -> None:
    '''Main entry point for the command line interface'''
    if ext_args is None:  # pragma: no cover
        args = parse_args(sys.argv[1:])  # skip the program name
    else:
        args = parse_args(ext_args)

    # choose console logger level
    if args['--verbose'] or args['plot']:
        console_level = logging.INFO
    elif args['--quiet']:
        console_level = logging.ERROR
    else:
        console_level = logging.WARNING
    
    _setup_logging(console_level, only_console=args['plot'])
    
    logger = logging.getLogger('simetuc')
    logger.info('Starting program...')
    logger.debug('Called from cmd with arguments: %s.', args)

    if args['plot']:
        command_plot(args)
    else:        
        command_simulation(args)
        
    _stop_logging()


if __name__ == "__main__":
    ext_args = ['config_file.cfg', '-d']
    main()

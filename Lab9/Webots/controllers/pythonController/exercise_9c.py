"""Exercise 9c"""

import numpy as np
import plot_results
from run_simulation import run_simulation
from simulation_parameters import SimulationParameters


def exercise_9c(world, timestep, reset):
    Rhead = [0.1, 0.2, 0.3]
    Rtail = [0.1, 0.2, 0.3]
    parameter_set = [
        SimulationParameters(
            simulation_duration=10,
            #drive=drive,
            amplitude_gradient = True,
            amplitudes=[H, T],
            freqs = 1,
            phase_bias_vertical = 2*np.pi/10,
            turn=0,
        )
        for H in Rhead
        for T in Rtail
    ]

    # Grid search
    for simulation_i, parameters in enumerate(parameter_set):
        reset.reset()
        path = "./logs/9c/simulation_{}.npz".format(simulation_i)
        run_simulation(
            world,
            parameters,
            timestep,
            int(1000*parameters.simulation_duration/timestep),
            logs=path
            
        )
    plot_results.plot_9c(len(parameter_set))

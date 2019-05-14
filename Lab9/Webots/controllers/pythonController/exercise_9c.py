"""Exercise 9c"""

import numpy as np
from run_simulation import run_simulation
from simulation_parameters import SimulationParameters


def exercise_9c(world, timestep, reset):
    Rhead = [0.1, 0.3, 0.6]
    Rtail = [0.1, 0.3, 0.6]
    parameter_set = [
        SimulationParameters(
            simulation_duration=4,
            #drive=drive,
            amplitude_gradient = True,
            amplitudes=[H, T],
            freqs = 5,
            phase_bias_vertical = 2*np.pi/10,
            turn=0,
        )
        for H in Rhead
        for T in Rtail
    ]

    # Grid search
    for simulation_i, parameters in enumerate(parameter_set):
        reset.reset()
        path = "./logs/9b/simulation_{}.npz".format(simulation_i)
        run_simulation(
            world,
            parameters,
            timestep,
            int(1000*parameters.simulation_duration/timestep),
            logs=path
            
        )
    for i in range(9):
        plot_results.main("./logs/9b/simulation_{}.npz", i)

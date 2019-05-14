"""Exercise 9b"""

import numpy as np
from run_simulation import run_simulation
from simulation_parameters import SimulationParameters
import plot_results

def exercise_9b(world, timestep, reset):
    """Exercise 9b"""
        # Parameters
    amplitudes = [0.2, 0.5, 0.7]
    phase_bias = [np.pi/2, np.pi/4, np.pi/8] 
    parameter_set = [
        SimulationParameters(
            simulation_duration=4,
            #drive=drive,
            amplitudes= amp,
            phase_bias_vertical = phase,
            turn=0,
        )
        for amp in amplitudes
        for phase in phase_bias
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
        plot_results.main("./logs/9b/simulation_{}.npz".format(i), i)
        



"""Exercise 9f"""

import numpy as np
import plot_results
from run_simulation import run_simulation
from simulation_parameters import SimulationParameters


def exercise_9f(world, timestep, reset):
    """Exercise 9f"""
    amplitudes = np.linspace(0, 0.5, 10)
    
    parameter_set = [SimulationParameters(
        freq_coef_body = np.array([1, .5]), # [C_v1, C_v0] in HZ
        freq_coef_limb = np.array([1, 0.0]),
        amp_coef_body = np.array([amp, 0.0]), # [C_R1, C_R0] in radians
        amp_coef_limb = np.array([0.3, 0.0]), 
        simulation_duration = 10,
        drive = 1,
        walk = True,
    ) for amp in amplitudes]
    
    for i, parameters in enumerate(parameter_set):
        reset.reset()
        path = "./logs/9f/simulation_{}.npz".format(i)
        run_simulation(
            world,
            parameters,
            timestep,
            int(1000*parameters.simulation_duration/timestep),
            logs=path
        )
    
    plot_results.plot_9f(timestep,len(amplitudes), amplitudes)

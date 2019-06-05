"""Exercise 9f"""

import numpy as np
import plot_results
from run_simulation import run_simulation
from simulation_parameters import SimulationParameters


def exercise_9f(world, timestep, reset):
    """Exercise 9f"""
    phase_offset = np.linspace(0, 2*np.pi, 8)
    
    parameter_set = [SimulationParameters(
        freq_coef_body = np.array([1, .5]), # [C_v1, C_v0] in HZ
        freq_coef_limb = np.array([1, 0.0]),
        amp_coef_body = np.array([0.15, 0.0]), # [C_R1, C_R0] in radians
        amp_coef_limb = np.array([0.15, 0.0]), 
        simulation_duration=10,
        drive = 1,
        walk = True,
        phase_bias_limb_spine = fo
    ) for fo in phase_offset]
    
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
    
    plot_results.plot_9f(timestep,len(phase_offset), phase_offset)

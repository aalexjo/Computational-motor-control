"""Exercise 9d"""

import numpy as np
from run_simulation import run_simulation
from simulation_parameters import SimulationParameters


def exercise_9d1(world, timestep, reset):
    """Exercise 9d1"""

    parameters = SimulationParameters(
        simulation_duration=10,
        drive = 4,
        turn = 0.,
    )

    reset.reset()
    path = "./logs/9d1/simulation_{}.npz".format(0)
    run_simulation(
        world,
        parameters,
        timestep,
        int(1000*parameters.simulation_duration/timestep),
        logs=path
    )

    #plot_results.main("./logs/9b/simulation_{}.npz", i)



def exercise_9d2(world, timestep, reset):
    """Exercise 9d2"""
    parameters = SimulationParameters(
        simulation_duration=10,
        drive = -2,
    )

    reset.reset()
    path = "./logs/9d1/simulation_{}.npz".format(0)
    run_simulation(
        world,
        parameters,
        timestep,
        int(1000*parameters.simulation_duration/timestep),
        logs=path
    )


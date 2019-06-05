"""Exercise 9d"""

import numpy as np
import plot_results
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

    plot_results.plot_9d1()



def exercise_9d2(world, timestep, reset):
    """Exercise 9d2"""
    parameters = SimulationParameters(
        simulation_duration=7,
        drive = 3,
    )

    reset.reset()
    path = "./logs/9d2/simulation_{}.npz".format(0)
    run_simulation(
        world,
        parameters,
        timestep,
        int(1000*parameters.simulation_duration/timestep),
        logs=path
    )
    plot_results.plot_9d2()


"""Exercise 9f"""

import numpy as np
from run_simulation import run_simulation
from simulation_parameters import SimulationParameters


def exercise_9f(world, timestep, reset):
    """Exercise 9f"""
    parameters = SimulationParameters(
        simulation_duration=30,
        drive = 2,
        walk = True,
    )

    reset.reset()
    path = "./logs/9f/simulation_{}.npz".format(0)
    run_simulation(
        world,
        parameters,
        timestep,
        int(1000*parameters.simulation_duration/timestep),
        logs=path
    )


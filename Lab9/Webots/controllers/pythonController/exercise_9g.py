"""Exercise 9g"""

import plot_results
from run_simulation import run_simulation
from simulation_parameters import SimulationParameters


def exercise_9g(world, timestep, reset):
    """Exercise 9g"""
    parameters = SimulationParameters(
        simulation_duration=50,
        drive = 3,
        walk = True,
    )

    reset.reset()
    path = "./logs/9g/simulation_{}.npz".format(0)
    run_simulation(
        world,
        parameters,
        timestep,
        int(1000*parameters.simulation_duration/timestep),
        logs=path
    )
    plot_results.plot_9g()

"""Run simulation"""

import cmc_pylog as pylog
from cmc_robot import SalamanderCMC


def run_simulation(world, parameters, timestep, n_iterations, logs):
    """Run simulation"""

    # Set parameters
    pylog.info(
        "Running new simulation:\n  {}".format("\n  ".join([
            "{}: {}".format(key, value)
            for key, value in parameters.items()
        ]))
    )

    # Setup salamander control
    salamander = SalamanderCMC(
        world,
        n_iterations,
        logs=logs,
        parameters=parameters
    )
    
    switch = 1
    # Simulation
    iteration = 0
    while world.step(timestep) != -1:
        iteration += 1
        if iteration >= n_iterations:
            break
        
        if salamander.gps.getValues()[0] > switch:
            salamander.network.parameters.walk = False
            salamander.network.parameters.update(salamander.network.parameters.parameters)
            switch = 10
            print("doinit")
        salamander.step()

    # Log data
    pylog.info("Logging simulation data to {}".format(logs))
    salamander.log.save_data()


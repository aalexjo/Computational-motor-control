"""Run simulation"""

import numpy as np
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
    switch_T = np.inf
    switched = False
    # Simulation
    iteration = 0
    while world.step(timestep) != -1:
        iteration += 1
        if iteration >= n_iterations:
            break
        """
        if iteration == n_iterations//3:
            #salamander.network.parameters.turn = 0.1 #9d1
            salamander.network.parameters.drive = -3 
            salamander.network.parameters.update(salamander.network.parameters.parameters)
        if salamander.gps.getValues()[0] > switch and switched == False: #used for 9f
            
            salamander.network.parameters.walk = False
            salamander.network.parameters.update(salamander.network.parameters.parameters)
            switch_T = iteration
            print(switch_T)
            switched = True
        if salamander.gps.getValues()[0] < switch and switched == True:
            salamander.network.parameters.walk = True
            salamander.network.parameters.turn = 0
            salamander.network.parameters.update(salamander.network.parameters.parameters)
            swiched = True
        if iteration == switch_T + 600:
            print("turning")
            salamander.network.parameters.turn = -0.11
            salamander.network.parameters.update(salamander.network.parameters.parameters)
        elif iteration == switch_T + 3500:
            print("straight")
            salamander.network.parameters.turn = 0
            salamander.network.parameters.update(salamander.network.parameters.parameters)
        """

        
        salamander.step()

    # Log data
    pylog.info("Logging simulation data to {}".format(logs))
    salamander.log.save_data()


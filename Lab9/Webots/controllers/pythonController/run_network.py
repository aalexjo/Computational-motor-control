"""Run network without Webots"""

import time
import numpy as np
import matplotlib.pyplot as plt
import cmc_pylog as pylog
from network import SalamanderNetwork
from save_figures import save_figures
from parse_args import save_plots
from simulation_parameters import SimulationParameters


def run_network(duration, update=False, drive=0):
    """Run network without Webots and plot results"""
    # Simulation setup
    timestep = 5e-3
    times = np.arange(0, duration, timestep)
    n_iterations = len(times)
    parameters = SimulationParameters(
        #drive=drive,
        amplitude_gradient=None,
        phase_lag=None,
        turn=None,
    )
    network = SalamanderNetwork(timestep, parameters)
    osc_left = np.arange(10)
    osc_right = np.arange(10, 20)
    osc_legs = np.arange(20, 24)
    
    cw = np.zeros([24,24])
    for i in range(network.parameters.n_body_joints*2):
        for j in range(network.parameters.n_body_joints*2):
            if j == i+1 or j == i-1 or j == i+10 or j == i-10:
                cw[i][j] = 10
                
    cw[20][1:10] = 1
    cw[21][7:10] = 1
    cw[22][11:20] = 1
    cw[23][17:20] = 1
    for i in range(20,24):
        for j in range(20,24):
            if j == i+1 or j == i-1 or j == i+2 or j == i-2: 
                cw[i][j] = 10
    
    network.parameters.freqs = 3*np.ones(24)
    network.parameters.coupling_weights = cw
    network.parameters.nominal_amplitudes = 0.2*np.ones(24)
    #network.parameters.nominal_amplitudes[0] = 1
    
    fb = np.zeros([24,24])
    for i in range(network.parameters.n_body_joints*2):
        for j in range(network.parameters.n_body_joints*2):
            if j == i+1:
                fb[i][j] = -2*np.pi/8
            elif j == i-1:
                fb[i][j] = 2*np.pi/8
            elif j == i+10 or j == i-10:
                fb[i][j] = np.pi
                
    network.parameters.phase_bias = fb

    
    # Logs
    phases_log = np.zeros([
        n_iterations,
        len(network.state.phases)
    ])
    phases_log[0, :] = network.state.phases
    amplitudes_log = np.zeros([
        n_iterations,
        len(network.state.amplitudes)
    ])
    amplitudes_log[0, :] = network.state.amplitudes
    freqs_log = np.zeros([
        n_iterations,
        len(network.parameters.freqs)
    ])
    freqs_log[0, :] = network.parameters.freqs
    outputs_log = np.zeros([
        n_iterations,
        len(network.get_motor_position_output())
    ])
    outputs_log[0, :] = network.get_motor_position_output()

    # Run network ODE and log data
    tic = time.time()
    for i, _ in enumerate(times[1:]):
        if update:
            network.parameters.update(
                SimulationParameters(
                    # amplitude_gradient=None,
                    # phase_lag=None
                )
            )
        network.step()
        phases_log[i+1, :] = network.state.phases
        amplitudes_log[i+1, :] = network.state.amplitudes
        outputs_log[i+1, :] = network.get_motor_position_output()
        freqs_log[i+1, :] = network.parameters.freqs
    toc = time.time()

    # Network performance
    pylog.info("Time to run simulation for {} steps: {} [s]".format(
        n_iterations,
        toc - tic
    ))
    
    plt.figure('phases')
    plt.plot(phases_log)
    
    plt.figure('amplitude')
    plt.plot(amplitudes_log)
    
    plt.figure('frequency')
    plt.plot(freqs_log)
    
    plt.figure('out')
    plt.plot(outputs_log)



def main(plot):
    """Main"""

    run_network(duration=5)

    # Show plots
    if plot:
        plt.show()
    else:
        save_figures()


if __name__ == '__main__':
    main(plot=not save_plots())


"""Robot parameters"""

import numpy as np
import cmc_pylog as pylog


class RobotParameters(dict):
    """Robot parameters"""

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

    def __init__(self, parameters):
        super(RobotParameters, self).__init__()

        # Initialise parameters
        self.n_body_joints = parameters.n_body_joints
        self.n_legs_joints = parameters.n_legs_joints
        self.n_joints = self.n_body_joints + self.n_legs_joints
        self.n_oscillators_body = 2*self.n_body_joints
        self.n_oscillators_legs = self.n_legs_joints
        self.n_oscillators = self.n_oscillators_body + self.n_oscillators_legs
        self.freqs = np.zeros(self.n_oscillators)
        self.coupling_weights = np.zeros([
            self.n_oscillators,
            self.n_oscillators
        ])
        self.phase_bias = np.zeros([self.n_oscillators, self.n_oscillators])
        self.rates = np.zeros(self.n_oscillators)
        self.nominal_amplitudes = np.zeros(self.n_oscillators)
        self.update(parameters)

    def update(self, parameters):
        """Update network from parameters"""
        self.set_frequencies(parameters)  # f_i
        self.set_coupling_weights(parameters)  # w_ij
        self.set_phase_bias(parameters)  # theta_i
        self.set_amplitudes_rate(parameters)  # a_i
        self.set_nominal_amplitudes(parameters)  # R_i

    def set_frequencies(self, parameters):
        """Set frequencies"""
        self.freqs = 5*np.ones(24)
        #pylog.warning("Coupling weights must be set")

    def set_coupling_weights(self, parameters):
        """Set coupling weights"""
        cw = np.zeros([24,24])
        for i in range(parameters.n_body_joints*2):
            for j in range(parameters.n_body_joints*2):
                if j == i+1 or j == i-1 or j == i+10 or j == i-10:
                    cw[i][j] = 10
                    
#        cw[20][1:10] = 1
#        cw[21][7:10] = 1
#        cw[22][11:20] = 1
#        cw[23][17:20] = 1
#        for i in range(20,24):
#            for j in range(20,24):
#                if j == i+1 or j == i-1 or j == i+2 or j == i-2: 
#                    cw[i][j] = 10
        self.coupling_weights = cw
        #"pylog.warning("Coupling weights must be set")

    def set_phase_bias(self, parameters):
        """Set phase bias"""
        fb = np.zeros([24,24])
        for i in range(parameters.n_body_joints*2):
            for j in range(parameters.n_body_joints*2):
                if j == i+1:
                    fb[i][j] = -2*np.pi/8
                elif j == i-1:
                    fb[i][j] = 2*np.pi/8
                elif j == i+10 or j == i-10:
                    fb[i][j] = np.pi
                
        self.phase_bias = fb
        #pylog.warning("Phase bias must be set")

    def set_amplitudes_rate(self, parameters):
        """Set amplitude rates"""
        #self.rates = parameters.rates
        #pylog.warning("Convergence rates must be set")

    def set_nominal_amplitudes(self, parameters):
        """Set nominal amplitudes"""
        self.nominal_amplitudes = 0.5*np.ones(24)

        #self.nominal_amplitudes = parameters.nominal_amplitudes
        #pylog.warning("Nominal amplitudes must be set")


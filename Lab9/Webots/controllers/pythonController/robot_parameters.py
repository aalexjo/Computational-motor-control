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
        self.coupling_weights = np.zeros([self.n_oscillators,self.n_oscillators])
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
        self.freqs = parameters.freqs*np.ones(self.n_oscillators)
        #pylog.warning("Coupling weights must be set")

    def set_coupling_weights(self, parameters):
        """Set coupling weights"""
        cw = parameters.coupling_weight
        for i in range(parameters.n_body_joints*2):
            for j in range(parameters.n_body_joints*2):
                if j == i+1 or j == i-1 or j == i+10 or j == i-10:
                    self.coupling_weights[i][j] = cw
                    
#        cw[20][1:10] = cw
#        cw[21][7:10] = cw
#        cw[22][11:20] = cw
#        cw[23][17:20] = cw
#        for i in range(parameters.n_body_joints*2,parameters.n_body_joints*2+parameters.n_legs_joints):
#            for j in range(parameters.n_body_joints*2,parameters.n_body_joints*2+parameters.n_legs_joints):
#                if j == i+1 or j == i-1 or j == i+parameters.n_legs_joints/2 or j == i-parameters.n_legs_joints/2: 
#                    cw[i][j] = cw

    def set_phase_bias(self, parameters):
        """Set phase bias"""
        fb_vertical = parameters.phase_bias_vertical
        fb_lateral = parameters.phase_bias_lateral
        
        for i in range(parameters.n_body_joints*2):
            for j in range(parameters.n_body_joints*2):
                if j == i+1:
                    self.phase_bias[i][j] = -fb_vertical
                elif j == i-1:
                    self.phase_bias[i][j] = fb_vertical
                elif j == i+parameters.n_body_joints or j == i-parameters.n_body_joints:
                    self.phase_bias[i][j] = fb_lateral

    def set_amplitudes_rate(self, parameters):
        """Set amplitude rates"""
        #self.rates = parameters.rates
        #pylog.warning("Convergence rates must be set")

    def set_nominal_amplitudes(self, parameters):
        """Set nominal amplitudes"""
        #self.nominal_amplitudes = parameters.nominal_amplitudes*np.ones(self.n_oscillators)
        if parameters.amplitude_gradient == None: 
            self.nominal_amplitudes = 0.5*np.ones(24)
        if parameters.amplitude_gradient:             
            r_start = parameters.amplitudes[0]
            r_end = parameters.amplitudes[1]
            self.nominal_amplitudes = np.linspace(r_start, r_end,len(self.nominal_amplitudes))




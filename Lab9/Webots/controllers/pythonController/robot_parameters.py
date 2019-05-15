"""Robot parameters"""

import numpy as np
import cmc_pylog as pylog


class RobotParameters(dict):
    """Robot parameters"""

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

    def __init__(self, parameters):
        super(RobotParameters, self).__init__()
        self.parameters = parameters
        # Initialise parameters
        self.n_body_joints = parameters.n_body_joints
        self.n_legs_joints = parameters.n_legs_joints
        self.n_joints = self.n_body_joints + self.n_legs_joints
        self.n_oscillators_body = 2*self.n_body_joints
        self.n_oscillators_legs = self.n_legs_joints
        self.n_oscillators = self.n_oscillators_body + self.n_oscillators_legs
        self.walk = parameters.walk
        
        self.freqs = np.ones(self.n_oscillators)
        self.coupling_weights = np.zeros([self.n_oscillators,self.n_oscillators])
        self.phase_bias = np.zeros([self.n_oscillators, self.n_oscillators])
        self.rates = np.zeros(self.n_oscillators)
        self.nominal_amplitudes = np.ones(self.n_oscillators)
        self.drive = 0
        if parameters.drive:
            self.drive = parameters.drive
        
        self.update(parameters)

    def update(self, parameters):
        """Update network from parameters"""
        self.calculate_drive(parameters)
        self.set_frequencies(parameters)  # f_i
        self.set_coupling_weights(parameters)  # w_ij
        self.set_phase_bias(parameters)  # theta_i
        self.set_amplitudes_rate(parameters)  # a_i
        self.set_nominal_amplitudes(parameters)  # R_i

    def calculate_drive(self, paramaters):
        if self.drive:  
            drive = np.abs(self.drive)
            if drive > paramaters.d_limit_body[0] and drive < paramaters.d_limit_body[1]:
                self.freq_body = paramaters.freq_coef_body[0]*drive + paramaters.freq_coef_body[1]
                self.amp_body = paramaters.amp_coef_body[0]*drive + paramaters.amp_coef_body[1]
            else:
                self.freq_body = 0
                self.amp_body = 0
            if drive > paramaters.d_limit_limb[0] and drive < paramaters.d_limit_limb[1] and self.walk == True:
                self.freq_limb = paramaters.freq_coef_limb[0]*drive + paramaters.freq_coef_limb[1]
                self.amp_limb = paramaters.amp_coef_limb[0]*drive + paramaters.amp_coef_limb[1]
            else:
                self.freq_limb = 0
                self.amp_limb = 0
                
            
    def set_frequencies(self, parameters):
        """Set frequencies"""
        if self.drive:
            freqs_body_left   = self.freq_body*np.ones(self.n_body_joints)*(parameters.turn+1)
            freqs_body_right  = self.freq_body*np.ones(self.n_body_joints)*(-parameters.turn+1)
            freqs_limbs_left  = self.freq_limb*np.ones(self.n_legs_joints)*(parameters.turn+1)
            freqs_limbs_right = self.freq_limb*np.ones(self.n_legs_joints)*(-parameters.turn+1)
            self.freqs = np.concatenate((freqs_body_left, freqs_body_right, freqs_limbs_left, freqs_limbs_right))
        else:
            self.freqs = parameters.freqs*np.ones(self.n_oscillators)
        #pylog.warning("Coupling weights must be set")

    def set_coupling_weights(self, parameters):
        """Set coupling weights"""
        cw = parameters.coupling_weight
        cw_l = parameters.coupling_weight_limb
        for i in range(parameters.n_body_joints*2):
            for j in range(parameters.n_body_joints*2):
                if j == i+1 or j == i-1 or j == i+10 or j == i-10:
                    self.coupling_weights[i,j] = cw
        
        self.coupling_weights[0:6,20] = cw_l
        self.coupling_weights[6:10,21] = cw_l
        self.coupling_weights[10:16,22] = cw_l
        self.coupling_weights[16:20,23] = cw_l
        for i in range(parameters.n_body_joints*2,parameters.n_body_joints*2+parameters.n_legs_joints):
            for j in range(parameters.n_body_joints*2,parameters.n_body_joints*2+parameters.n_legs_joints):
                if j == i+1 or j == i-1 or j == i+parameters.n_legs_joints/2 or j == i-parameters.n_legs_joints/2: 
                    self.coupling_weights[i,j] = cw
        if parameters.drive:
            if parameters.drive < 0:
                self.coupling_weights = np.transpose(self.coupling_weights)
        np.core.arrayprint._line_width = 40
        np.set_printoptions(edgeitems=200, linewidth=200)
        print(self.coupling_weights)
        
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
                    
        self.phase_bias[0:6,20] = 0
        self.phase_bias[6:10,21] = 0
        self.phase_bias[10:16,22] = 0
        self.phase_bias[16:20,23] = 0
        for i in range(parameters.n_body_joints*2,parameters.n_body_joints*2+parameters.n_legs_joints):
            for j in range(parameters.n_body_joints*2,parameters.n_body_joints*2+parameters.n_legs_joints):
                if j == i+1 or j == i-1 or j == i+parameters.n_legs_joints/2 or j == i-parameters.n_legs_joints/2: 
                    self.phase_bias[i][j] = fb_lateral
        if parameters.drive:
            if parameters.drive < 0:
                self.phase_bias = np.transpose(self.phase_bias)
                
    def set_amplitudes_rate(self, parameters):
        """Set amplitude rates"""
        self.rates = parameters.amplitudes_rate*np.ones(self.n_oscillators)
        #pylog.warning("Convergence rates must be set")

    def set_nominal_amplitudes(self, parameters):
        """Set nominal amplitudes"""
        #self.nominal_amplitudes = parameters.nominal_amplitudes*np.ones(self.n_oscillators)
        if parameters.drive:
            amp_body_left   = self.amp_body*np.ones(self.n_body_joints)*(parameters.turn+1)
            amp_body_right  = self.amp_body*np.ones(self.n_body_joints)*(-parameters.turn+1)
            amp_limbs_left  = self.amp_limb*np.ones(self.n_legs_joints)*(parameters.turn+1)
            amp_limbs_right = self.amp_limb*np.ones(self.n_legs_joints)*(-parameters.turn+1)
            self.nominal_amplitudes = np.concatenate((amp_body_left, amp_body_right, amp_limbs_left, amp_limbs_right))
        elif parameters.amplitude_gradient == None: 
            self.nominal_amplitudes = parameters.nominal_amplitudes*np.ones(24)
        else:            
            r_start = parameters.amplitudes[0]
            r_end = parameters.amplitudes[1]
            self.nominal_amplitudes = np.linspace(r_start, r_end,len(self.nominal_amplitudes))
        



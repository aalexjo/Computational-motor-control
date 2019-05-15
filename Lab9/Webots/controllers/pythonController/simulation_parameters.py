"""Simulation parameters"""
import numpy as np

class SimulationParameters(dict):
    """Simulation parameters"""

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

    def __init__(self, **kwargs):
        super(SimulationParameters, self).__init__()
        # Default parameters
        self.n_body_joints = 10
        self.n_legs_joints = 4
        self.simulation_duration = 30
        self.phase_lag = None
        self.amplitude_gradient = None
        self.drive = 0
        self.turn = 0
        
        self.freqs = 5  # f_i
        self.coupling_weight = 10  # w_ij
        self.coupling_weight_limb = 30  # w_ij
        self.phase_bias_vertical = 2*np.pi/10  # theta_i
        self.phase_bias_lateral = np.pi
        self.amplitudes_rate = 20  # a_i
        self.nominal_amplitudes = 0.5  # R_i
        
        self.amplitudes = [0.5, 0.5]
        
        #----  drive parameters   ----
        self.d_limit_body = [1.0, 5.0] #[ dlow, dhigh ] in arbitrary units
        self.d_limit_limb = [1.0, 3.0] #
        
        self.freq_coef_body = [0.2, 0.3] # [C_v1, C_v0] in HZ
        self.freq_coef_limb = [0.2, 0.0] 
        
        self.amp_coef_body = [0.065, 0.196] # [C_R1, C_R0] in radians
        self.amp_coef_limb = [0.131, 0.131] 
        
        # Feel free to add more parameters (ex: MLR drive)
        # self.drive_mlr = ...
        # ...
        # Update object with provided keyword arguments

        
        self.update(kwargs)  # NOTE: This overrides the previous declarations


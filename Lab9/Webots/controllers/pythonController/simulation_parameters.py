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
        
        
        self.freqs = 5  # f_i
        self.coupling_weight = 10  # w_ij
        self.phase_bias_vertical = 2*np.pi/8  # theta_i
        self.phase_bias_lateral = np.pi
        self.amplitudes_rate = 20  # a_i
        self.nominal_amplitudes = 0.5  # R_i
        # Feel free to add more parameters (ex: MLR drive)
        # self.drive_mlr = ...
        # ...
        # Update object with provided keyword arguments

        
        self.update(kwargs)  # NOTE: This overrides the previous declarations


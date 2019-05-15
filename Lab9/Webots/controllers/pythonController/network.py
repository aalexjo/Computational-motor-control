"""Oscillator network ODE"""

import numpy as np

from solvers import euler, rk4
from robot_parameters import RobotParameters


def network_ode(_time, state, parameters):
    """Network_ODE

    returns derivative of state (phases and amplitudes)

    """
    phases = state[:parameters.n_oscillators]
    amplitudes = state[parameters.n_oscillators:2*parameters.n_oscillators]

    phase_dots = np.zeros(phases.shape)
    amp_dots=np.zeros(amplitudes.shape)
    
    for i in range(0,len(phases)): #For all parameters 

        phase_dots[i] = 2*np.pi*parameters.freqs[i]

        for j in range(0,len(phases)):
            phase_dots[i] += amplitudes[j] * parameters.coupling_weights[i,j] * np.sin(phases[j]-phases[i]-parameters.phase_bias[i,j])
            
        amp_dots[i] = parameters.rates[i]*(parameters.nominal_amplitudes[i]-amplitudes[i]) #Update amplitude diff_eq
    return np.concatenate([np.asarray(phase_dots), np.asarray(amp_dots)])


def motor_output(phases, amplitudes, parameters):
    """Motor output"""
    n = parameters.n_body_joints
    
    q_body = amplitudes[:n]*(1+np.cos(phases[:n])) - amplitudes[n:n*2]*(1+np.cos(phases[n:n*2]))
    q_limb = np.pi/2-phases[2*n:]

    return np.concatenate((q_body, q_limb))


class ODESolver(object):
    """ODE solver with step integration"""

    def __init__(self, ode, timestep, solver=rk4):
        super(ODESolver, self).__init__()
        self.ode = ode
        self.solver = solver
        self.timestep = timestep
        self._time = 0

    def integrate(self, state, *parameters):
        """Step"""
        diff_state = self.solver(
            self.ode,
            self.timestep,
            self._time,
            state,
            *parameters
        )
        self._time += self.timestep
        return diff_state

    def time(self):
        """Time"""
        return self._time


class RobotState(np.ndarray):
    """Robot state"""

    def __init__(self, *_0, **_1):
        super(RobotState, self).__init__()
        self[:] = 0.0

    @classmethod
    def salamandra_robotica_2(cls):
        """State of Salamandra robotica 2"""
        return cls(2*24, dtype=np.float64, buffer=np.zeros(2*24))

    @property
    def phases(self):
        """Oscillator phases"""
        return self[:24]

    @phases.setter
    def phases(self, value):
        self[:24] = value

    @property
    def amplitudes(self):
        """Oscillator phases"""
        return self[24:]

    @amplitudes.setter
    def amplitudes(self, value):
        self[24:] = value


class SalamanderNetwork(ODESolver):
    """Salamander oscillator network"""

    def __init__(self, timestep, parameters):
        super(SalamanderNetwork, self).__init__(
            ode=network_ode,
            timestep=timestep,
            solver=euler  # Feel free to switch between Euler (euler) or
                        # Runge-Kutta (rk4) integration methods
        )
        # States
        self.state = RobotState.salamandra_robotica_2()
        # Parameters
        self.parameters = RobotParameters(parameters)
        # Set initial state
        self.state.phases = 1e-4*np.random.ranf(self.parameters.n_oscillators)

    def step(self):
        """Step"""
        self.state += self.integrate(self.state, self.parameters)

    def get_motor_position_output(self):
        """Get motor position"""
        return motor_output(self.state.phases, self.state.amplitudes, self.parameters)


""" Hopf oscillator """


class HopfParameters(object):
    """ Hopf Parameters """

    def __init__(self, mu, omega):
        super(HopfParameters, self).__init__()
        self.mu = mu
        self.omega = omega

    def __str__(self):
        return self.msg()

    def msg(self):
        """ Message """
        return "mu: {}, omega: {}".format(self.mu, self.omega)

    def check(self):
        """ Check parameters """
        assert self.mu >= 0, "Mu must be positive"
        assert self.omega >= 0, "Omega must be positive"


class CoupledHopfParameters(HopfParameters):
    """ Coupled Hopf Parameters """

    def __init__(self, mu, omega, k):
        super(CoupledHopfParameters, self).__init__(mu, omega)
        self.k = k

    def msg(self):
        """ Message """
        return "mu: {}, omega: {}, k: {}".format(self.mu, self.omega, self.k)

    def check(self):
        """ Check parameters """
        assert self.mu >= 0, "Mu must be positive"
        assert self.omega >= 0, "Omega must be positive"
        assert self.k >= 0, "K must be positive"


def hopf_equation(x, _=None, params=HopfParameters(mu=1., omega=1.0)):
    """ Hopf oscillator equation """
    mu = params.mu
    omega = params.omega
    # biolog.warning("Hopf oscillator equation must be implemented")
    return [
        (mu - (x[0]**2 + x[1]**2)) * x[0] - omega * x[1],
        (mu - (x[0]**2 + x[1]**2)) * x[1] + omega * x[0]
    ]


def coupled_hopf_equation(x, _=None, params=None):
    """ Coupled Hopf oscillator equation """
    if params is None:
        params = CoupledHopfParameters(
            mu=[1., 1.],
            omega=[1.0, 1.2],
            k=[-0.5, -0.5]
        )
    mu = params.mu
    omega = params.omega
    k = params.k
    # biolog.warning("Coupled Hopf oscillator equation must be implemented")
    return [
        (mu[0] - (x[0]**2 + x[1]**2))*x[0] - omega[0]*x[1] + k[0]*x[2],
        (mu[0] - (x[0]**2 + x[1]**2))*x[1] + omega[0]*x[0],
        (mu[1] - (x[2]**2 + x[3]**2))*x[2] - omega[1]*x[3] + k[1]*x[0],
        (mu[1] - (x[3]**2 + x[2]**2))*x[3] + omega[1]*x[2]
    ]
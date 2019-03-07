""" Systems related codes for exercise 2 (Only for corrections) """

import numpy as np
import cmc_pylog as pylog

try:
    import sympy
    IMPORT_SYMPY = True
except ImportError:
    IMPORT_SYMPY = False


def fixed_point(A):
    """ Compute fixed point """
    x = sympy.symbols(["x{}".format(i) for i in range(2)])
    sol = sympy.solve(np.dot(A, x), x)
    x0 = sol[x[0]], sol[x[1]]
    pylog.info("Fixed point: {}".format(x0))


def eigen(A):
    """ Compute eigenvectors and eigenvalues """
    eigenvalues, eigenvectors = np.linalg.eig(A)
    pylog.info("Eigenvalues: {}".format(eigenvalues))
    pylog.info("Eigenvectors:\n{}".format(eigenvectors))
    return eigenvalues, eigenvectors


def system_analysis(A):
    """ Exercise 2.a - Analyse system """
    if IMPORT_SYMPY:
        fixed_point(A)
        eigen(A)
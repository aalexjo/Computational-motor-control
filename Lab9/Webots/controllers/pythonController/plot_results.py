"""Plot results"""

import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from cmc_robot import ExperimentLogger
from save_figures import save_figures
from parse_args import save_plots


def plot_positions(times, link_data):
    """Plot positions"""
    for i, data in enumerate(link_data.T):
        plt.plot(times, data, label=["x", "y", "z"][i])
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Distance [m]")
    plt.grid(True)


def plot_trajectory(link_data, lab = None):
    """Plot positions"""
    plt.plot(link_data[:, 0], link_data[:, 2], label = lab)
    plt.legend()
    plt.xlabel("x [m]")
    plt.ylabel("z [m]")
    plt.axis("equal")
    plt.grid(True)

def plot_joint_output(times, joints_data, lab = None):
    """Plot spine angles"""

    for i in np.arange(0,10,2):
        plt.plot(times[200:7000],joints_data[:,i,0][200:7000]-i*0.22, label = lab)
    for i in range(10,12):
        plt.plot(times[200:7000],0.5*np.cos(joints_data[:,i,0][200:7000])-i*1+7.5, label = lab)

    #plt.plot(times,joints_data[:,0,0], label = lab)
    plt.legend()
    #plt.title('Spine angles')
    plt.xlabel('time[s]')
    plt.ylabel('angle[rad]')
    
def plot_velocity(timestep, times, link_data, lab = None):
    plt.plot(times[1:], compute_velocity(timestep, link_data) ,label = lab)
    plt.legend()
    #plt.title('Salamander velocity')
    plt.xlabel('time[s]')
    plt.ylabel('Velocity[m/s]')

def compute_velocity(timestep, link_data):
    dist_array = link_data[1:]-link_data[:-1]
    vel_array = np.linalg.norm(dist_array, axis=1)/timestep
    return vel_array
    
def plot_2d(results, labels, n_data=300, log=False, cmap=None):
    """Plot result

    results - The results are given as a 2d array of dimensions [N, 3].

    labels - The labels should be a list of three string for the xlabel, the
    ylabel and zlabel (in that order).

    n_data - Represents the number of points used along x and y to draw the plot

    log - Set log to True for logarithmic scale.

    cmap - You can set the color palette with cmap. For example,
    set cmap='nipy_spectral' for high constrast results.

    """
    xnew = np.linspace(min(results[:, 0]), max(results[:, 0]), n_data)
    ynew = np.linspace(min(results[:, 1]), max(results[:, 1]), n_data)
    grid_x, grid_y = np.meshgrid(xnew, ynew)
    results_interp = griddata(
        (results[:, 0], results[:, 1]), results[:, 2],
        (grid_x, grid_y),
        method='linear'  # nearest, cubic
    )
    extent = (
        min(xnew), max(xnew),
        min(ynew), max(ynew)
    )
    plt.plot(results[:, 0], results[:, 1], "r.")
    imgplot = plt.imshow(
        results_interp,
        extent=extent,
        aspect='auto',
        origin='lower',
        interpolation="none",
        norm=LogNorm() if log else None
    )
    if cmap is not None:
        imgplot.set_cmap(cmap)
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    cbar = plt.colorbar()
    cbar.set_label(labels[2])


def main(plot=True):
    """Main"""
    # Load data
    with np.load('logs/example/simulation_0.npz') as data:
        timestep = float(data["timestep"])
        amplitude = data["amplitudes"]
        phase_lag = data["phase_lag"]
        link_data = data["links"][:, 0, :]
        joints_data = data["joints"]
    times = np.arange(0, timestep*np.shape(link_data)[0], timestep)

    # Plot data
    plt.figure("Positions")
    plot_positions(times, link_data)

    # Show plots
    if plot:
        plt.show()
    else:
        save_figures()
        
       
def plot_9c(num_plots):
    """custom function for plotting task 9d1"""
    # Load data
    avg_velocity = np.array([])
    for i in range(num_plots):
        with np.load('logs/9c/simulation_{}.npz'.format(i)) as data:
            timestep = float(data["timestep"])
            amplitude = data["amplitudes"]
            #phase_lag = data["phase_lag"]
            link_data = data["links"][:, 0, :]
            joints_data = data["joints"]
        times = np.arange(0, timestep*np.shape(link_data)[0], timestep)
    
        # Plot data
        plt.figure("Trajectory")
        plot_trajectory(link_data)
    plot = True
    # Show plots
    if plot:
        plt.show()
    else:
        save_figures()  
        
def plot_9d1():
    """custom function for plotting task 9d1"""
    # Load data
    with np.load('logs/9d1/simulation_0.npz') as data:
        timestep = float(data["timestep"])
        amplitude = data["amplitudes"]
        #phase_lag = data["phase_lag"]
        link_data = data["links"][:, 0, :]
        joints_data = data["joints"]
    times = np.arange(0, timestep*np.shape(link_data)[0], timestep)

    # Plot data
    plt.figure("Trajectory")
    plot_trajectory(link_data)
    
    plt.figure("joint angles")
    plot_joint_output(times, joints_data)
    
    plot = True
    # Show plots
    if plot:
        plt.show()
    else:
        save_figures()  

def plot_9d2():
    """custom function for plotting task 9d2"""
    # Load data
    with np.load('logs/9d2/simulation_0.npz') as data:
        timestep = float(data["timestep"])
        amplitude = data["amplitudes"]
        #phase_lag = data["phase_lag"]
        link_data = data["links"][:, 0, :]
        joints_data = data["joints"]
    times = np.arange(0, timestep*np.shape(link_data)[0], timestep)

    # Plot data
    plt.figure("Trajectory")
    plot_trajectory(link_data)
    
    plt.figure("joint angles")
    plot_joint_output(times, joints_data)
    
    plot = True
    # Show plots
    if plot:
        plt.show()
    else:
        save_figures()  
        
def plot_9f(timestep,num_plots, labels):
    """custom function for plotting task 9d1"""
    # Load data
    avg_velocity = np.array([])
    for i in range(num_plots):
        with np.load('logs/9f/simulation_{}.npz'.format(i)) as data:
            timestep = float(data["timestep"])
            amplitude = data["amplitudes"]
            #phase_lag = data["phase_lag"]
            link_data = data["links"][:, 0, :]
            joints_data = data["joints"]
        times = np.arange(0, timestep*np.shape(link_data)[0], timestep)
    
        # Plot data
        plt.figure("Trajectory")
        plot_trajectory(link_data, lab = labels[i])
        
        plt.figure("joint angles")
        plot_joint_output(times, joints_data, lab = labels[i])
        avg_velocity = np.append(avg_velocity, np.average(compute_velocity(timestep, link_data)))
        
    plt.figure("Avg Velocity")
    plt.plot(labels, avg_velocity)

def plot_9g():
    """custom function for plotting task 9d2"""
    # Load data
    with np.load('logs/9g/simulation_0.npz') as data:
        timestep = float(data["timestep"])
        amplitude = data["amplitudes"]
        #phase_lag = data["phase_lag"]
        link_data = data["links"][:, 0, :]
        joints_data = data["joints"]
    times = np.arange(0, timestep*np.shape(link_data)[0], timestep)

    # Plot data
    plt.figure("Trajectory")
    plot_trajectory(link_data)
    
    plt.figure("Joint angles")
    plot_joint_output(times, joints_data)
    
    plot = True
    # Show plots
    if plot:
        plt.show()
    else:
        save_figures() 
        
    
    plot = True
    # Show plots
    if plot:
        plt.show()
    else:
        save_figures()  

if __name__ == '__main__':
    #main(plot=not save_plots())
    plot_9c(9)
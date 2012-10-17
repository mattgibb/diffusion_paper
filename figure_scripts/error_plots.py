#!/usr/bin/env python
"""
plots the evolving ground truth errors of each slice

Usage:
./error_plots.py

"""

# from sys import argv
from os import listdir
from os.path import *
from sys import argv
from numpy import *
from scipy.stats.mstats import gmean

# plot 3d line
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# constants
PROJECT_ROOT = str(realpath(join(__file__, '..', '..')))
FIGURE_PATH = str(join(PROJECT_ROOT, '2_methods/Figs/'))

# absolute and relative info
absolute_info = {"dir": "GroundTruthErrors",         "figure_name": "absolute_errors", "log": False}
relative_info = {"dir": "RelativeGroundTruthErrors", "figure_name": "relative_errors", "log": True}
    
# construct error directory
errors_root = "/Users/matt/Code/imaging/registration/results/dummy/200_alpha0.4rt/HiResPairs/"
for info in (absolute_info, relative_info):
    errors_path = errors_root + info["dir"]
    banana_errors_path = errors_root + "Banana" + info["dir"]
    
    # read errors
    error_files = sorted(listdir(errors_path), key=int)
    errors = transpose(array([genfromtxt(join(errors_path, file)) for file in error_files]))
    banana_errors = genfromtxt(join(banana_errors_path, "1"))
    
    # plot
    fig3d = plt.figure(frameon=False)
    ax = fig3d.add_axes([0.0,0.0,1.0,1.0], projection='3d')
    for i, slice in enumerate(errors):
        x = range(len(slice))
        y = [i] * len(slice)
        ax.plot(x, y, slice)
    plt.xlabel('Smoothing Iteration', fontsize='xx-large')
    plt.ylabel('Slice Number', fontsize='xx-large')
    ax.set_zlabel("Mean Euclidian Distance Error", fontsize='xx-large')
    plt.show()
    # fig3d.savefig(join(FIGURE_PATH, info["figure_name"] + "_3d.pdf"))

    # 2d plots
    # error before smoothing, after 40 smoothings, and after banana registration
    fig2d = plt.figure(figsize=(10, 6))
    ax = fig2d.add_axes([0.12,0.1,0.85,0.85])
    values = hstack((errors[:,(0,40)],banana_errors[None].T))
    x = range(len(values))
    ax.plot(x, values)
    plt.xlabel('Smoothing Iteration', fontsize='xx-large')
    plt.ylabel("Log Mean Euclidian Distance Error", fontsize='xx-large')
    plt.tick_params(axis='both', which='major', labelsize=16)
    if info["log"]: ax.set_yscale('log')
    # plt.ylim([0,1800])
    plt.grid(axis="y")
    # plt.show()
    fig2d.savefig(join(FIGURE_PATH, info["figure_name"] + "_2d.pdf"))
    
    if info["log"]:
        print("Relative arithmetic means:")
        print(mean(values, axis=0))        
        print("Relative geometric means:")
        print(gmean(values))
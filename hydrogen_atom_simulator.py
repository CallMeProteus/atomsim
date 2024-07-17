import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import random
import time
from electron_simulation import ElectronSimulation
from probability_calculation import ProbabilityCalculation

class HydrogenAtomSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Hydrogen Atom Simulator")
        
        # Initialize simulation parameters
        self.initialize_params()
        
        # Set up GUI elements
        self.setup_gui()
        
        # Create instances of other modules
        self.electron_simulation = ElectronSimulation(self)
        self.probability_calculation = ProbabilityCalculation(self)
        
    def initialize_params(self):
        # Simulation parameters
        self.BOHRS_RADIUS = 0.52917721067e-10
        self.Z = 1
        self.N = 1000
        self.W, self.H = 500, 500
        self.NUCLEUS_RADIUS = 40
        self.ORBIT_RADIUS_1, self.ORBIT_RADIUS_2, self.ORBIT_RADIUS_3 = 94, 85, 75
        self.ELECTRON_SPEED_RANGE = (20, 60)
        self.NE = 30  # number of electrons
        
    def setup_gui(self):
        # GUI setup
        self.control_frame = tk.Frame(self.master)
        self.control_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        self.viz_frame = tk.Frame(self.master)
        self.viz_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        
        # Add controls
        tk.Button(self.control_frame, text="Run 2D Simulation", command=self.run_2d_simulation).pack()
        tk.Button(self.control_frame, text="Run 3D Simulation", command=self.run_3d_simulation).pack()
        tk.Button(self.control_frame, text="Calculate Probabilities", command=self.calculate_probabilities).pack()
        
        # Set up canvas for 2D animation
        self.canvas_2d = tk.Canvas(self.viz_frame, width=self.W, height=self.H, bg="black")
        self.canvas_2d.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        
        # Set up matplotlib figure for 3D plot
        self.fig = plt.Figure(figsize=(5, 5))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas_3d = FigureCanvasTkAgg(self.fig, master=self.viz_frame)
        self.canvas_3d.draw()
        self.canvas_3d.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
        
    def run_2d_simulation(self):
        self.electron_simulation.run_2d_simulation()
        
    def run_3d_simulation(self):
        self.probability_calculation.run_3d_simulation()
        
    def calculate_probabilities(self):
        self.probability_calculation.calculate_probabilities()
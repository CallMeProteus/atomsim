import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ProbabilityClouds:
    def __init__(self, master):
        self.master = master
        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def hydrogen_1s(self, x, y, z, a0=1):
        r = np.sqrt(x**2 + y**2 + z**2)
        return (1 / (np.pi * a0**3))**0.5 * np.exp(-r / a0)

    def draw(self):
        x = np.linspace(-10, 10, 100)
        y = np.linspace(-10, 10, 100)
        X, Y = np.meshgrid(x, y)
        Z = self.hydrogen_1s(X, Y, 0)
        
        self.ax.clear()
        self.ax.contourf(X, Y, Z, levels=20, cmap='viridis')
        self.ax.set_title("Hydrogen 1s Orbital Probability Density")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.canvas.draw()

    def run(self):
        self.draw()
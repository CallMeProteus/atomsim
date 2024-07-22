import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ClassicalVsQuantum:
    def __init__(self, master):
        self.master = master
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(10, 5))
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.time = 0

    def classical_orbit(self, t, a=1, omega=1):
        x = a * np.cos(omega * t)
        y = a * np.sin(omega * t)
        return x, y

    def quantum_density(self, x, y, a0=1):
        r = np.sqrt(x**2 + y**2)
        return (1 / (np.pi * a0**2)) * np.exp(-2*r / a0)

    def draw(self):
        # Classical orbit
        t = np.linspace(0, 2*np.pi, 100)
        x, y = self.classical_orbit(t)
        self.ax1.clear()
        self.ax1.plot(x, y)
        self.ax1.set_title("Classical Orbit")
        self.ax1.set_xlim(-1.5, 1.5)
        self.ax1.set_ylim(-1.5, 1.5)
        self.ax1.set_aspect('equal')
        
        # Current position
        current_x, current_y = self.classical_orbit(self.time)
        self.ax1.plot(current_x, current_y, 'ro')

        # Quantum probability density
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        Z = self.quantum_density(X, Y)
        
        self.ax2.clear()
        self.ax2.contourf(X, Y, Z, levels=20, cmap='viridis')
        self.ax2.set_title("Quantum Probability Density")
        self.ax2.set_aspect('equal')

        self.canvas.draw()

    def animate(self):
        self.time += 0.1
        self.draw()
        self.master.after(50, self.animate)

    def run(self):
        self.animate()
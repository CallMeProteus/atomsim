import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class BohrModel3D:
    def __init__(self, master):
        self.master = master
        self.fig = Figure(figsize=(6, 6))
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.nucleus_radius = 0.2
        self.orbit_radii = [1, 2, 3, 4]
        self.electrons = [
            {'orbit': 0, 'theta': 0, 'phi': 0},
            {'orbit': 1, 'theta': np.pi/2, 'phi': 0},
            {'orbit': 2, 'theta': np.pi/4, 'phi': np.pi/4}
        ]

    def draw_sphere(self, radius, color):
        u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
        x = radius * np.cos(u) * np.sin(v)
        y = radius * np.sin(u) * np.sin(v)
        z = radius * np.cos(v)
        self.ax.plot_surface(x, y, z, color=color, alpha=0.6)

    def draw_orbit(self, radius):
        u = np.linspace(0, 2 * np.pi, 100)
        x = radius * np.cos(u)
        y = radius * np.sin(u)
        z = np.zeros_like(u)
        self.ax.plot(x, y, z, color='gray', alpha=0.5)

    def draw(self):
        self.ax.clear()
        
        # Draw nucleus
        self.draw_sphere(self.nucleus_radius, 'red')
        
        # Draw orbits
        for radius in self.orbit_radii:
            self.draw_orbit(radius)
        
        # Draw electrons
        for electron in self.electrons:
            radius = self.orbit_radii[electron['orbit']]
            theta, phi = electron['theta'], electron['phi']
            x = radius * np.sin(theta) * np.cos(phi)
            y = radius * np.sin(theta) * np.sin(phi)
            z = radius * np.cos(theta)
            self.ax.scatter([x], [y], [z], color='blue', s=50)

        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-5, 5)
        self.ax.set_zlim(-5, 5)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.set_title("3D Bohr Model")

        self.canvas.draw()

    def animate(self):
        for electron in self.electrons:
            electron['phi'] += 0.1
            electron['theta'] += 0.05
        self.draw()
        self.master.after(50, self.animate)

    def run(self):
        self.animate()
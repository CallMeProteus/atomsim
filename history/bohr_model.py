import tkinter as tk
import math

class BohrModel:
    def __init__(self, canvas):
        self.canvas = canvas
        self.width = 400
        self.height = 400
        self.center_x = self.width // 2
        self.center_y = self.height // 2
        self.nucleus_radius = 20
        self.orbit_radii = [60, 100, 140, 180]
        self.electrons = [
            {'orbit': 0, 'angle': 0},
            {'orbit': 1, 'angle': 0},
            {'orbit': 2, 'angle': 0}
        ]

    def draw(self):
        self.canvas.delete("all")
        
        # Draw nucleus
        self.canvas.create_oval(
            self.center_x - self.nucleus_radius,
            self.center_y - self.nucleus_radius,
            self.center_x + self.nucleus_radius,
            self.center_y + self.nucleus_radius,
            fill="red"
        )
        
        # Draw orbits
        for radius in self.orbit_radii:
            self.canvas.create_oval(
                self.center_x - radius,
                self.center_y - radius,
                self.center_x + radius,
                self.center_y + radius,
                outline="gray"
            )
        
        # Draw electrons
        for electron in self.electrons:
            radius = self.orbit_radii[electron['orbit']]
            x = self.center_x + radius * math.cos(electron['angle'])
            y = self.center_y + radius * math.sin(electron['angle'])
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")

    def animate(self):
        for electron in self.electrons:
            electron['angle'] += 0.1
        self.draw()
        self.canvas.after(50, self.animate)

    def run(self):
        self.animate()
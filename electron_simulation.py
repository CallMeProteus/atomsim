import math
import random
import time

class ElectronSimulation:
    def __init__(self, hydrogen_atom_simulator):
        self.hydrogen_atom_simulator = hydrogen_atom_simulator
        
    def create_electrons(self, n, r):
        # Create electrons
        electrons = []
        for i in range(n):
            a = i * 2 * math.pi / n
            x, y = self.hydrogen_atom_simulator.W // 2 + r * math.cos(a), self.hydrogen_atom_simulator.H // 2 + r * math.sin(a)
            c = "#0000FF"
            d, s = random.choice([-1, 1]), random.uniform(*self.hydrogen_atom_simulator.ELECTRON_SPEED_RANGE)
            electrons.append({"x": x, "y": y, "color": c, "direction": d, "speed": s})
        return electrons
        
    def animate_2d(self, e1, e2, e3):
        # Animate 2D simulation
        self.hydrogen_atom_simulator.canvas_2d.delete("all")
        x, y = self.hydrogen_atom_simulator.W // 2, self.hydrogen_atom_simulator.H // 2
        self.hydrogen_atom_simulator.canvas_2d.create_oval(x - self.hydrogen_atom_simulator.NUCLEUS_RADIUS, y - self.hydrogen_atom_simulator.NUCLEUS_RADIUS, 
                                       x + self.hydrogen_atom_simulator.NUCLEUS_RADIUS, y + self.hydrogen_atom_simulator.NUCLEUS_RADIUS, fill="red")
        self.hydrogen_atom_simulator.canvas_2d.create_text(x, y, text="Nucleus", fill="white")
        
        for e in e1 + e2 + e3:
            a = time.time() * e["direction"] * e["speed"] * 2 * math.pi / 500
            r = self.hydrogen_atom_simulator.ORBIT_RADIUS_1 if e in e1 else (self.hydrogen_atom_simulator.ORBIT_RADIUS_2 if e in e2 else self.hydrogen_atom_simulator.ORBIT_RADIUS_3)
            x, y = self.hydrogen_atom_simulator.W // 2 + r * math.cos(a), self.hydrogen_atom_simulator.H // 2 + r * math.sin(a)
            self.hydrogen_atom_simulator.canvas_2d.create_oval(x - 5, y - 5, x + 5, y + 5, fill=e["color"])
        
        self.hydrogen_atom_simulator.canvas_2d.after(10, self.animate_2d, e1, e2, e3)
        
    def run_2d_simulation(self):
        # Run 2D simulation
        electrons1 = self.create_electrons(self.hydrogen_atom_simulator.NE, self.hydrogen_atom_simulator.ORBIT_RADIUS_1)
        electrons2 = self.create_electrons(self.hydrogen_atom_simulator.NE, self.hydrogen_atom_simulator.ORBIT_RADIUS_2)
        electrons3 = self.create_electrons(self.hydrogen_atom_simulator.NE, self.hydrogen_atom_simulator.ORBIT_RADIUS_3)
        self.animate_2d(electrons1, electrons2, electrons3)
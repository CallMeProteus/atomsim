import math
import random
import tkinter as tk

class ProbabilityCalculation:
    def __init__(self, hydrogen_atom_simulator):
        self.hydrogen_atom_simulator = hydrogen_atom_simulator
        
    def R(self, r):
        # Radial wavefunction
        return (2 / self.hydrogen_atom_simulator.BOHRS_RADIUS)**(3/2) * math.exp(-self.hydrogen_atom_simulator.Z*r/self.hydrogen_atom_simulator.BOHRS_RADIUS) / math.sqrt(math.factorial(2*self.hydrogen_atom_simulator.Z - 1)) * (2*self.hydrogen_atom_simulator.Z*r/self.hydrogen_atom_simulator.BOHRS_RADIUS)**(self.hydrogen_atom_simulator.Z-1) * math.exp(-self.hydrogen_atom_simulator.Z*r/(2*self.hydrogen_atom_simulator.BOHRS_RADIUS)) * math.pow(r/self.hydrogen_atom_simulator.BOHRS_RADIUS, 2*self.hydrogen_atom_simulator.Z-2)
        
    def probability_density(self, r, theta, phi):
        # Probability density function
        return self.R(r)**2 * r**2 * math.sin(theta)
        
    def run_3d_simulation(self):
        # Run 3D simulation
        r_samples = []
        theta_samples = []
        phi_samples = []
        
        for i in range(self.hydrogen_atom_simulator.N):
            r = random.uniform(0, 10*self.hydrogen_atom_simulator.BOHRS_RADIUS)
            theta = random.uniform(0, math.pi)
            phi = random.uniform(0, 2*math.pi)
            r_samples.append(r)
            theta_samples.append(theta)
            phi_samples.append(phi)
        
        prob_density = [self.probability_density(r_samples[i], theta_samples[i], phi_samples[i]) for i in range(self.hydrogen_atom_simulator.N)]
        
        self.hydrogen_atom_simulator.ax.clear()
        scatter = self.hydrogen_atom_simulator.ax.scatter(r_samples, theta_samples, phi_samples, c=prob_density, cmap='viridis')
        self.hydrogen_atom_simulator.ax.scatter([0], [0], [0], s=100, marker='o', color='red')
        self.hydrogen_atom_simulator.ax.set_xlabel('r')
        self.hydrogen_atom_simulator.ax.set_ylabel('theta')
        self.hydrogen_atom_simulator.ax.set_zlabel('phi')
        self.hydrogen_atom_simulator.ax.set_title('Distribution of electron position')
        self.hydrogen_atom_simulator.fig.colorbar(scatter)
        self.hydrogen_atom_simulator.canvas_3d.draw()
        
    def calculate_probabilities(self):
        # Calculate probabilities
        r_samples = []
        theta_samples = []
        phi_samples = []
        
        for i in range(self.hydrogen_atom_simulator.N):
            r = random.uniform(0, 10*self.hydrogen_atom_simulator.BOHRS_RADIUS)
            theta = random.uniform(0, math.pi)
            phi = random.uniform(0, 2*math.pi)
            r_samples.append(r)
            theta_samples.append(theta)
            phi_samples.append(phi)
        
        prob_density = [self.probability_density(r_samples[i], theta_samples[i], phi_samples[i]) for i in range(self.hydrogen_atom_simulator.N)]
        
        dr = 0.1*self.hydrogen_atom_simulator.BOHRS_RADIUS
        prob = []
        for r in range(int(10*self.hydrogen_atom_simulator.BOHRS_RADIUS/dr)):
            r_min = r*dr
            r_max = (r+1)*dr
            vol_shell = 4*math.pi*(r_max**3 - r_min**3)/3
            prob_shell = sum([prob_density[i] for i in range(self.hydrogen_atom_simulator.N) if r_min <= r_samples[i] <= r_max])
            prob.append(prob_shell / vol_shell)
        
        result_window = tk.Toplevel(self.hydrogen_atom_simulator.master)
        result_window.title("Probability Results")
        result_text = tk.Text(result_window)
        result_text.pack()
        
        for i in range(len(prob)):
            r_min = i*dr
            r_max = (i+1)*dr
            result_text.insert(tk.END, f"Probability of electron between {r_min/self.hydrogen_atom_simulator.BOHRS_RADIUS:.2f} and {r_max/self.hydrogen_atom_simulator.BOHRS_RADIUS:.2f} Bohr radii: {prob[i]:.6e}\n")
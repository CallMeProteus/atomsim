import tkinter as tk
from tkinter import ttk
from bohr_model import BohrModel
from probability_clouds import ProbabilityClouds
from classical_vs_quantum import ClassicalVsQuantum
from threed_bohr_model import BohrModel3D

class AtomVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Atom Visualizer")
        
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Bohr Model Tab
        bohr_frame = ttk.Frame(self.notebook)
        self.notebook.add(bohr_frame, text="Bohr Model")
        bohr_canvas = tk.Canvas(bohr_frame, width=400, height=400)
        bohr_canvas.pack()
        self.bohr_model = BohrModel(bohr_canvas)

        #3d model of bohrs atom
        # threed_bohr_frame = ttk.Frame(self.notebook)
        # self.notebook.add(threed_bohr_frame, text="3D Bohr Model")
        # self.threed_bohr_model = BohrModel3D(threed_bohr_frame)
        
        # Probability Clouds Tab
        prob_frame = ttk.Frame(self.notebook)
        self.notebook.add(prob_frame, text="Probability Clouds")
        self.prob_clouds = ProbabilityClouds(prob_frame)
        
        # Classical vs Quantum Tab
        cvq_frame = ttk.Frame(self.notebook)
        self.notebook.add(cvq_frame, text="Classical vs Quantum")
        self.cvq = ClassicalVsQuantum(cvq_frame)
        
    def run(self):
        self.bohr_model.run()
        # self.threed_bohr_model.run()
        self.prob_clouds.run()
        self.cvq.run()

if __name__ == "__main__":
    root = tk.Tk()
    app = AtomVisualizer(root)
    app.run()
    root.mainloop()
import tkinter as tk
from hydrogen_atom_simulator import HydrogenAtomSimulator

if __name__ == "__main__":
    root = tk.Tk()
    app = HydrogenAtomSimulator(root)
    root.mainloop()
import tkinter as tk
import math, time, random


# Constants
W, H = 500, 500
NUCLEUS_RADIUS = 40
ORBIT_RADIUS_1, ORBIT_RADIUS_2, ORBIT_RADIUS_3 = 94, 85,75
ELECTRON_SPEED_RANGE = (20, 60)
NE = 30#number of electrons
# Initialize tkinter
root = tk.Tk()
root.title('Hydrogen Atom by group 1')
canvas = tk.Canvas(root, width=W, height=H, bg="black")
canvas.pack()

# Define function to create electrons
def create_electrons(n, r):
    electrons = []
    for i in range(n):
        a = i * 2 * math.pi / n
        x, y = W // 2 + r * math.cos(a), H // 2 + r * math.sin(a)
        c = random.choice(["#0000FF",])# add more colors to see electrons in different colors
        d, s = random.choice([-1, 1]), random.uniform(*ELECTRON_SPEED_RANGE)
        electrons.append({"x": x, "y": y, "color": c, "direction": d, "speed": s})
    return electrons

# Define animation function
def animate(e1, e2,e3):
    canvas.delete("all")
    x, y = W // 2, H // 2
    canvas.create_oval(x - NUCLEUS_RADIUS, y - NUCLEUS_RADIUS, x + NUCLEUS_RADIUS, y + NUCLEUS_RADIUS, fill="red")
    canvas.create_text(x, y, text="Nucleus", fill="white")
    for e in e1:
        a = time.time() * e["direction"] * e["speed"] * 2 * math.pi / 500
        x, y = W // 2 + ORBIT_RADIUS_1 * math.cos(a), H // 2 + ORBIT_RADIUS_1 * math.sin(a)
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=e["color"])
    for e in e2:
        a = time.time() * e["direction"] * e["speed"] * 2 * math.pi / 500
        x, y = W // 2 + ORBIT_RADIUS_2 * math.cos(a), H // 2 + ORBIT_RADIUS_2 * math.sin(a)
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=e["color"])
    for e in e3:
        a = time.time() * e["direction"] * e["speed"] * 2 * math.pi / 500
        x, y = W // 2 + ORBIT_RADIUS_3 * math.cos(a), H // 2 + ORBIT_RADIUS_3* math.sin(a)
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=e["color"])
    canvas.after(10, animate, e1, e2,e3)

# Create electrons and start animation
electrons1 = create_electrons(NE, ORBIT_RADIUS_1)
electrons2 = create_electrons(NE, ORBIT_RADIUS_2)
electrons3 = create_electrons(NE, ORBIT_RADIUS_3)
animate(electrons1, electrons2,electrons3 )

# Start tkinter event loop
root.mainloop()

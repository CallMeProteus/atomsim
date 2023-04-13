import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
BOHRS_RADIUS = 0.52917721067e-10 # meters
Z = 1 # atomic number of hydrogen

'''number of runs, start with low numbers and increase gradually 
 Try up to 1million that what ive tested, hight than this, dont blame me'''
N = 10

''' Also nucleus is the red spot at the origin, the plot is in 3d bytheway'''


# Function to calculate the radial wave function
def R(r):
    return (2 / BOHRS_RADIUS)**(3/2) * math.exp(-Z*r/BOHRS_RADIUS) / math.sqrt(math.factorial(2*Z - 1)) * (2*Z*r/BOHRS_RADIUS)**(Z-1) * math.exp(-Z*r/(2*BOHRS_RADIUS)) * math.pow(r/BOHRS_RADIUS, 2*Z-2)

# Function to calculate the probability density
def probability_density(r, theta, phi):
    return R(r)**2 * r**2 * math.sin(theta)



# Arrays to store the sampled positions
r_samples = []
theta_samples = []
phi_samples = []

# Monte Carlo sampling
for i in range(N):
    r = random.uniform(0, 10*BOHRS_RADIUS) # Sample r from 0 to 10 times the Bohr radius
    theta = random.uniform(0, math.pi) # Sample theta from 0 to pi
    phi = random.uniform(0, 2*math.pi) # Sample phi from 0 to 2*pi
    r_samples.append(r)
    theta_samples.append(theta)
    phi_samples.append(phi)

# Calculate the probability density for each sampled position
prob_density = [probability_density(r_samples[i], theta_samples[i], phi_samples[i]) for i in range(N)]

# Create a 3D scatter plot of the sampled positions
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(r_samples, theta_samples, phi_samples, c=prob_density, cmap='viridis')
ax.scatter([0], [0], [0], s=100, marker='o', color='red') # Add nucleus as a red dot at the origin
ax.set_xlabel('r')
ax.set_ylabel('theta')
ax.set_zlabel('phi')
ax.set_title('Distribution of electron position')
plt.show()

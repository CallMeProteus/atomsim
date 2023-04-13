'''monte carlo position of electron position estimato'''
import random
import math
'''number of runs, start with low numbers and increase gradually 
 Try up to 1million that what ive tested, hight than this, dont blame me'''
N = 10 # number of runs, start with low numbers and increase gradually 

BOHRS_RADIUS = 0.52917721067e-10 #  meters, pick ur poison
Z = 1 # atomic number of hydrogen

# Function to calculate the radial wave function
def R(r):
    return (2 / BOHRS_RADIUS)**(3/2) * math.exp(-Z*r/BOHRS_RADIUS) / math.sqrt(math.factorial(2*Z - 1)) * (2*Z*r/BOHRS_RADIUS)**(Z-1) * math.exp(-Z*r/(2*BOHRS_RADIUS)) * math.pow(r/BOHRS_RADIUS, 2*Z-2)
# Function to calculate the probability density
def probability_density(r, theta, phi):
    return R(r)**2 * r**2 * math.sin(theta)







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

# Calculate the probability of finding the electron in a spherical shell between r and r + dr
dr = 0.1*BOHRS_RADIUS
prob = []
for r in range(int(10*BOHRS_RADIUS/dr)):
    r_min = r*dr
    r_max = (r+1)*dr
    vol_shell = 4*math.pi*(r_max**3 - r_min**3)/3
    prob_shell = sum([prob_density[i] for i in range(N) if r_min <= r_samples[i] <= r_max])
    prob.append(prob_shell / vol_shell)


for i in range(len(prob)):
    r_min = i*dr
    r_max = (i+1)*dr
    print(f"Probability of electron between {r_min/BOHRS_RADIUS} and {r_max/BOHRS_RADIUS} Bohr radii: {prob[i]}")

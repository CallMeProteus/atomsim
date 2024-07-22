![Screenshot](https://raw.githubusercontent.com/CallMeProteus/atomsim/main/Screenshot%20from%202024-07-17%2013-50-07.png)

# Hydrogen Atom Simulator

The Hydrogen Atom Simulator is a Python application that allows users to visualize and explore the behavior of a hydrogen atom. It includes a 2D animation of electrons orbiting the nucleus and a 3D plot of the probability density function of the electron's position.
Features
2D animation of electrons orbiting the nucleus
3D plot of the probability density function of the electron's position
Calculation of the probability of finding the electron within a specific radial distance from the nucleus

## Installation
Clone the repository:

```
git clone https://github.com/CallMeProteus/atomsim
```
Navigate to the project directory:

```
cd atomsim
```
Install the required dependencies:

```
pip install -r requirements.txt
```
Usage
Run the application:
```
python main.py
```
The application window will appear with three buttons: "Run 2D Simulation", "Run 3D Simulation", and "Calculate Probabilities".
Click on the "Run 2D Simulation" button to start the 2D animation of electrons orbiting the nucleus.
Click on the "Run 3D Simulation" button to generate a 3D plot of the probability density function of the electron's position.
Click on the "Calculate Probabilities" button to open a window displaying the probability of finding the electron within different radial distances from the nucleus.
Structure
The application is divided into the following modules:
main.py: The entry point of the application, where the Tkinter window is created and the HydrogenAtomSimulator class is instantiated.
hydrogen_atom_simulator.py: Contains the HydrogenAtomSimulator class, which handles the simulation and visualization logic. It creates instances of the ElectronSimulation and ProbabilityCalculation classes.
electron_simulation.py: Handles the 2D electron simulation and animation.
probability_calculation.py: Handles the 3D probability density calculation and visualization.
## Dependencies
```
Python 3.x
Tkinter
NumPy
Matplotlib
mpl_toolkits.mplot3d
matplotlib.backends.backend_tkagg
```

## Contributing
If you would like to contribute to the Hydrogen Atom Simulator, please follow these steps:
Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push your changes to your forked repository.
Submit a pull request to the original repository.
## License
This project is licensed under the MIT License.
### Acknowledgments
The Hydrogen Atom Simulator was inspired by the need to visualize and understand the behavior of a hydrogen atom.
The application uses various open-source libraries and tools to achieve its functionality.
Contact

If you have any questions or feedback, please feel free to contact the project maintainers jafethyahuma@gmail.com or callmeproteus@yahoo.com.

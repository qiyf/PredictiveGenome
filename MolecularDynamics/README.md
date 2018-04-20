## Molecular Dynamics Simulation with LAMMPS. 

Implementation of the potential energy funtion is provied in the src folder.  

## Installation

The LAMMPS package can be downloaded by running the following command:
```
git clone -b stable https://github.com/lammps/lammps.git
```
or with other links from the official site:

[http://lammps.sandia.gov/download.html](http://lammps.sandia.gov/download.html)

After download both of the packages, unpack both Predictive Genome Model and LAMMPS packages under the same directory. Then the modified potential files can be connected to the LAMMPS source code by executing the following command (rename the LAMMPS folder as `./lammps/` or change the name of the downloaded LAMMPS folder in the file `./PredictiveGenome/lammpsCode/src/connectLAMMPSPotential.sh`):
```
./PredictiveGenome/lammpsCode/src/connectLAMMPSPotential.sh
```
The corresponding potential files should be generated under `./lammps/src/`.

To compile the parallel version of LAMMPS, go to the folder `./lammps/src/`, and type the command:
```
make clean-all
make openmpi
```
To include the packages, type the command (e.g. class2 package):
```
make yes-class2
```
For more details, please refer to the instrucion on the official site:

[http://lammps.sandia.gov/doc/Section_start.html](http://lammps.sandia.gov/doc/Section_start.html).


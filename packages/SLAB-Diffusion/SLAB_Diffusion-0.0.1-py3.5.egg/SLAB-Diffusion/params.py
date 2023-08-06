path_outputs=''# you should add the path to the output directory here. Then type import params.py
v=1. #v=c/vd, see equation (7) of SOumagnac et al. 2018
h=10e15 #the size of the slab. Make sure it is larger than the characteristic size of the explosion.
E=1.0e51 #initial energy deposited in the slab
dillution_factor=200 #decrease this number to get more epochs
total_time=0.1 #total time of the simulation, in units of the diffusion time h^2/D
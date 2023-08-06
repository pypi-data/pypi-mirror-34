#
#The Defaultbparameters are those used in Soumagnac et al. 2018
path_outputs='./outputs'# you should add the path to the output directory here. Then type import params.py
v=1. #v=c/vd, see equation (7) of SOumagnac et al. 2018
h=10e15 #the size of the slab. Make sure it is larger than the characteristic size of the explosion.
E=1.0e51 #initial energy deposited in the slab
dillution_factor=50 #decrease this number to get more epochs. Increase to run quicker. Do not increase too much or you will get an error 'TypeError: iteration over a 0-d array'
total_time=1. #total duration of the simulation, in units of diffusion time h^2/D.

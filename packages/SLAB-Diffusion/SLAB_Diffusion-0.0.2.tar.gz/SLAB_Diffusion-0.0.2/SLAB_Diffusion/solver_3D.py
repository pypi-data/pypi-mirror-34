"""*******************************************************
contains solvers of the diffusion equation in 3D, with BB boundary conditions
*******************************************************"""
#print __doc__

import numpy as np
import pylab


def solver_3D_norm(Nx,Ny,Nz,Lx,Ly,Initial_xyz,F,v,a,total_time,reflecting=True,Ei=1.):#forward euler solver 1D
    """Description: solves the diffusion equation, in 3D, in a slab
    Input  :-
            -
            -
    Output :- u : 4D array with time, and the values of u in x,y,z
            - temp: 4D array with time, anf the values of T in x,y,z
            - spacex, spacey, spacez
            - time
            - FWHM: a time-long array with the value of the FWHM at the edge z=h
    Plots and data files:
        Plots:  - output_file+'/images2D/image_'+str(t).zfill(5)+'.png': at each time, a 2-panels plot with the (x,y) plane at z=h/2 and at z=h
                - output_file+'/edge_U/z0_' + str(t).zfill(5) + '.png': at each time, a plot of FWHM contour on the (x,y) plane at z=h
                - output_file + '/edge_FWHM.png': evolution with time of the FWHM surface diameter at z=h
    Tested : ?
         By : Maayane T. Soumagnac Jan 2018
        URL :
    Example:my_solver.solver_FE_1D_0boudaries(Nx,L=L,Initial_x=Initial_symetric,D=1,F=0.1,total_time=20,show_plots=False)
    and then
            my_solver.solver_FE_2D_raw_of_initials_along_x(Nx,Nz,L=L,h=h,Initial_x=Initial_symetric,D=1,F=0.2,total_time=20,show_plots=False)
    must give the same result.
    Reliable:  """
    space_x=np.linspace(0,Lx,num=Nx+1) # there are Nx cells, and Nx+1 points, witht the fist one 0, the last one L
    space_y = np.linspace(0, Ly, num=Ny + 1)
    space_z=np.linspace(0,1,num=Nz+1)
    delta_x=space_x[1]-space_x[0]
    delta_y = space_y[1] - space_y[0]
    delta_z=space_z[1]-space_z[0]
    print('delta_x/h is {0}'.format(delta_x))
    print('delta_y/h is {0}'.format(delta_y))
    print('delta_z/h is {0}'.format(delta_z))
    delta_t=F/((1/delta_x**2)+(1/delta_y**2)+(1/delta_z**2))
    print('delta_t/td is {0}'.format(delta_t))
    F_1Dx =delta_t/delta_x**2
    F_1Dy =delta_t / delta_y ** 2
    F_1Dz=delta_t/delta_z**2
    print('The equivalent 1-d F along x axis, F=D*delta_t/delta_x**2={0}'.format(F_1Dx))
    print('The equivalent 1-d F along y axis, F=D*delta_t/delta_z**2={0}'.format(F_1Dy))
    print('The equivalent 1-d F along z axis, F=D*delta_t/delta_z**2={0}'.format(F_1Dz))
    #pdb.set_trace()
    Nt=int(round(total_time/float(delta_t)))
    print('given the total time,F and L, I have {0} time meshpoints'.format(Nt))
    print('the coefficient (c/vdiff)*(deltat/(4*deltaz)) at the boundary is {0}'.format(v/a*(delta_t/delta_z)))
    #pdb.set_trace()
    time=np.linspace(0,total_time,num=Nt+1)
    #print time[:-1]
    #print time[:-1]/(24*3600)
    #pdb.set_trace()
    u = np.zeros((Nt + 1, Nx + 1, Ny+1,Nz+1))
    u_notnorm = np.zeros((Nt + 1, Nx + 1, Ny + 1, Nz + 1))
    temp=np.zeros((Nt + 1, Nx + 1, Ny+1,Nz+1))
    #a = 4 * StefanBoltzmann / c
    print(np.shape(space_x))
    print(np.shape(space_y))
    print(np.shape(space_z))
    #TEST

    ########  Sets Initial_xyz(space_x, space_z) ##########
    print(np.shape(Initial_xyz(space_x, space_y, space_z)))  # z, x, y

    #print np.shape(Initial_xyz(space_x,space_z,space_y)) #z, x, y
    #if normalization_xyz!=None:
        #norma=normalization_xyz(space_x,space_y,space_z)
    norma=np.sum(Initial_xyz(space_x, space_y, space_z))*(delta_x*delta_y*delta_z)/Ei#*delta_t
    #print 'the initial amount of energy in the box, before normalization, is',norma
    #else:
    #    norma=1.
    u[0, :, :, :] = Initial_xyz(space_x, space_y, space_z)/norma#/norma#(0.20053026197)#**1./3.#/norma
    print('check: after normalization, the initioal amount of energy in the box is {0}'.format(np.sum(u[0, :, :, :])*delta_x*delta_y*delta_z))
    #print(int(Nz))
    #print('Nz/2 is', int(Nz/2))
    pylab.matshow(u[0,:,:,int(Nz/2)].T)
    pylab.xlabel('x axis')
    pylab.ylabel('y axis')
    pylab.title('Initial condition, centre of the slab',y=1.08)#z=0
    pylab.colorbar()
    #pylab.show()
    #pdb.set_trace()
    #print np.shape(norma)
    #pdb.set_trace()
    coeff_boundary=v/a*(delta_t/delta_z)
    #coeff_boundary=c*delta_t/(4*delta_z)
    print('the multiplicative factor playing the role of F at the boundary is {0}'.format(coeff_boundary))

    #print 'I am setting absorbing conditions at the edges'
    #u[:,0,:,:]=0.
    #u[:,Nx,:,:]=0.
    #u[:, :,0, :] = 0.
    #u[:, :,Ny, :] = 0.

    ########  Solves ##########

    for t,s in enumerate(time[:-1]):
        print('I am looking at the time meshpoint #{0}, i.e. t/tD={1}'.format(t, s))
        u[t + 1, 1:-1,1:-1,1:-1] = u[t, 1:-1, 1:-1,1:-1] +F_1Dx*(-2*u[t, 1:-1, 1:-1,1:-1]+u[t, 2:, 1:-1,1:-1] + u[t, :-2, 1:-1,1:-1]) \
                                    + F_1Dy*(u[t, 1:-1, 2:,1:-1] + u[t, 1:-1, :-2,1:-1]-2*u[t, 1:-1, 1:-1,1:-1])\
                                    +F_1Dz*(u[t, 1:-1,1:-1, 2:] + u[t, 1:-1,1:-1,:-2]-2*u[t, 1:-1, 1:-1,1:-1])
        #BB boundary conditions along z
        u[t + 1, 1:-1,1:-1,0] = (u[t, 1:-1,1:-1,0] + F_1Dz * (u[t, 1:-1,1:-1,1] - u[t, 1:-1,1:-1,0]) - coeff_boundary * u[t, 1:-1,1:-1,0])
        u[t + 1, 1:-1,1:-1,Nz] = (u[t, 1:-1,1:-1,Nz] - F_1Dz * (u[t, 1:-1,1:-1,Nz] - u[t, 1:-1,1:-1,Nz - 1]) - coeff_boundary * u[t,1:-1,1:-1, Nz])
        if reflecting==True:
            #Reflecting boundary conditions for x and y
            u[t + 1, 1:-1,0,1:-1] = u[t, 1:-1,0,1:-1] + F_1Dy * (u[t, 1:-1,1,1:-1] - u[t, 1:-1,0,1:-1])
            u[t + 1, 1:-1,Ny,1:-1] = u[t, 1:-1,Ny,1:-1] - F_1Dy * (u[t, 1:-1,Ny,1:-1] - u[t, 1:-1,Ny - 1,1:-1])
            u[t + 1, 0,1:-1,1:-1] = u[t,0, 1:-1,1:-1] + F_1Dx * (u[t, 1,1:-1,1:-1] - u[t, 0,1:-1,1:-1])
            u[t + 1, Nx,1:-1,1:-1] = u[t,Nx, 1:-1,1:-1] - F_1Dx * (u[t, Nx,1:-1,1:-1] - u[t, Nx-1,1:-1,1:-1])
        else:
            u[t + 1, 1:-1, 0, 1:-1] = 0.
            u[t + 1, 1:-1, Ny, 1:-1] = 0.
            u[t + 1, 0, 1:-1, 1:-1] = 0.
            u[t + 1, Nx, 1:-1, 1:-1] = 0.

    print('returning')
    #print 'I am checking that the energy is conserved. '
    #print 'The amount of energy in the grid at the end is {0}'.format(np.sum(u[-1,:,:,:]))
    #print 'And the integrated energy at the end {0}'.format(np.trapz(u[:,:,:,-1],time))
    #print 'And the amount of energy released is 2*{0}'.format(np.sum(u[:-1,:,:,-1]))
    return u,space_x,space_y,space_z,time#,FWHM



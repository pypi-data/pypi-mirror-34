
"""*******************************************************
contains solvers of the diffusion equation in 3D, with BB boundary conditions
*******************************************************"""
#print __doc__



import numpy as np
import pylab
import FWHM_calc


def plot_cuts_2D_u(u,space_z,time,time_Units=None,output_file='.',dilution_factor=None,show_plots=False):#Nx,Ny,Nz,Lx,Ly,h,Initial_xyz,D,F,c,StefanBoltzmann,total_time,show_plots=False,savefigs_3D=False,savefigs_boundary=False,factor=None,time_Units=None,dist_Units=None,dilution_factor=None):#forward euler solver 1D
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

    print('************ I am plotting 2D cuts of the energy density *******************')
    #space_x=np.linspace(0,Lx,num=Nx+1) # there are Nx cells, and Nx+1 points, witht the fist one 0, the last one L
    #space_y = np.linspace(0, Ly, num=Ny + 1)
    #space_z=np.linspace(0,h,num=Nz+1)
    '''
        delta_x=space_x[1]-space_x[0]
        delta_y = space_y[1] - space_y[0]
        delta_z=space_z[1]-space_z[0]
        print 'delta_x is {0} cm'.format(delta_x)
        print 'delta_y is {0} cm'.format(delta_y)
        print 'delta_z is {0} cm'.format(delta_z)
        delta_t=F/((D/delta_x**2)+(D/delta_y**2)+(D/delta_z**2))
        print 'delta_t is {0} s, i.e. {1} days'.format(delta_t,delta_t/(3600*24))
        F_1Dx =D*delta_t/delta_x**2
        F_1Dy = D * delta_t / delta_y ** 2
        F_1Dz= D*delta_t/delta_z**2
        print 'The equivalent 1-d F along x axis, F=D*delta_t/delta_x**2={0}'.format(F_1Dx)
        print 'The equivalent 1-d F along y axis, F=D*delta_t/delta_z**2={0}'.format(F_1Dy)
        print 'The equivalent 1-d F along z axis, F=D*delta_t/delta_z**2={0}'.format(F_1Dz)
        #pdb.set_trace()
        Nt=int(round(total_time/float(delta_t)))
        print 'given the total time,F and L, I have {0} time meshpoints'.format(Nt)
        #print 'the coefficient c*deltat/(4*deltaz) at the boundary is {0}'.format(c*delta_t/(4*delta_z))
        #pdb.set_trace()
        time=np.linspace(0,total_time,num=Nt+1)
        '''
    Nt=np.shape(time)[0]-1
    Nz=np.shape(space_z)[0]-1
    '''
    #print time[:-1]
    #print time[:-1]/(24*3600)
    #pdb.set_trace()
    u = np.zeros((Nt + 1, Nx + 1, Ny+1,Nz+1))
    temp=np.zeros((Nt + 1, Nx + 1, Ny+1,Nz+1))
    a = 4 * StefanBoltzmann / c
    print np.shape(space_x)
    print np.shape(space_y)
    print np.shape(space_z)
    #TEST
    u_analytic = np.zeros((Nt + 1, Nx + 1, Ny + 1, Nz + 1))
    print np.shape(u_analytic)
    for t, s in enumerate(time[:-1]):
        print t,s
        #print 1. / (s*math.sqrt(s))
        for i_x,x in enumerate(space_x):
            for i_y, y in enumerate(space_y):
                u_analytic[t, i_x, i_y, :] = 1. / (s*math.sqrt(s))*np.exp(-(np.power(x-Lx/2,2)+np.power(y-Ly/2,2)+np.power(space_z[:]-h/2,2))/(4*D*s))

    ########  Sets Initial_xyz(space_x, space_z) ##########
    print np.shape(Initial_xyz(space_x,space_z,space_y)) #z, x, y
    u[0,:,:,:]=u_analytic[1,:,:,:]#Initial_xyz(space_x,space_z,space_y)
    u[:,0,:,:]=0.
    u[:,Nx,:,:]=0.
    u[:, :,0, :] = 0.
    u[:, :,Ny, :] = 0.
    #COMMENT WHEN NOT CHECKING ANALYTIC
    u[:, :,:, 0] = 0.
    u[:, :,:, Nz] = 0.
    #checks
    temp[0,:,:,:] = np.power(1. / a * u[0,:,:,:] * factor, 0.25)
    pylab.matshow(u[0,:,:,Nz/2].T)
    pylab.xlabel('x axis')
    pylab.ylabel('y axis')
    pylab.title('Initial condition, at z=h/2')
    pylab.colorbar()
    pylab.show()
    #pdb.set_trace()
    coeff_boundary=c*delta_t/(4*delta_z)
    print 'the multiplicative factor playing the role of F at the boundary is {0}'.format(coeff_boundary)

    ########  Solves ##########
    for t,s in enumerate(time[:-1]):
        print 'I am looking at the time meshpoint #{0}, i.e. t={1}'.format(t, s)
        u[t + 1, 1:-1,1:-1,1:-1] = u[t, 1:-1, 1:-1,1:-1] +F_1Dx*(-2*u[t, 1:-1, 1:-1,1:-1]+u[t, 2:, 1:-1,1:-1] + u[t, :-2, 1:-1,1:-1]) \
                                    + F_1Dy*(u[t, 1:-1, 2:,1:-1] + u[t, 1:-1, :-2,1:-1]-2*u[t, 1:-1, 1:-1,1:-1])\
                                    +F_1Dz*(u[t, 1:-1,1:-1, 2:] + u[t, 1:-1,1:-1,:-2]-2*u[t, 1:-1, 1:-1,1:-1])
        #PUT BACK WHEN NOT COMPARING TO ANALYTIC
        #u[t + 1, 1:-1,1:-1,0] = u[t, 1:-1,1:-1,0] + F_1Dz * (u[t, 1:-1,1:-1,1] - u[t, 1:-1,1:-1,0]) - coeff_boundary * u[t, 1:-1,1:-1,0]
        #u[t + 1, 1:-1,1:-1,Nz] = u[t, 1:-1,1:-1,Nz] - F_1Dz * (u[t, 1:-1,1:-1,Nz] - u[t, 1:-1,1:-1,Nz - 1]) - coeff_boundary * u[t,1:-1,1:-1, Nz]
        #temp[t+1,:,:,:] = np.power(1. / a * u[t+1,:,:,:] * factor, 0.25)

    '''
    ######### Plots the 2D cuts at diluted times to make a video of u and the temperature ############

    if dilution_factor != None:
        print('I am diluting time by {0}'.format(dilution_factor))
        time_diluted = time[::dilution_factor]
        index_dilute=range(Nt+1)[::dilution_factor]
        print(np.shape(time_diluted))
        print(np.shape(index_dilute))
        #pdb.set_trace()
    if dilution_factor != None:
        for t, s in enumerate(time_diluted):
            if time_Units=='s':
                print('I am looking at index {0} i.e. time t={1} days'.format(index_dilute[t], s/(3600*24)))
            elif time_Units=='tD':
                print('I am looking at index {0} i.e. time t/tD={1}'.format(index_dilute[t], s))

            ###### plots, at each time, the (x,y) plane at z=h/2 and at z=h

            fig = pylab.figure(figsize=(10, 5))
            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)
            im0=ax1.matshow(u[int(index_dilute[t]),:,:,Nz/2].T,cmap=pylab.get_cmap('hot'),vmin=0, vmax=2*np.max(u[-1, :, :, :]))#vmin=0,vmax=0.001)
            im1=ax2.matshow(u[int(index_dilute[t]), :, :, Nz].T,cmap=pylab.get_cmap('hot'),vmin=0, vmax=2*np.max(u[-1, :, :, :]))#vmax=0.001)
            if time_Units=='s':
                ax1.set_title('t={0} days, z=h/2'.format(round(s/(3600*24), 3)))
                ax2.set_title('t={0} days, z=h'.format(round(s/(3600*24),3)))
            elif time_Units=='tD':
                ax1.set_title('t/tD={0}, z=h/2'.format(round(s, 3)))
                ax2.set_title('t/tD={0}, z=h'.format(round(s,3)))
            pylab.subplots_adjust(wspace=0.33)
            ax1.set_xlabel('x direction (meshpoint index)')
            ax2.set_xlabel('x direction (meshpoint index)')
            ax1.set_ylabel('y direction (meshpoint index)')
            fig.subplots_adjust(right=0.8)
            cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
            fig.colorbar(im0, cax=cbar_ax)
            pylab.savefig(output_file+'/images2D/image_'+str(t).zfill(5)+'.png', bbox_inches='tight')
            #pylab.show()
            #pdb.set_trace()
        '''
            ######### Plots the 2D cuts at diluted times to make a video of the temperature ############

            fig = pylab.figure(figsize=(10, 5))
            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)
            im0=ax1.matshow(temp[int(index_dilute[t]),:,:,Nz/2].T,vmin=0,vmax=40000)
            im1=ax2.matshow(temp[int(index_dilute[t]), :, :, Nz].T,vmin=0,vmax=40000)
            if time_Units=='days':
                ax1.set_title('t={0} days, z=h/2'.format(round(s/(3600*24), 3)))
                ax2.set_title('t={0} days, z=h'.format(round(s/(3600*24),3)))
            else:
                ax1.set_title('t={0} days, z=h/2'.format(round(s, 3)))
                ax2.set_title('t={0} days, z=h'.format(round(s,3)))
            pylab.subplots_adjust(wspace=0.33)
            ax1.set_xlabel('x direction (meshpoint index)')
            ax2.set_xlabel('x direction (meshpoint index)')
            ax1.set_ylabel('y direction (meshpoint index)')
            fig.subplots_adjust(right=0.8)
            cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
            fig.colorbar(im0, cax=cbar_ax)
            pylab.savefig(output_file+'/images2D_temp/image_'+str(t).zfill(5)+'.png', bbox_inches='tight')
            #pylab.show()
            #pdb.set_trace()
        '''
    else:
        for t, s in enumerate(time[:-1]):
            if time_Units=='s':
                print('I am looking at the time t={1} days'.format(t, s/(3600*24)))
            elif time_Units=='tD':
                print('I am looking at the time t/tD={1}'.format(t, s))
            ###### plots, at each time, the (x,y) plane at z=h/2 and at z=h
            fig = pylab.figure(figsize=(10, 5))
            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)
            im0=ax1.matshow(u[t,:,:,Nz/2].T,cmap=pylab.get_cmap('hot'),vmin=0,vmax=0.001)
            im1=ax2.matshow(u[t,:,:, Nz].T,cmap=pylab.get_cmap('hot'),vmin=0,vmax=0.001)
            if time_Units=='days':
                ax1.set_title('t={0} days, z=h/2'.format(round(s/(3600*24), 3)))
                ax2.set_title('t={0} days, z=h'.format(round(s/(3600*24),3)))
            else:
                ax1.set_title('t={0} days, z=h/2'.format(round(s, 3)))
                ax2.set_title('t={0} days, z=h'.format(round(s,3)))
            pylab.subplots_adjust(wspace=0.33)
            ax1.set_xlabel('x direction (meshpoint index)')
            ax2.set_xlabel('x direction (meshpoint index)')
            ax1.set_ylabel('y direction (meshpoint index)')
            fig.subplots_adjust(right=0.8)
            cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
            fig.colorbar(im0, cax=cbar_ax)
            pylab.savefig(output_file+'/images2D/image_'+str(t).zfill(5)+'.png', bbox_inches='tight')
            #pylab.show()
            #pdb.set_trace()
    if show_plots ==True:
        pylab.show()

def plot_u_latest_time(u,spacez,time,time_Units=None,output_file='.',show_plots=False):#Nx,Ny,Nz,Lx,Ly,h,Initial_xyz,D,F,c,StefanBoltzmann,total_time,show_plots=False,savefigs_3D=False,savefigs_boundary=False,factor=None,time_Units=None,dist_Units=None,dilution_factor=None):#forward euler solver 1D
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
    print('************ I am plotting the energy density at the latest time *******************')

    Nz=int(np.shape(spacez)[0]-1)
    #print(Nz/2)
    print('Nz is',Nz)

    ###### Plots u at latest time, at z=h/2 and at z=h)

    fig = pylab.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    im0 = ax1.matshow(u[-1, :, :, int(Nz / 2)].T, cmap=pylab.get_cmap('hot'), vmin=0, vmax=np.max(u[-1, :, :, int(Nz / 2)]))
    im1=ax2.matshow(u[-1, :, :, int(Nz)].T,cmap=pylab.get_cmap('hot'),vmin=0,vmax=np.max(u[-1, :, :, int(Nz / 2)]))
    #im0=ax1.matshow(u[-1,:,:,Nz/2].T,cmap=pylab.get_cmap('hot'),vmin=0,vmax=0.002)
    #im1=ax2.matshow(u[-1, :, :, Nz].T,cmap=pylab.get_cmap('hot'),vmin=0,vmax=0.002)
    if time_Units == 's':
        ax1.set_title('t={0} days, z=h/2'.format(round(time[-1]/(24*3600), 3)))
        ax2.set_title('t={0} days, z=h'.format(round(time[-1]/(24*3600),3)))
    elif time_Units=='tD':
        ax1.set_title('t/tD={0}, z=h/2'.format(round(time[-1], 3)))
        ax2.set_title('t/tD={0}, z=h'.format(round(time[-1],3)))
    pylab.subplots_adjust(wspace=0.33)
    ax1.set_xlabel('x direction (meshpoint index)')
    ax2.set_xlabel('x direction (meshpoint index)')
    ax1.set_ylabel('y direction (meshpoint index)')
    fig.subplots_adjust(right=0.8)
    cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    fig.colorbar(im0, cax=cbar_ax)
    pylab.savefig(output_file+'/images2D/image_'+str(time[-1]).zfill(5)+'.png', bbox_inches='tight')
    if show_plots==True:
        pylab.show()

def plot_cuts_2D_temp(temp,space_z,time,time_Units=None,output_file='.',dilution_factor=None,show_plots=False):#Nx,Ny,Nz,Lx,Ly,h,D,F,total_time,time_Units=None,output_file='.',dilution_factor=None,show_plots=False):#Nx,Ny,Nz,Lx,Ly,h,Initial_xyz,D,F,c,StefanBoltzmann,total_time,show_plots=False,savefigs_3D=False,savefigs_boundary=False,factor=None,time_Units=None,dist_Units=None,dilution_factor=None):#forward euler solver 1D
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
    print('************ I am plotting 2D cuts of the temperature *******************')
    '''
    space_x=np.linspace(0,Lx,num=Nx+1) # there are Nx cells, and Nx+1 points, witht the fist one 0, the last one L
    space_y = np.linspace(0, Ly, num=Ny + 1)
    space_z=np.linspace(0,h,num=Nz+1)
    delta_x=space_x[1]-space_x[0]
    delta_y = space_y[1] - space_y[0]
    delta_z=space_z[1]-space_z[0]
    print 'delta_x is {0} cm'.format(delta_x)
    print 'delta_y is {0} cm'.format(delta_y)
    print 'delta_z is {0} cm'.format(delta_z)
    delta_t=F/((D/delta_x**2)+(D/delta_y**2)+(D/delta_z**2))
    print 'delta_t is {0} s, i.e. {1} days'.format(delta_t,delta_t/(3600*24))
    F_1Dx =D*delta_t/delta_x**2
    F_1Dy = D * delta_t / delta_y ** 2
    F_1Dz= D*delta_t/delta_z**2
    print 'The equivalent 1-d F along x axis, F=D*delta_t/delta_x**2={0}'.format(F_1Dx)
    print 'The equivalent 1-d F along y axis, F=D*delta_t/delta_z**2={0}'.format(F_1Dy)
    print 'The equivalent 1-d F along z axis, F=D*delta_t/delta_z**2={0}'.format(F_1Dz)
    #pdb.set_trace()
    '''
    '''
    #print time[:-1]
    #print time[:-1]/(24*3600)
    #pdb.set_trace()
    u = np.zeros((Nt + 1, Nx + 1, Ny+1,Nz+1))
    temp=np.zeros((Nt + 1, Nx + 1, Ny+1,Nz+1))
    a = 4 * StefanBoltzmann / c
    print np.shape(space_x)
    print np.shape(space_y)
    print np.shape(space_z)
    #TEST
    u_analytic = np.zeros((Nt + 1, Nx + 1, Ny + 1, Nz + 1))
    print np.shape(u_analytic)
    for t, s in enumerate(time[:-1]):
        print t,s
        #print 1. / (s*math.sqrt(s))
        for i_x,x in enumerate(space_x):
            for i_y, y in enumerate(space_y):
                u_analytic[t, i_x, i_y, :] = 1. / (s*math.sqrt(s))*np.exp(-(np.power(x-Lx/2,2)+np.power(y-Ly/2,2)+np.power(space_z[:]-h/2,2))/(4*D*s))

    ########  Sets Initial_xyz(space_x, space_z) ##########
    print np.shape(Initial_xyz(space_x,space_z,space_y)) #z, x, y
    u[0,:,:,:]=u_analytic[1,:,:,:]#Initial_xyz(space_x,space_z,space_y)
    u[:,0,:,:]=0.
    u[:,Nx,:,:]=0.
    u[:, :,0, :] = 0.
    u[:, :,Ny, :] = 0.
    #COMMENT WHEN NOT CHECKING ANALYTIC
    u[:, :,:, 0] = 0.
    u[:, :,:, Nz] = 0.
    #checks
    temp[0,:,:,:] = np.power(1. / a * u[0,:,:,:] * factor, 0.25)
    pylab.matshow(u[0,:,:,Nz/2].T)
    pylab.xlabel('x axis')
    pylab.ylabel('y axis')
    pylab.title('Initial condition, at z=h/2')
    pylab.colorbar()
    pylab.show()
    #pdb.set_trace()
    coeff_boundary=c*delta_t/(4*delta_z)
    print 'the multiplicative factor playing the role of F at the boundary is {0}'.format(coeff_boundary)

    ########  Solves ##########
    for t,s in enumerate(time[:-1]):
        print 'I am looking at the time meshpoint #{0}, i.e. t={1}'.format(t, s)
        u[t + 1, 1:-1,1:-1,1:-1] = u[t, 1:-1, 1:-1,1:-1] +F_1Dx*(-2*u[t, 1:-1, 1:-1,1:-1]+u[t, 2:, 1:-1,1:-1] + u[t, :-2, 1:-1,1:-1]) \
                                    + F_1Dy*(u[t, 1:-1, 2:,1:-1] + u[t, 1:-1, :-2,1:-1]-2*u[t, 1:-1, 1:-1,1:-1])\
                                    +F_1Dz*(u[t, 1:-1,1:-1, 2:] + u[t, 1:-1,1:-1,:-2]-2*u[t, 1:-1, 1:-1,1:-1])
        #PUT BACK WHEN NOT COMPARING TO ANALYTIC
        #u[t + 1, 1:-1,1:-1,0] = u[t, 1:-1,1:-1,0] + F_1Dz * (u[t, 1:-1,1:-1,1] - u[t, 1:-1,1:-1,0]) - coeff_boundary * u[t, 1:-1,1:-1,0]
        #u[t + 1, 1:-1,1:-1,Nz] = u[t, 1:-1,1:-1,Nz] - F_1Dz * (u[t, 1:-1,1:-1,Nz] - u[t, 1:-1,1:-1,Nz - 1]) - coeff_boundary * u[t,1:-1,1:-1, Nz]
        #temp[t+1,:,:,:] = np.power(1. / a * u[t+1,:,:,:] * factor, 0.25)

    '''
    Nt=np.shape(time)[0]-1
    Nz=np.shape(space_z)[0]-1
    ######### Plots the 2D cuts at diluted times to make a video of u and the temperature ############

    if dilution_factor != None:
        print('I am diluting time by {0}'.format(dilution_factor))
        time_diluted = time[::dilution_factor]
        index_dilute=range(Nt+1)[::dilution_factor]
    if dilution_factor != None:
        for t, s in enumerate(time_diluted):
            if time_Units == 's':
                print('I am looking at the time t={1} days'.format(t, s/(3600*24)))
            elif time_Units=='td':
                print('I am looking at the time t/td={1}'.format(t, s))

            ###### plots, at each time, the (x,y) plane at z=h/2 and at z=h

            fig = pylab.figure(figsize=(10, 5))
            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)
            im0=ax1.matshow(temp[int(index_dilute[t]),:,:,Nz/2].T,vmin=0,vmax=np.max(temp[-1, :, :, Nz / 2]))
            im1=ax2.matshow(temp[int(index_dilute[t]), :, :, Nz].T,vmin=0,vmax=np.max(temp[-1, :, :, Nz / 2]))
            if time_Units=='s':
                ax1.set_title('t={0} days, z=h/2'.format(round(s/(3600*24), 3)))
                ax2.set_title('t={0} days, z=h'.format(round(s/(3600*24),3)))
            elif time_Units=='td':
                ax1.set_title('t/td={0}, z=h/2'.format(round(s, 3)))
                ax2.set_title('t/td={0}, z=h'.format(round(s,3)))
            pylab.subplots_adjust(wspace=0.33)
            ax1.set_xlabel('x direction (meshpoint index)')
            ax2.set_xlabel('x direction (meshpoint index)')
            ax1.set_ylabel('y direction (meshpoint index)')
            fig.subplots_adjust(right=0.8)
            cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
            fig.colorbar(im0, cax=cbar_ax)
            pylab.savefig(output_file+'/images2D_temp/image_'+str(t).zfill(5)+'.png', bbox_inches='tight')
            #pylab.show()
            #pdb.set_trace()
    else:
        for t, s in enumerate(time[:-1]):
            print('I am looking at the time t={1} days'.format(t, s/(3600*24)))
            ###### plots, at each time, the (x,y) plane at z=h/2 and at z=h
            fig = pylab.figure(figsize=(10, 5))
            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)
            im0=ax1.matshow(temp[t,:,:,Nz/2].T,vmin=0,vmax=np.max(temp[-1, :, :, Nz / 2]))
            im1=ax2.matshow(temp[t,:,:, Nz].T,vmin=0,vmax=np.max(temp[-1, :, :, Nz / 2]))
            if time_Units=='days':
                ax1.set_title('t={0} days, z=h/2'.format(round(s/(3600*24), 3)))
                ax2.set_title('t={0} days, z=h'.format(round(s/(3600*24),3)))
            else:
                ax1.set_title('t={0} days, z=h/2'.format(round(s, 3)))
                ax2.set_title('t={0} days, z=h'.format(round(s,3)))
            pylab.subplots_adjust(wspace=0.33)
            ax1.set_xlabel('x direction (meshpoint index)')
            ax2.set_xlabel('x direction (meshpoint index)')
            ax1.set_ylabel('y direction (meshpoint index)')
            fig.subplots_adjust(right=0.8)
            cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
            fig.colorbar(im0, cax=cbar_ax)
            pylab.savefig(output_file+'/images2D_temp/image_'+str(t).zfill(5)+'.png', bbox_inches='tight')
    if show_plots==True:
        pylab.show()

def plot_temp_latest_time(temp,spacez,time,time_Units=None,output_file='.',show_plots=False):#Nx,Ny,Nz,Lx,Ly,h,Initial_xyz,D,F,c,StefanBoltzmann,total_time,show_plots=False,savefigs_3D=False,savefigs_boundary=False,factor=None,time_Units=None,dist_Units=None,dilution_factor=None):#forward euler solver 1D
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
    print('************ I am plotting the temperature at the latest time *******************')
    Nz = np.shape(spacez)[0] - 1

    ###### Plots temp at latest time, at z=h/2 and at z=h)

    fig = pylab.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    im0 = ax1.matshow(temp[-1, :, :, Nz / 2].T, vmin=0, vmax=np.max(temp[-1, :, :, Nz / 2]))
    im1 = ax2.matshow(temp[-1, :, :, Nz].T, vmin=0, vmax=np.max(temp[-1, :, :, Nz / 2]))
    # im0=ax1.matshow(u[-1,:,:,Nz/2].T,cmap=pylab.get_cmap('hot'),vmin=0,vmax=0.002)
    # im1=ax2.matshow(u[-1, :, :, Nz].T,cmap=pylab.get_cmap('hot'),vmin=0,vmax=0.002)
    if time_Units == 'days':
        ax1.set_title('t={0} days, z=h/2'.format(round(time[-1] / (24 * 3600), 3)))
        ax2.set_title('t={0} days, z=h'.format(round(time[-1] / (24 * 3600), 3)))
    else:
        ax1.set_title('t={0}, z=h/2'.format(round(time[-1], 3)))
        ax2.set_title('t={0}, z=h'.format(round(time[-1], 3)))
    pylab.subplots_adjust(wspace=0.33)
    ax1.set_xlabel('x direction (meshpoint index)')
    ax2.set_xlabel('x direction (meshpoint index)')
    ax1.set_ylabel('y direction (meshpoint index)')
    fig.subplots_adjust(right=0.8)
    cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    fig.colorbar(im0, cax=cbar_ax)
    pylab.savefig(output_file + '/images2D_temp/image_' + str(time[-1]).zfill(5) + '.png', bbox_inches='tight')
    if show_plots == True:
        pylab.show()

def calc_and_plot_contour_FWHM(u,space_x,space_y,space_z,time,time_Units=None,output_file='.',dist_Units=None,dilution_factor=None,plot=True):
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
    print('************ I am the contours of teh energy density FWHM *******************')

    ###### plots the contour of FWHM at the edge (z=h), calculate the diameter of the FWHM surface and plots its evolution
    Nx=np.shape(space_x)[0]-1
    Nz = np.shape(space_z)[0] - 1
    Nt = np.shape(time)[0] - 1
    delta_x=space_x[1]-space_x[0]

    r1=np.zeros(np.shape(time)[0]-1)
    r2=np.zeros(np.shape(time)[0]-1)
    FWHM=np.zeros(np.shape(time)[0]-1)
    half_peak_2D_U = np.zeros(np.shape(time)[0] - 1)
    half_peak_1D_U=np.zeros(np.shape(time)[0] - 1)
    for t, s in enumerate(time[:-1]):
        print('I am looking at the time-meshpoint #{0}, i.e. t={1}'.format(t, s))
        half_peak_2D_U[t]=0.5*np.max(u[t,:,:,-1])
        half_peak_1D_U[t], r1[t], r2[t] = FWHM_calc.FWHM_calc(space_x, u[t,round(Nx/2),:, 0], show_plot=False)
        FWHM[t] = r2[t] - r1[t]
    if plot==True:
        if dilution_factor == None:
            for t, s in enumerate(time[:-1]):
                if time_Units=='tD':
                    print('I am looking at t/tD={0}'.format(s))
                pylab.figure()
                pylab.contour(space_x,space_y,u[t, :, :, Nz].T,[half_peak_2D_U[t],2*half_peak_2D_U[t]])
                #print FWHM[t]
                pylab.hlines(np.max(space_y)/2,xmin=np.max(space_y)/2-FWHM[t]/2, xmax=np.max(space_y)/2+FWHM[t]/2,color='red')
                pylab.xlabel('x direction (meshpoint index)')
                pylab.ylabel('y direction (meshpoint index)')
                pylab.title('Contour of FWHM(u) at z=h')
                pylab.savefig(output_file+'/edge_U/z0_' + str(t).zfill(5) + '.png', bbox_inches='tight')
        else:
            print('I am diluting time by {0}'.format(dilution_factor))
            time_diluted = time[::dilution_factor]
            index_dilute = range(Nt)[::dilution_factor]
            for t, s in enumerate(time_diluted):
                if time_Units=='tD':
                    print('I am looking at t/tD={0}'.format(s))
                elif time_Units=='s':
                    print('I am looking at t={0} days'.format(s/(3600*24)))
                pylab.figure()
                pylab.contour(space_x,space_y,u[int(index_dilute[t]), :, :, Nz].T,[half_peak_2D_U[int(index_dilute[t])],2*half_peak_2D_U[int(index_dilute[t])]])
                #print FWHM[int(index_dilute[t])]
                pylab.hlines(np.max(space_y)/2,xmin=np.max(space_y)/2-FWHM[int(index_dilute[t])]/2, xmax=np.max(space_y)/2+FWHM[int(index_dilute[t])]/2,color='red')
                pylab.xlabel('x direction (meshpoint index)')
                pylab.ylabel('y direction (meshpoint index)')
                pylab.title('Contour of FWHM(u) at z=h')
                pylab.savefig(output_file+'/edge_U/z0_' + str(t).zfill(5) + '.png', bbox_inches='tight')

    #FWHM[:]=FWHM[:]*delta_x
    pylab.figure()
    if time_Units == 's':
        #time[:-1]=time[:-1]/(24*3600)
        pylab.xlabel('time [days]')
    elif time_Units=='tD':
        pylab.xlabel(r'$t/t_D$')
        pylab.plot(time[:-1], FWHM, 'b-')
    if time_Units=='s':
        pylab.plot(time[:-1]/(3600*24),FWHM,'b-')
    if dist_Units=='cm':
        #FWHM[:]=FWHM[:]*delta_x
        pylab.ylabel(r'$FWHM\;[cm]$')
    else:
        pylab.ylabel(r'$FWHM/h$')
    #pylab.title('FWHM at the edge')
    pylab.grid()
    pylab.savefig(output_file+'/edge_FWHM.png', bbox_inches='tight')
    pylab.savefig(output_file + '/edge_FWHM.png', bbox_inches='tight')

    np.savetxt(output_file + '/FWHM.txt', list(zip(time, FWHM)))
    #if time_Units == 'days':
        #time[:-1]=time[:-1]*(24*3600)#brings it back
    return time,FWHM
    #pylab.show()


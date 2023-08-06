
"""*******************************************************
SLAB-Diffusion: solves diffusion equation, for a constant density profile.
Calculates the evolution in time of T and R.
Make a figure like Figure 11 of Soumagnac et al 2018
******************************************************"""
print(__doc__)


import numpy as np
import pylab
import os
import logging
import pdb
import matplotlib.pyplot as plt
import math
from . import solver_3D
from . import black_body_flux_density
from . import fit_black_body_flux_spec
from . import distances_conversions
from . import plotter_3D
from . import params
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

__all__=['calculate_T_and_R_in_time']

#print(params.dillution_factor)
#pdb.set_trace()
Nx=160
Ny=160
Nz=20

sigma=8/100.#delta_x

Lx=8.
Ly=8.
h=1.

F=0.3


def trivariate_uncorelated_Gaussian(x,y,z,mux,muy,muz,sigmax,sigmay,sigmaz):
    """Gaussian function"""
    return np.exp(-0.5 * (((x - mux) ** 2 / sigmax ** 2)+((y - muy) ** 2 /sigmay ** 2)+((z - muz) ** 2 /sigmaz ** 2)))

def Initial_trivariate(x,y,z):
    X, Y, Z = np.meshgrid(x, y,z)
    return trivariate_uncorelated_Gaussian(X,Y,Z,Lx/2,Ly/2,h/2,sigma,sigma,sigma)

def calculate_T_and_R_in_time(total_time=params.total_time,Etot=params.E,true_h=params.h,output_file=params.path_outputs,
                              dilution_factor = params.dillution_factor,v=params.v):

    space_x=np.linspace(0,Lx,num=Nx+1)
    delta_x=space_x[1]-space_x[0]
    space_y=np.linspace(0,Ly,num=Ny+1)
    delta_y=space_y[1]-space_y[0]
    space_z=np.linspace(0,h,num=Nz+1)
    delta_z=space_z[1]-space_z[0]    
    delta_t=F/((1/delta_x**2)+(1/delta_y**2)+(1/delta_z**2))
    Nt = int(round(total_time / float(delta_t)))
    print('given the total time,F and L, I have {0} time meshpoints'.format(Nt))
    
    #checking the normalization
    a=4.
    Ei=Etot/true_h**3
    print('the initial volumetric energy is',Ei)
    
    already_run=False
    if already_run==False:
        u,spacex,spacey,spacez,time=solver_3D.solver_3D_norm(Nx,Ny,Nz,Lx=Lx,Ly=Ly,Initial_xyz=Initial_trivariate,F=F,v=v,a=a,total_time=total_time,reflecting=True,Ei=Ei)#53.125)
        if os.path.exists(output_file+'/images2D')!=True:
            logger.info('the output file for the 2D images did not exist yet. I am creating it now')
            os.makedirs(output_file+'/images2D')
        plotter_3D.plot_u_latest_time(u,space_z,time,time_Units='tD',output_file=output_file,show_plots=True)
    
        #Temperature
        sig_cgs=5.6704e-5
        c_cgs=3e10
        initial_energy_density=1.#5000.0 #erg/cm^3
    
        a_bb = 4 * sig_cgs/ c_cgs
        print('I am calculating temp at the surface')
        temp=np.zeros((Nt + 1, Nx + 1, Ny+1))
        temp[:,:,:] = np.power(1. / a_bb * u[:,:,:,Nz], 0.25)
        #plotter_3D.plot_cuts_2D_temp(temp,spacez,time,time_Units='tD',output_file=output_file,dilution_factor=dilution_factor,show_plots=True)
        #plotter_3D.plot_temp_latest_time(temp,spacez,time,time_Units=None,output_file=output_file,show_plots=False)
        pylab.matshow(temp[-1,:,:].T)
        pylab.xlabel('x axis')
        pylab.ylabel('y axis')
        pylab.title('final temperature at z=h/2',y=1.08)
        pylab.colorbar()
        #pylab.tight_layout()
        pylab.show()
    else:
        time = np.linspace(0, total_time, num=Nt + 1)
    
    time_observed=[]
    print('dilution_factor',dilution_factor)
    time_diluted = time[::dilution_factor]
    index_dilute = range(Nt+1)[::dilution_factor]
    print(np.shape(time_diluted))
    print(np.shape(index_dilute))
    
    Sum_BB_fromfile=np.zeros((len(time[::dilution_factor]),100))
    
    already_run=False
    if already_run==False:
        for t, s in enumerate(time_diluted):
            Sum_BB_ind = np.zeros((100))
            print(t)
            print(s)
            print('I am looking at the edge at time-meshpoint {0}, i.e time {1}'.format(index_dilute[t], s))
            # edge = u[t, :, :, Nz]
            #if s >= tmin and s <= tmax:
            time_observed.append(s)
            #pylab.figure()
                #Sum_BB[t,:,0]=np.linspace(1e-10,1e-6,num=100)
            for i,l in enumerate(spacex):
                for j,k in enumerate(spacey):
                    #print(temp[int(index_dilute[t]),i,j,Nz]
                    #if temp[int(index_dilute[t]),i,j,Nz]!=0.:
                    #pdb.set_trace()
                    #print('I am calculating a cell {0} spectrum'.format()
                    bb_flux_spectrum=black_body_flux_density.black_body_flux_density(temp[int(index_dilute[t]),i,j],np.linspace(1e-10,1e-6,num=100),type='P',verbose=False,distance_pc=1,Radius=None)[2]#les luminosites seront celle de bb 1 solar radius a 1 pc!
                    #pylab.plot(bb_flux_spectrum[:,0]*1e9,bb_flux_spectrum[:,1])
                    #else:
                    #    bb_flux_spectrum=np.zeros(100,2)
                    #    bb_flux_spectrum[:, 0]=np.linspace(1e-10,1e-6,num=100)
                    Sum_BB_ind[:] = Sum_BB_ind[:] + bb_flux_spectrum[:, 1] #erg/sec/cm^2/Ang
                    #Sum_BB[t,:]=Sum_BB[t,:]+bb_flux_spectrum[:,1]
            #pylab.xlabel('wavelegth [$nm$]')
            #pylab.ylabel(r'$B_\lambda$ [$erg/s/cm^2/\AA$]')
            #pylab.title('Edge cells spectra at t={0}'.format(s))
            #pylab.savefig(output_file+'/cells_bb_spectra/cell_bb_' + str(t).zfill(5) + '.png', bbox_inches='tight')
            np.savetxt(output_file+'/Sum_BB_time_{0}.txt'.format(s), Sum_BB_ind[:])
    
    time_observed_x=[]
    for t, s in enumerate(time_diluted):
        #if s >= tmin and s <= tmax:
        print('I am looking at the edge at time-meshpoint {0}, i.e time {1}'.format(int(index_dilute[t]), s))
        time_observed_x.append(s)
    np.savetxt(output_file+'/time_observed.txt',time_observed_x)
    
    distance_modulus=37.77
    distance_pc=distances_conversions.DM_to_pc(distance_modulus)
    
    time_observed_fromfile=np.genfromtxt(output_file+'/time_observed.txt')
    #Sum_BB_fromfile=np.genfromtxt(output_file+'/Sum_BB.txt',skip_header=1)
    for t, s in enumerate(time_diluted): #10s per step 1days~6 steps (60 s per day), 50 days en 50 min
        Sum_BB_fromfile[t,:]=np.genfromtxt(output_file+'/Sum_BB_time_{0}.txt'.format(s))
    
    print(np.shape(Sum_BB_fromfile))
    print(Sum_BB_fromfile[0,:])
    
    pylab.figure()
    for t,s in enumerate(time_observed_fromfile):
        print(t)
        pylab.plot(np.linspace(1e-10,1e-6,num=100)*1e9,Sum_BB_fromfile[t,:])
    pylab.xlabel('wavelegth [$nm$]')
    pylab.ylabel(r'$B_\lambda$ [$erg/s/cm^2/\AA$]')
    #pylab.title('Sum of all edge cells spectra from day {0} to {1} days'.format(tmin,tmax/(3600*24)))
    if os.path.exists(output_file + '/cells_bb_spectra') != True:
        logger.info('the output file for the 2D images did not exist yet. I am creating it now')
        os.makedirs(output_file + '/cells_bb_spectra')

    pylab.savefig(output_file+'/cells_bb_spectra/sum_cells_bb.png', bbox_inches='tight')
    
    already_fit=False
    if already_fit==False:
        BB_evo=np.zeros((np.shape(time_observed_fromfile)[0],4))
        for t, s in enumerate(time_observed_fromfile):
            print('I am looking at time {0}'.format(s))
            Sum_BB_fromfile_w_wavelengths = np.zeros((100, 2))
            Sum_BB_fromfile_w_wavelengths[:, 0] = np.linspace(1e-10, 1e-6, num=100)
            Sum_BB_fromfile_w_wavelengths[:, 1] = Sum_BB_fromfile[t, :]
            Xi_array, best_temp, index_min, best_coeff1, best_radius, best_luminosity=fit_black_body_flux_spec.fit_black_body_flux_spec(Sum_BB_fromfile_w_wavelengths,TempVec=np.logspace(3,6,1000),WaveUnits='m',distance=distance_pc)
            BB_evo[t,0]=s
            BB_evo[t,1]=best_temp
            BB_evo[t,2]=best_radius
            BB_evo[t,3]=best_luminosity
        np.savetxt(output_file+'/Sum_BB_properties.txt',BB_evo,header='time,best-fit temperature,best-fit radius,best-fit luminosity')
    
    
    BB_evo_fromfile=np.genfromtxt(output_file+'/Sum_BB_properties.txt',skip_header=1)
    
    pylab.figure()
    pylab.plot(BB_evo_fromfile[:,0],BB_evo_fromfile[:,1],'r-')
    pylab.xlabel(r'$\frac{t}{h^2/D(z=h)}$',fontsize=25)
    ax=pylab.gca()
    ax.set_xscale("log")
    pylab.grid()
    pylab.ylabel('temperature [K]',fontsize=25)
    pylab.xlim(BB_evo_fromfile[1,0],BB_evo_fromfile[-1,0])
    #pylab.title('Spectrum BB temperature')
    pylab.savefig(output_file+'/edge_spectrum_BB_T.png', bbox_inches='tight')
    
    BB_evo_fromfile=np.genfromtxt(output_file+'/Sum_BB_properties.txt',skip_header=1)
    pylab.figure()
    pylab.plot(BB_evo_fromfile[:,0],BB_evo_fromfile[:,2],'bo')
    pylab.xlabel('time [t/]')
    pylab.ylabel('radius [arb]')
    pylab.title('Spectrum BB radius')
    pylab.grid()
    pylab.savefig(output_file+'/edge_spectrum_BB_R.png', bbox_inches='tight')

    pylab.show()

    temperatures=np.genfromtxt(output_file+'/Sum_BB_properties.txt',skip_header=1)[:,1]
    Luminosities=np.genfromtxt(output_file+'/Luminosities_Dcst_2.txt')

    dilution_factor_1=25
    dilution_factor_2=1
    Luminosities_diluted=Luminosities[::dilution_factor_1]

    pylab.figure()
    pylab.plot(Luminosities)
    pylab.show()

    print(Luminosities_diluted)

    #pdb.set_trace()

    radii=np.power((1./(4*math.pi*sig_cgs)*np.multiply(Luminosities_diluted,1/np.power(temperatures,4))),0.5)
    time_Dcst_diluted=time[::dilution_factor_1]

    time_Dcst_diluted_more=time_Dcst_diluted[::dilution_factor_2]
    radii_diluted_more=radii[::dilution_factor_2]

    pylab.figure()
    pylab.plot(time_Dcst_diluted_more,radii_diluted_more,'b-')
    pylab.grid()
    pylab.xlabel(r'$\frac{t}{h^2/D(z=h)}$',fontsize=25)
    pylab.ylabel(r'Radius $r_{BB}$ [cm]', fontsize=25)
    pylab.savefig(output_file+'/edge_spectrum_BB_R_2.png',bbox_inches='tight')
    pylab.show()

    #only if you ran solver_diffusion_and_calc_spectrum_w_true_values.py before
    BB_evo_fromfile=np.genfromtxt(output_file+'/Sum_BB_properties.txt',skip_header=1)

    #pylab.figure()

    #pylab.title('Spectrum BB temperature')
    #pylab.savefig(output_file/edge_spectrum_BB_T.png', bbox_inches='tight')


    pylab.figure()
    f = plt.figure(figsize=(8,8))
    ax1 = plt.subplot(212)
    plt.plot(BB_evo_fromfile[:,0],BB_evo_fromfile[:,1],'r-')
    plt.xlabel(r'$\rm{\frac{t}{t_d}}$',fontsize=25)
    ax=pylab.gca()
    ax.set_xscale("log")
    pylab.grid(True, which="both")
    plt.ylabel('temperature [K]',fontsize=23)
    plt.xlim(BB_evo_fromfile[1,0],BB_evo_fromfile[-1,0])
    plt.yticks(fontsize=16)
    plt.xticks(fontsize=16)
    # share x only
    ax2 = plt.subplot(211, sharex=ax1)
    plt.plot(time_Dcst_diluted_more,radii_diluted_more/1e15,'b-')
    pylab.grid(True, which="both")
    #plt.xlabel(r'$\frac{t}{h^2/D(z=h)}$',fontsize=25)
    plt.ylabel(r'Radius $r_{BB}$ [$\rm{10^{15}}\,$cm]', fontsize=18)
    #plt.savefig(output_file/edge_spectrum_BB_R_2.png',bbox_inches='tight')
    plt.yticks(fontsize=16)
    plt.xticks(fontsize=16)
    plt.xlim(0.01,1)
    #plt.ylim(0,16e15)
    plt.setp(ax2.get_xticklabels(), visible=False)
    #pylab.tight_layout()
    #plt.savefig('./paper_figures/kernel_comparision_same_xaxis.pdf', facecolor='w', edgecolor='w',
    #              orientation='portrait',
    #              papertype=None, format='pdf', transparent=False, bbox_inches=None, pad_inches=0.5)
    plt.savefig(output_file+'/edge_spectrum_BB_R_T_sameaxis.png',bbox_inches='tight')


    pylab.show()


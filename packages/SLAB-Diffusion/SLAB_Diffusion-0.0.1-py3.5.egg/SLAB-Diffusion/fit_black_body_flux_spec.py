#! //anaconda/bin/python

"""*******************************************************

******************************************************"""
#print __doc__

import os
import numpy as np
from numpy import linalg
import pdb
import black_body_flux_density
import pylab
import fitting_tools
import distances_conversions
import energy_conversions
import math
import shutil
import logging
import correct_spectrum
import copy
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fit_black_body_flux_spec(Spec,TempVec=None,FLuxUnits=None,comments="#",WaveUnits=None,distance=None,Ebv=0,z=0,ndof=None,covariance=None,show_plot=False,Verbose='on',output_file=None,output_pdf_file=None,path_to_txt_file=None,vertical_line_T=None):
	"""Description: Fit a black-body spectrum alpha*F_bb to an observed spectrum (in flux units).
	Input  :- Spec: either a numpy array or a path to file with 1st column: wavelemgth, anf second column flux Observed spectrum [Wave, Flux]. [WaveUnits,erg/cm^2/s/A]. Default is [m,erg/cm^2/s/A]
			- comments: if Spec is a path to a file, the character used to indicate the start of a comment. All the characters occurring on a line after a comment are discarded. Default is #
			- TempVec : Vector of temperatures to test [K].If empty matrix the use default. Default is logspace(3,6,500). For each of these temperature, the code fits A*Model(T) to the data. then the best temperature is chosen
			- FluxUnits units of flux
				-
				-
			- WaveUnits units of wavelength in Spectrum
				- 'A' angstrom
				- 'nm' nanometers
				- 'cm' centimeters
				- 'm' meters
				- 'Hz' TO DO
				- 'eV' TO DO
				- 'keV' TO DO
			- Optional distance [pc], default is 10pc.
			- Extinction correction (E_{B-V}) to apply to the spectrum before the fit. Default is None. IF YU USE THIS MAKE SURE YOU HAVE NOT CORRECTED THE INPUT SPECTRUM YET
			- Redshift correction z to apply to the spectrum before the fit. Default is None. IF YU USE THIS MAKE SURE YOU HAVE NOT CORRECTED THE INPUT SPECTRUM YET

			The correction is applied as: f_true=f_obs*10^(0.4*A), where A is defined as mag_obs=mag_true+A
			- show_plot: if set to True, show the plot. create it in anycase.
			- Verbose: if 'on', print final results
			- path_to_txt_file: if given, then the final result will br printed into a text file placed there
	Output :- numpy array with the following fields:
				-temperature
				-for this temperature, best fit multiplication factor alpha. alpha is (R/d)^2, and therefore gives you the radius if you know the distance.
	 		(see my lecture notes in observationnal astronomy for an explanation of alpha).
	 			-for this temperature, value of best fit chi2
	 			-for this temperature, value of the radius in cm
	 		-value of best temperature index in Xi_array
	 		-value of best temperature coeff1
	 		-value of best temperature radius in cm
	Plots and output files: -plot best fit in .outputs_from_fit_black_body_flux_spec_function/fit_result.pdf
							-plot chi2, coeff, and R in outputs_from_fit_black_body_flux_spec_function/fit_grid_results.pdf
							-save sorted_Xi_array in outputs_from_fit_black_body_flux_spec_function/Sorted_fir_results.txt
	Tested : ?
	    By : Maayane T. Soumagnac Nov 2016
	   URL :
	Example: [Xi_array,best_temp,index_min,best_coeff,best_radius]=fit_black_body.fit_black_body_spec(black_body_with_errors,distance=1.,show_plot=True)
	Reliable:
	 TO DO: give an option for the speed: decrease the length of TempVec, give the spec units as options"""
	if output_file==None:
		if os.path.exists('./outputs_from_fit_black_body_flux_spec_function'):
			logger.info('output_path/txt_files did exist, I am removing it and creating a new one')
			#shutil.rmtree('./outputs_from_fit_black_body_flux_spec_function')
		else:
			logger.info('the output file file did not exist yet. I am creating it now')
			os.makedirs('./outputs_from_fit_black_body_flux_spec_function')
		output_file='./outputs_from_fit_black_body_flux_spec_function'
	if isinstance(Spec, str):
		print('you provided a filename for the spectrum')
		Spectrum = np.genfromtxt(Spec, comments=comments)
	elif isinstance(Spec, np.ndarray):
		print('you provided a numpy array for the spectrum')
		print('Spec is',Spec)
		#pdb.set_trace()
		Spectrum = copy.copy(Spec)
	else:
		print('ERROR: Unsupported type for Spec')
		pdb.set_trace()
	if output_pdf_file==None:
		if os.path.exists(output_file+'/pdf_files'):
			logger.info('output_path/pdf_files did exist')
			#shutil.rmtree('./outputs_from_fit_black_body_flux_spec_function')
		else:
			logger.info('output_path/pdf_files did not exist. I am creating it now')
			os.makedirs(output_file+'/pdf_files')
		output_pdf_file=output_file+'/pdf_files'
	path_to_param_file=output_file+'/best_param.txt'
	path_to_best_fit_spectrum=output_file+'/best_fit_spectrum.txt'
	Spectrum_corrected = np.zeros(np.shape(Spectrum))
	#print Spectrum_in_meters
	#******************** correct flux with extinction ************************
	#print Ebv
	#print z
	#pdb.set_trace()
	if z==None:
		z=0
	if Ebv!=0 and z==0:
		print('You provided extinction corrections only')
		Spectrum_corrected=correct_spectrum.correct_spectrum_for_redshift_and_extinction(Spectrum,Ebv=Ebv,comments="#",WaveUnits=WaveUnits,z=0,show_plot=False,title=None,output_pdf_file=output_pdf_file)
		#convert spectrum into microns, as it is the units supported by the extinction functions
		#Spectrum_microns = np.zeros(np.shape(Spectrum))
		#Spectrum_microns[:,0]=Spectrum_in_meters[:,0]*1e6 #wavelength in microns
		#Spectrum_microns[:,1]=Spectrum_in_meters[:,1]
		#Spectrum_corrected[:,1]=extinction.correct_obs_flux_for_extinction(Spectrum_microns,Ebv,Model=None,R=None)[:,1]
		#Spectrum_corrected[:,0]=Spectrum_in_meters[:,0]

		#print 'SPectrum microns',Spectrum_microns
		#print 'Spectrum corrected',Spectrum_corrected
		# Spectrum_corrected is now in meters and flux
	elif Ebv==0 and z!=0:
		print('You provided redshift corrections only')
		Spectrum_corrected=correct_spectrum.correct_spectrum_for_redshift_and_extinction(Spectrum,Ebv=0,comments="#",WaveUnits=WaveUnits,z=z,show_plot=False,title=None,output_pdf_file=output_pdf_file)
		#Spectrum_corrected[:,1]=correct_spectrum.correct_spectrum_for_redshift(Spectrum_in_meters,comments="#",WaveUnits='m',z=z,show_plot=True,title=None)[:,1]
		#Spectrum_corrected[:,0]=correct_spectrum.correct_spectrum_for_redshift(Spectrum_in_meters,comments="#",WaveUnits='m',z=z,show_plot=True,title=None)[:,0]
	elif Ebv!=0 and z!=0:
		print('You provided both extinction and redshift corrections')
		Spectrum_corrected = correct_spectrum.correct_spectrum_for_redshift_and_extinction(Spectrum, Ebv=Ebv, comments="#",
																					   WaveUnits=WaveUnits, z=z,
																					   show_plot=False, title=None)
	else:
		print('You provided no corrections')
		Spectrum_corrected=copy.copy(Spectrum)
	#Spectrum_corrected[:,1]=correct_spectrum.correct_spectrum_for_redshift_and_extinction(Spectrum_in_meters,Ebv=Ebv,comments="#",WaveUnits='m',z=z,show_plot=True,title=None)[:,1]
		#Spectrum_corrected[:,0] =correct_spectrum.correct_spectrum_for_redshift_and_extinction(Spectrum_in_meters,Ebv=Ebv,comments="#",WaveUnits='m',z=z,show_plot=True,title=None)[:,0]
	#else:
		#print 'There is no extinction'
		 # in meters
	#Spectrum_corrected[:, 0] = Spectrum_in_meters[:, 0]

	#******************** convert all waveunits into meters ***********************
	Spectrum_in_meters=np.zeros(np.shape(Spectrum_corrected))
	if WaveUnits.lower()=='a':
		Spectrum_in_meters[:,0]=Spectrum[:,0]*1e-10 #A in meters
		Spectrum_corrected[:,0]=Spectrum_corrected[:,0]*1e-10 #A in meters
	elif WaveUnits.lower()=='nm':
		Spectrum_in_meters[:,0]=Spectrum[:,0]*1e-9
		Spectrum_corrected[:,0]=Spectrum_corrected[:,0]*1e-9 #nm in meters
	elif WaveUnits.lower()=='cm':
		Spectrum_in_meters[:, 0]=Spectrum[:,0]*1e-2 #cm in meters
		Spectrum_corrected[:, 0]=Spectrum_corrected[:,0]*1e-2 #cm in meters
	elif WaveUnits.lower()=='m':
		#Spectrum_corrected[:, 0]=Spectrum_corrected[:,0]
		Spectrum_corrected[:, 0]=Spectrum_corrected[:,0]
	elif WaveUnits==None:
		Spectrum_corrected[:, 0]=Spectrum_corrected[:,0] # default is meters
	else:
		print('WaveUnits unsupported yet')
		pdb.set_trace()
	Spectrum_in_meters[:,1]=Spectrum[:,1] # TO DO fluxUnits support
	# ******************** Fit ************************
	if TempVec==None:
		Temp=np.logspace(3.,6.,500)
		#TempVec = np.arange(1000, 100000, 10)
	else:
		Temp=TempVec
	if distance==None:
		dist=distances_conversions.pc_to_cm(10) # dist in cm
		#print 'the distance in cm is {0}'.format(dist)
	else:
		dist=distances_conversions.pc_to_cm(distance)
		#print 'the distance in cm is {0}'.format(dist)
	coeff1=np.zeros(np.shape(Temp))
	#This is in case there are 2 param in model l1*black_body+l2: coeff2=np.zeros(np.shape(Temp))
	#Xi_array=np.empty([np.shape(Temp)[0],4], dtype=object)
	Xi_array=np.empty([np.shape(Temp)[0],4], dtype=object)
	#extinction
	index=np.zeros(np.shape(Temp))
	if covariance==None:
		for i, j in enumerate(Temp):
			index = i
			#print 'the checked temperature is {0}'.format(j)
			#This is in case there are 2 param in model l1*black_body+l2: A = np.array(zip(black_body_flux_density.black_body_flux_density(j, Spectrum_corrected[:, 0], 'P')[0][:, 1],
			#				 ones))
			A = np.array(black_body_flux_density.black_body_flux_density(j, Spectrum_corrected[:, 0], 'P')[2][:, 1])
			matrix_solution=np.dot(1./(np.dot(A.transpose(),A)),(np.dot(A.transpose(),Spectrum_corrected[:,1])))
			coeff1[i] = matrix_solution
			#This is in case there are 2 param in model l1*black_body+l2: coeff1[i] = matrix_solution[0]
			#This is in case there are 2 param in model l1*black_body+l2: coeff2[i] = matrix_solution[1]
			Xi_array[i, 0] = j
			Xi_array[i,1]=coeff1[i]
			#This is in case there are 2 param in model l1*black_body+l2: Xi_array[i, 1] = coeff2[i]
			#This is in case there are 2 param in model l1*black_body+l2: Xi_array[i, 2] = objective_no_cov(coeff1[i]*black_body_flux_density.black_body_flux_density(j, Spectrum_corrected[:, 0], 'P')[0][:, 1]+coeff2[i],Spectrum_corrected).chi_square_value()
			Xi_array[i, 2] = fitting_tools.objective_no_cov(
				coeff1[i] * black_body_flux_density.black_body_flux_density(j, Spectrum_corrected[:, 0], 'P')[2][:, 1],
				Spectrum_corrected).chi_square_value()
			if coeff1[i]<=0:
				Xi_array[i,3]=0
			else:
				Xi_array[i,3]= math.sqrt(coeff1[i]*dist**2)#radius in cm
		#print np.shape(Spectrum_corrected)[0]
#		covar=np.identity(np.shape(Spectrum_corrected)[0])
#		invcov=linalg.inv(covar)
	else:
		invcov=linalg.inv(covariance)
		for i, j in enumerate(Temp):
			index=i
			A = np.array(black_body_flux_density.black_body_flux_density(j, Spectrum_corrected[:, 0], 'P')[2][:, 1])
			matrix_solution = np.dot(linalg.inv(np.dot(np.dot(A.transpose(), invcov), A)),
									 (np.dot(np.dot(A.transpose(), invcov), Spectrum_corrected[:, 1])))
			coeff1[i] = matrix_solution
			#This is in case there are 2 param in model l1*black_body+l2: coeff1[i] = matrix_solution[0]
			#This is in case there are 2 param in model l1*black_body+l2: coeff2[i] = matrix_solution[1]
			Xi_array[i, 0] = j
			Xi_array[i, 1] = coeff1[i]
			#This is in case there are 2 param in model l1*black_body+l2: Xi_array[i, 1] = coeff2[i]
			# This is in case there are 2 param in model l1*black_body+l2: Xi_array[i, 2] = objective_no_cov(coeff1[i]*black_body_flux_density.black_body_flux_density(j, Spectrum_corrected[:, 0], 'P')[0][:, 1]+coeff2[i],Spectrum_corrected).chi_square_value()
			Xi_array[i, 2] = fitting_tools.objective_with_cov(coeff1[i]*black_body_flux_density.black_body_flux_density(j, Spectrum_corrected[:, 0], 'P')[2][:, 1],Spectrum_corrected,invcov).chi_square_value()
			if coeff1[i]<=0:
				Xi_array[i,3]=0
			else:
				Xi_array[i,3]= math.sqrt(coeff1[i]*dist**2)#radius in cm
	index_min=np.argmin(Xi_array[:,2])
	best_coeff1=coeff1[index_min]
	#This is in case there are 2 param in model l1*black_body+l2: best_coeff2=coeff2[index_min]
	best_temp=Temp[index_min]
	best_radius=Xi_array[index_min,3]
	#mettre best radius en m: 4piR^2sigmaT^4
	#best_luminosity=energy_conversions.convert_energy(4*math.pi*(distances_conversions.solar_radius_to_m(best_radius))**2*5.7e-8*best_temp**4,'J','erg')
	best_luminosity = energy_conversions.convert_energy(
		4 * math.pi * (best_radius * 1e-2) ** 2 * 5.7e-8 * best_temp ** 4, 'J', 'erg')  # en w

	# print 'best coeff1 is {0}'.format(best_coeff1)
	# print 'best coeff2 is {0}'.format(best_coeff2)
	#print 'the best temperature is {0}'.format(best_temp)
	sorted_Xi_array = Xi_array[Xi_array[:,2].argsort()]
	np.savetxt(output_file+'/Sorted_fit_result.txt',
				   sorted_Xi_array, header='best coefficient A (in model A*blackbody), best temperature, sorted chi2')

	#******************** Plots ************************

	#Plot the fitting results
	pylab.figure()
	if Ebv!=0 and z==0:
		print('You provided extinction corrections only')
		#print Spectrum_corrected
		pylab.plot(Spectrum_in_meters[:, 0]*1e9, Spectrum_in_meters[:, 1], 'ro', label=r'data')
		pylab.plot(Spectrum_corrected[:, 0]*1e9, Spectrum_corrected[:, 1], 'bo', label=r'data corrected for extinction')
	elif Ebv!=0 and z!=0:
		print('You provided both extinction E={0} and redshift z={1} corrections'.format(Ebv,z))
		pylab.plot(Spectrum_in_meters[:, 0] * 1e9, Spectrum_in_meters[:, 1], 'ro', label=r'data')
		pylab.plot(Spectrum_corrected[:, 0] * 1e9, Spectrum_corrected[:, 1], 'bo',
				   label=r'data corrected for extinction and redshift')
	elif Ebv==0 and z!=0:
		print('You provided redshift corrections only')
		pylab.plot(Spectrum_in_meters[:, 0] * 1e9, Spectrum_in_meters[:, 1], 'ro', label=r'data')
		pylab.plot(Spectrum_corrected[:, 0] * 1e9, Spectrum_corrected[:, 1], 'bo',
				   label=r'data corrected for redshift')
	else:
		pylab.plot(Spectrum_corrected[:, 0] * 1e9, Spectrum_corrected[:, 1], 'ro',label=r'data')
	#This is in case there are 2 param in model l1*black_body+l2: pylab.plot(Spectrum_corrected[:,0]*1e9,best_coeff1*black_body_flux_density.black_body_flux_density(best_temp, Spectrum_corrected[:, 0], 'P')[0][:,1]+best_coeff2,'-b',label='best fit')

	pylab.plot(np.linspace(1e-10, 1e-6, num=1000) * 1e9,black_body_flux_density.black_body_flux_density(best_temp, np.linspace(1e-10, 1e-6, num=1000), 'P',
															   distance_pc=distance,
															   Radius=distances_conversions.cm_to_solar_radius(
																   best_radius))[2][:,1],'-g', label='best fit')


	#pylab.plot(np.linspace(1e-10, 1e-6, num=1000) * 1e10,
	#		   best_coeff1 * black_body_flux_density.black_body_flux_density(best_temp, np.linspace(1e-10, 1e-6, num=1000) * 1e10, 'P')[2][:, 1],
	#		   'g-', label='best fit')
	ax = pylab.gca() #'{:0.3e}'.format(2.32432432423e25)
	ax.text(0.2, 0.05,'$T=${0}$K$, $R=${1}$cm$'.format('{:.2f}'.format(round(best_temp,2)),'{:.2e}'.format(best_radius)),
			transform=ax.transAxes, bbox=dict(facecolor='none', edgecolor='green', boxstyle='square'))
	pylab.xlabel('wavelength $(nm)$')
	pylab.grid()
	pylab.legend()
	pylab.title(r'Results of fit')
	pylab.savefig(output_pdf_file+'/fit_result.pdf', facecolor='w', edgecolor='w',
					  orientation='portrait', papertype=None, format='pdf', transparent=False, bbox_inches=None,
					  pad_inches=0.1)


	#Plot Xi_array fields
	f, axarr = pylab.subplots(3, sharex=True)
	#x_formatter = ScalarFormatter(useOffset=False)
	axarr[0].plot(Xi_array[:,0], Xi_array[:,2], 'b',
				  label=r'$\chi^2$')
	if vertical_line_T!=None:
		axarr[0].axvline(vertical_line_T)
	axarr[0].plot(best_temp, Xi_array[index_min, 2], 'ro',markersize=5)
	axarr[0].set_title(r'Results of fit')
	axarr[0].set_ylabel(r'best fit $\chi^2$')
	#axarr[1].set_xlabel(r'checked temperature')
	axarr[0].grid()
	axarr[0].axvline(x=best_temp,color='k',linestyle='--')
	if TempVec==None:
		axarr[0].set_xscale('log')
	axarr[1].plot(Xi_array[:,0], Xi_array[:,1],'r',
				  label=r'multiplicative factor')
	axarr[1].set_ylabel(r'best fit multiplicative factore')
	axarr[1].plot(best_temp, Xi_array[index_min, 1], 'ro',markersize=5)
	#pylab.xlim(min(julian_days_NUV), max(julian_days_NUV))
	#pylab.legend(label=['common measurement days'])
	# pylab.gca().invert_yaxis()
	axarr[1].grid()
	axarr[1].axvline(x=best_temp,color='k',linestyle='--')
	if TempVec==None:
		axarr[1].set_xscale('log')
	#axarr[0].xaxis.set_major_formatter(x_formatter)
	axarr[2].plot(Xi_array[:,0], Xi_array[:,3], 'm',
				  label=r'Radius')
	axarr[2].plot(best_temp, Xi_array[index_min, 3], 'ro',markersize=5)
	axarr[2].set_ylabel(r'best fit radius')
	axarr[2].set_xlabel(r'checked temperature')
	axarr[2].grid()
	axarr[2].axvline(x=best_temp,color='k',linestyle='--')
	if TempVec == None:
		axarr[2].set_xscale('log')
	#axarr[1].xaxis.set_major_formatter(x_formatter)
	pylab.savefig(output_pdf_file + '/fit_grid_results.pdf', facecolor='w', edgecolor='w',
					  orientation='portrait', papertype=None, format='pdf', transparent=False, bbox_inches=None,
					  pad_inches=0.1)


	if show_plot == True:
		pylab.show()
	if Verbose=='on':
		print('The best fit temperature is {0} and the best fit radius is {1}, and the best coef is {2}'.format(best_temp,best_radius,best_coeff1))
	result_matrix=np.zeros((1,6))
	result_matrix[0,0]=0
	result_matrix[0,1]=best_temp
	result_matrix[0,2]=index_min
	result_matrix[0,3]=best_coeff1
	result_matrix[0,4]=best_radius
	result_matrix[0,5]=best_luminosity
	#if path_to_txt_file!=None:
	np.savetxt(path_to_param_file,result_matrix,header='place holder, best temp, index, best coeff, best_radius, best luminosity')
	best_fit_spectrum=np.zeros((1000,2))
	best_fit_spectrum[:,0]=np.linspace(1e-10,1e-6,num=1000)*1e10
	best_fit_spectrum[:,1]=best_coeff1 * black_body_flux_density.black_body_flux_density(best_temp, np.linspace(1e-10,1e-6,num=1000), 'P')[2][:,
                         1]
	np.savetxt(path_to_best_fit_spectrum,best_fit_spectrum,header='Wavelength $[\AA]$,Flux $[erg/sec/cm^2/\AA ]$')
	print('Spectrum inside fit_bb is',Spectrum)
	print('Spec is',Spec)
	#pdb.set_trace()
	return Xi_array,best_temp,index_min, best_coeff1, best_radius,best_luminosity


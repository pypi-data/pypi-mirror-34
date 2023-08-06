
"""*******************************************************
This module creates black_body flux density
*****************************************************
"""
#print __doc__


from astropy import constants as const
import math
import distances_conversions
import numpy as np
import pdb

def black_body_flux_density(Temp,wavelength,type=None,verbose=False,distance_pc=None,Radius=None):
    """Description: Given a temperature, calculates a black body flux density B_lambda.
    If a radius anda distance are given, calculate the apparent flux density (R/d)^2*B_lambda
    Input  :- Temperature [K]
            - numpy array of wavelengths [m], tipically np.linspace(1e-10,1e-6,num=1000)
            - type of formula:
                'P' Planck
                'RJ' Rayleigh-Jeans approximation
            - Radius (optionnal) in solar radius
            - distance (optionnal) in pc
            - Ebv: (optionnal, default is none) extinction to correct the theoretical spectrum with
            - redshift: (optionnal, default is none) z to apply to the theoretical spectrum with
    Output :array of numpy.arrays [spectrum_cgs,spectrum_Hz,spectrum_A,spectrum_mJy,spectrum_phot] CAREFULLL! confusing between spectrum_cgs and spectrum_A has caused so much arm in the past!
            - spectrum_cgs: wavelength [m], Emittance (flux density) in erg/sec/cm^2/cm(lambda)
            - spectrum_Hz: wavelength [m], Emittance in erg/sec/cm^2/Hz
            - spectrum_A: wavelength [m], Emittance in erg/sec/cm^2/Ang (lambda), 1e-8*Emittance (flux density) in erg/sec/cm^2/cm(lambda)
            - spectrum_mjy: wavelength [m], Emittance [mJy]
            - spectrum_phot: wavelength [m], number of photons [photons/sec/cm^2/Ang (lambda)]
    Tested : ?
         By : Maayane T. Soumagnac Nov 2016
        URL :
    Example:[E_cgs, E_Hz, E_A,Emjy, E_phot] = black_body_models.black_body_models(3000, wavelengths, 'P')
    Reliable:  """

    h_cgs=const.h.cgs.value
    c_cgs=const.c.cgs.value
    kB_cgs=const.k_B.cgs.value

    wavelength_in_cm=wavelength*1e2 # wavelength in cgs
    wavelength_in_cm = wavelength_in_cm.astype(float)
    nu=c_cgs/wavelength_in_cm #frequency in s (because c is in cm/s and wavlength in cm)
    if (Radius!=None and distance_pc!=None):

        R_pc=distances_conversions.solar_radius_to_pc(Radius)
        coeff=(R_pc/distance_pc)**2

    else:
        if verbose==True:
            print('the radius or distance or both were not specified')
        coeff=1.

    if type.lower() in (None,'p'):
        if verbose==True:
            print('formula used for black body: Planck')
        b_cgs=h_cgs*c_cgs/(wavelength_in_cm*kB_cgs*Temp)

        if verbose == True:
            print('b_cgs is', b_cgs)
            print('be aware that {0} elements in the exponent of the Planck formula lead to an infinite exponent'.format(np.shape(np.exp(b_cgs)[np.isinf(np.exp(b_cgs))==True])[0]))
            print('denom shape is',np.shape(h_cgs*c_cgs/(wavelength_in_cm*kB_cgs*Temp)))

        E_cgs=coeff*2*math.pi*h_cgs*c_cgs**2/(wavelength_in_cm**5 *(np.exp(h_cgs*c_cgs/(np.float64(wavelength_in_cm)*kB_cgs*Temp)) - 1.0))
        E_Hz=coeff*2*math.pi*h_cgs*nu**3/(c_cgs**2*(np.exp(h_cgs*nu/(kB_cgs*Temp))-1.0)) #this is the planck formula in Hz ()
        E_A=E_cgs*1e-8 # because cm-1 =(1e8 A)-1
        E_mjy=1e-26*E_Hz # because 1Jy=1e-26 J/(sec*m^2*Hz) and 1J=1e7erg
        E_phot=coeff*2*math.pi*nu**2/(c_cgs**2*(np.exp(h_cgs*nu/(kB_cgs*Temp))-1.0))
    elif type.lower() == 'rj':
        if verbose == True:
            print('formula used for black body: Rayleigh-Jeans')
        E_cgs=coeff*2*math.pi*c_cgs*kB_cgs*Temp/wavelength_in_cm**4
        E_Hz=coeff*2*math.pi*kB_cgs*Temp*(nu/c_cgs)**2
        E_A = E_cgs * 1e-8  # because cm-1 =(1e8 A)-1
        E_mjy = 1e-26 * E_Hz  # because 1Jy=1e-26 J/(sec*m^2*Hz) and 1J=1e7erg
        E_phot=None # I am not sure
    else:
        print('unknown formula')
        pdb.set_trace()

    redshift = 0
    wavelength_fixed=wavelength*(redshift+1)
    E_A_fixed=E_A/(redshift+1)
    spectrum_cgs=np.array(list(zip(wavelength_fixed,E_cgs)))
    spectrum_Hz=np.array(list(zip(wavelength_fixed,E_Hz)))
    spectrum_A=np.array(list(zip(wavelength_fixed,E_A_fixed)))
    spectrum_mjy=np.array(list(zip(wavelength_fixed,E_mjy)))
    spectrum_phot=np.array(list(zip(wavelength_fixed,E_phot)))

    return spectrum_cgs, spectrum_Hz, spectrum_A, spectrum_mjy, spectrum_phot



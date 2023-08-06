# SLAB_Diffusion
The `SLAB-Diffusion` package is a tool for modeling the radiative diffusion of photons through a slab of circumstellar material (CSM), e.g. in order to simulate the observables (effective blackbody temperature and radius) of an interacting Supernova.

[![PyPI](https://img.shields.io/pypi/v/SLAB-Diffusion.svg?style=flat-square)](https://pypi.python.org/pypi/SLAB-Diffusion)

```python
>>> import SLAB_Diffusion
>>> SLAB_Diffusion.calculate_T_and_R_in_time()
```

## Documenation

The `SLAB_Diffusion` package was used in [Soumagnac et al, 2018]() to model the radiative diffusion of photons through a slab of circumstellar material. 

The version available here assumes constant density (and hence diffusion constant) in the slab. A more sophisticated version with varying density can be made available on demand by emailing maayane.soumagnac at weizmann.ac.il

## Credit
If you are using SLAB-Diffusion, please reference Soumagnac et al. 2018 

[Bibtex entry for Soumagnac et al. 2018]()

## How to install the `SLAB-Diffusion` code?

### pip

`pip install SLAB_Diffusion`

### Python version
* `python 2`: higher than `2.7.10`
* `python 3`

### Required python packages
* `math`
* `numpy`
* `pylab`
* `math`
*  `matplotlib`

## How to run the `SLAB-Diffusion` code?

### Edit the params.py file

The default parameters are those used in Soumagnac et al. 2018 and allow to recover Figure 11.
After every modification of `params.py`, rerun

```python
>>> python setup.py install
```
from the `SLAB_Diffusion` directory

### Visualize the evolution of R and T for a given slab

```python
>>> import SLAB_Diffusion
>>> SLAB_Diffusion.calculate_T_and_R_in_time()
```




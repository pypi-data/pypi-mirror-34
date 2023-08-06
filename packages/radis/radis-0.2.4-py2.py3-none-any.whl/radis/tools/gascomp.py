# -*- coding: utf-8 -*-
"""
Determine Gas composition using Cantera
"""

from __future__ import absolute_import
from radis.misc.utils import NotInstalled
try:
    import cantera as ct
except:
    ct = NotInstalled('cantera', 'Cantera is needed to calculate equilibrium mole fractions'+\
                      '. Install with  `pip install cantera`')
    
def get_eq_mole_fraction(initial_mixture, T, p):
    ''' Returns mole fraction at temperature T 
    
    Parameters
    ----------
    
    initial_mixture: str
        Gas composition. Example::
            
             'N2:0.79, O2:0.21, CO2:363e-6'
             
        Or: 
            
             'CO2:1'
             
    T: float (K)
        temperature (Kelvin) to calculate equilibrium
        
    P: float (Pa)
        temperature (Pascal) to calculate equilibrium
        
    Examples
    --------
    
    Calculate equilibrium mixture of CO2 at 2000 K, 1 atm::
        
        >>> get_eq_mole_fraction('CO2:1', 2000, 101325)
        
        {'C': 1.7833953335281855e-19,
         'CO': 0.01495998583472384,
         'CO2': 0.9775311634424326,
         'O': 5.7715610124613225e-05,
         'O2': 0.007451135112719029}
        
    '''

    # %% Init Cantera
    g = ct.Solution('gri30.xml')
    g.TPX = T, p, initial_mixture
    
    # Minimize Gibbs:
    g.equilibrate('TP')
    
    # Returns
    return g.mole_fraction_dict()
    

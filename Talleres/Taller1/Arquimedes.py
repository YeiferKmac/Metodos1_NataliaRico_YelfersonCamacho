<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 21:43:50 2022

@author: LENOVO 4
"""

import numpy as np
import matplotlib.pyplot as mplt
import sympy as sym

#
def polar_to_cartesian(r, theta): 
   xx = r * sym.cos(theta)
   yy = r * sym.sin(theta) 
=======
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 21:43:50 2022

@author: LENOVO 4
"""

import numpy as np
import matplotlib.pyplot as mplt
import sympy as sym

#
def polar_to_cartesian(r, theta): 
   xx = r * sym.cos(theta)
   yy = r * sym.sin(theta) 
>>>>>>> d40ca733cedba27ae221b6502e8fdca20fde37df
   return(xx, yy)
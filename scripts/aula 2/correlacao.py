#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Covariância e correlação

@author: cafe
"""

import numpy as np
import pandas as pd

# Vamos construir nossos dados correlacionados

x = np.arange(1,101)
y = 2*x
z = x**2
w = np.exp(x)

dados = pd.DataFrame([x,x,y,z,w]).T

# Níveis de correlação
dados.plot(0,1,title=f'Correlação= {dados[[0,1]].corr()[0][1]}')
dados.plot(0,2,title=f'Correlação= {dados[[0,2]].corr()[0][2]}')
dados.plot(0,3,title=f'Correlação= {dados[[0,3]].corr()[0][3]}')
dados.plot(0,4,title=f'Correlação= {dados[[0,4]].corr()[0][4]}')

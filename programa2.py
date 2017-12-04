# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:31:52 2017

@author: nacho
"""

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt


# Constante de gravitación universal:
G = 6.67*10**(-11)
# Masa del Sol en kg:
msol = 1.9*10**30

def pinta_curva_y_planetas(planetas_dist,planetas_v,planetas_nombre):
    
    mpl.rcParams['figure.dpi']= 150
    
    fig2,ax2=plt.subplots()
    
    distancia_vec = np.arange(50,5000,0.1)
    v_vec = np.sqrt(G*msol/(distancia_vec*10**9))
    
    plt.plot(distancia_vec,v_vec)
    plt.plot(planetas_dist,planetas_v,'bo',ms=10)
    plt.xlabel(r"Distancia media al Sol en millones de $km$")
    plt.ylabel(r"Velocidad del planeta en $m/s$")
    
    for i, txt in enumerate(planetas_nombre):
        ax2.annotate(txt,xy=(planetas_dist[i],planetas_v[i]),xytext=(planetas_dist[i]+100,planetas_v[i]+100))
        
    plt.show()
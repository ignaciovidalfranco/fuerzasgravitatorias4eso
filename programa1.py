from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np


factor_de_velocidad = 4
factor_v = 10
factor_aceleracion  = 10
dref = 149597870700

def pinta_resultados(Fgravedad,a,v,T,Tdias):
    
    print('Fuerza Sol-Planeta: {} Newtons'.format(Fgravedad))
    print('Aceleración centrípeta: {} m/s^2'.format(a))
    print('Velocidad: {} m/s'.format(v))
    print('Período (en segundos): {} s'.format(T))
    print('Período (en días): {} dias'.format(Tdias))

#######################################################################
## A partir de aquí, todo es código para hacer la animación...       ##
#######################################################################

centro_orbita = (7,7)

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)
ax = plt.axes(xlim=(0, 14), ylim=(0, 14))

patchTierra = plt.Circle(centro_orbita, 0.25, fc='b')
patchSol = plt.Circle(centro_orbita, 0.75, fc='y')

vector_a = ax.quiver(0,0,0,0,angles='xy', scale_units='xy', scale=4.5,color='r')
vector_v = ax.quiver(0,0,0,0,angles='xy', scale_units='xy', scale=4.5)    

def init():
    
    ax.set_aspect('equal')    
    ax.axis('off')
    ax.add_patch(patchTierra)
    ax.add_patch(patchSol)
    return patchTierra,patchSol,

def animate(i,factor_de_distancia,a,v):
    
    # Hago que la figura de vueltas siguiendo la ecuación de un círculo.
    vref = 29105
    aref = 0.0056
    radianes = np.radians((v/vref)*i)
    
    x = centro_orbita[0] + factor_de_distancia*np.sin(radianes)
    y = centro_orbita[1] + factor_de_distancia*np.cos(radianes)
    
    vector_a.set_offsets(np.array([x,y]))
    vector_a.set_UVC(-factor_aceleracion*(a/aref)*np.sin(radianes),
                     -factor_aceleracion*(a/aref)*np.cos(radianes))
    
    vector_v.set_offsets(np.array([x,y]))
    vector_v.set_UVC(-factor_v*(v/vref)*np.sin((radianes-np.pi/2)),
                     -factor_v*(v/vref)*np.cos((radianes-np.pi/2)))
                       
    patchTierra.center = (x, y)
    return patchTierra,vector_a,vector_v,patchSol,
    
def mostrar_animacion(a,v,distancia):
    
    factor_de_distancia = 5*(distancia/dref)
    anim = animation.FuncAnimation(fig, animate,
                                   fargs=(factor_de_distancia,a,v), 
                                   frames=500, 
                                   init_func=init,    
                                   interval=17,
                                   blit=True)

    return anim
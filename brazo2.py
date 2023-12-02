import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Se definen los limites que se mostrara
fig, ax = plt.subplots()
ax.set_xlim([-40,40])
ax.set_ylim([-40,40])
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")

# Se colocan los puntos y la linea
linea1, = ax.plot([],[],color="green")
punto1, = ax.plot([],[],"ro",color="blue")
punto2, = ax.plot([],[],"ro",color="black")

linea2, = ax.plot([],[],color="green")
punto3, = ax.plot([],[],"ro",color="black")

linea3, = ax.plot([],[],color="red")

# Se colocan los puntos y la linea
linea4, = ax.plot([],[],color="green")
punto4, = ax.plot([],[],"ro",color="blue")
punto5, = ax.plot([],[],"ro",color="black")

linea5, = ax.plot([],[],color="green")
punto6, = ax.plot([],[],"ro",color="black")

linea6, = ax.plot([],[],color="red")

punto_silueta, = ax.plot([],[],"ro",color="yellow")

# Se definen parametros
radio = 20
pasos = 100
ang1 = np.pi/4
ang2 = np.pi-np.pi/4
inicioX = 0
inicioY = 0

# Parametros para el caso del circulo
radio_circulo = 20
ang1_circulo = np.arcsin(radio_circulo/(2*radio))
ang2_circulo = np.pi - np.arcsin(radio_circulo/(2*radio))

def cinematicaDirecta(ang,x,y):
      
    finalX = radio*np.cos(ang) + x
    finalY = radio*np.sin(ang) + y
    return finalX,finalY,


def init():
    # Brazo 1
    linea1.set_data([],[])
    punto1.set_data([],[])
    punto2.set_data([],[])

    linea2.set_data([],[])
    punto3.set_data([],[])

    linea3.set_data([],[])

    # Brazo 2
    linea4.set_data([],[])
    punto4.set_data([],[])
    punto5.set_data([],[])

    linea5.set_data([],[])
    punto6.set_data([],[])

    linea6.set_data([],[])

    return linea1, punto1, punto2, linea2, punto3, linea3,linea4, punto4, punto5, linea5, punto6, linea6,

# Creamos la funcion que hara la figura de un circulo
def circulo(frame):
    global radio,pasos,inicioX,inicioY,ang1_circulo,ang2_circulo
    
    finalX1,finalY1=cinematicaDirecta(ang1_circulo,inicioX,inicioY)
          
    linea1.set_data([inicioX,finalX1],[inicioY,finalY1])
    punto1.set_data(inicioX,inicioY)
    punto2.set_data(finalX1,finalY1)
    
    finalX2,finalY2=cinematicaDirecta(2*np.arccos(radio_circulo/20)+ang1_circulo,finalX1,finalY1)
    linea2.set_data([finalX1,finalX2],[finalY1,finalY2])
    punto3.set_data(finalX2,finalY2)

    linea3.set_data([inicioX,finalX2],[inicioY,finalY2])

    if (ang1_circulo>-np.pi*(1/2)-np.arccos(radio_circulo/20)):
        ang1_circulo -= 0.05

    finalX3,finalY3=cinematicaDirecta(ang2_circulo,inicioX,inicioY)
          
    linea4.set_data([inicioX,finalX3],[inicioY,finalY3])
    punto4.set_data(inicioX,inicioY)
    punto5.set_data(finalX3,finalY3)
    
    finalX4,finalY4=cinematicaDirecta(ang2_circulo-2*np.arccos(radio_circulo/20),finalX3,finalY3)
    linea5.set_data([finalX3,finalX4],[finalY3,finalY4])
    punto6.set_data(finalX4,finalY4)

    linea6.set_data([inicioX,finalX4],[inicioY,finalY4])

    if (ang2_circulo<np.pi*(3/2)+np.arccos(radio_circulo/20)):
        ang2_circulo += 0.05
    
    return linea1, punto1, punto2, linea2, punto3,linea3,linea4, punto4, punto5, linea5, punto6,linea6,


def animacion(frame):
    global radio,pasos,inicioX,inicioY, ang
    
    ang += 0.2
    
    finalX1,finalY1=cinematicaDirecta(ang,inicioX,inicioY)
          
    linea1.set_data([inicioX,finalX1],[inicioY,finalY1])
    punto1.set_data(inicioX,inicioY)
    punto2.set_data(finalX1,finalY1)
    
    finalX2,finalY2=cinematicaDirecta(ang,finalX1,finalY1)
    linea2.set_data([finalX1,finalX2],[finalY1,finalY2])
    punto3.set_data(finalX2,finalY2)

    return linea1, punto1, punto2, linea2, punto3,

ani = FuncAnimation(fig,circulo,frames=np.arange(0,pasos+1,8), init_func=init,blit=True,interval=100)

plt.show()
print("Hola")
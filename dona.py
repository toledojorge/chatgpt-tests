import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Creamos una figura y un eje
fig, ax = plt.subplots()

# Creamos los datos para dibujar la donut
theta = np.linspace(0, 2 * np.pi, 100)
r = 1
x = r * np.cos(theta)
y = r * np.sin(theta)

# Dibujamos la donut en el eje
donut, = ax.plot(x, y)

# Creamos la función de animación
def animate(i):
    theta = np.linspace(0, 2 * np.pi, 100) + i / 10
    r = 1
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    donut.set_xdata(x)
    donut.set_ydata(y)

# Creamos el objeto de animación
anim = FuncAnimation(fig, animate, frames=100, interval=20)

plt.show()

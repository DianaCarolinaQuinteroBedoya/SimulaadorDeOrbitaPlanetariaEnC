# Estudiante: Diana Carolina Quintero Bedoya
# Correo: diana.quintero01@correo.usa.edu.co
# Carrera: Ciencias de la computación e Inteligencia Artificial
# Fecha:  6 Mayo 2021
# Ultima Modificación: 11 Mayo 2021 
# Docente: John Corredor Pdh
# Materia: Computación paralela y distrribuida
# Universidad Sergio Arboleda
# 
######### Test Simulador de Orbitas Planetarias ##########
#
import CySimulador as cy
import PySimulador as py
import time

def main(simulator):
    AU = (149.6e6 * 1000)
    sun = simulator.Body()
    sun.name = 'Sun'
    sun.mass = 1.98892 * 10**30
    #sun.pencolor('yellow')

    earth = simulator.Body()
    earth.name = 'Earth'
    earth.mass = 5.9742 * 10**24
    earth.px = -1*AU
    earth.vy = 29.783 * 1000            # 29.783 km/sec
    #earth.pencolor('blue')

    # Venus parameters taken from
    # http://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html
    venus = simulator.Body()
    venus.name = 'Venus'
    venus.mass = 4.8685 * 10**24
    venus.px = 0.723 * AU
    venus.vy = -35.02 * 1000
    #venus.pencolor('red')

    simulator.loop([sun, earth, venus])

if __name__ == '__main__':
        initial = time.time()
        main(py)
        tiempoPy = time.time() - initial

        initial = time.time()
        main(cy)
        tiempoCy = time.time() - initial

        SpeedUp = round(tiempoPy/tiempoCy, 3)

        print("tiempo Py: {}\n".format(tiempoPy))
        print("tiempo Cy: {}\n".format(tiempoCy))
        print("SpeedUp: {}\n".format(SpeedUp))



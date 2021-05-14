# Estudiante: Diana Carolina Quintero Bedoya
# Correo: diana.quintero01@correo.usa.edu.co
# Carrera: Ciencias de la computación e Inteligencia Artificial
# Fecha:  6 Mayo 2021
# Ultima Modificación: 11 Mayo 2021 
# Docente: John Corredor Pdh
# Materia: Computación paralela y distrribuida
# Universidad Sergio Arboleda
# 
######### Makefile Simulador de Orbitas Planetarias ##########
#
all:
		python3 setup.py build_ext --inplace

clean:
		rm -rf build *.so *_simulador.c *html

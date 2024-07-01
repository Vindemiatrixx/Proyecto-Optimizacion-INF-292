import threading
import numpy as np
import random
import multiprocessing

np.random.seed(42)
random.seed(42)

def leer_instancias(archivo):

    instancias = []
    with open(archivo, 'r') as archivo_instancias:
        lineas = archivo_instancias.readlines()

    for linea in lineas:

        linea = linea.strip()
        if linea:

            conjunto_i, conjunto_j = linea.split(';')
            
            valor_I_inf, valor_I_sup = map(int, conjunto_i.split('-'))
            valor_J_inf, valor_J_sup = map(int, conjunto_j.split('-'))

            instancias.append((valor_I_inf,valor_I_sup,valor_J_inf,valor_J_sup))
    
    return instancias


def distribucion_triangular_trabajadores(cant):

    minimo = 1
    moda = 8
    maximo = 8

    datos_W = np.random.triangular(minimo,moda,maximo,cant)
    datos_W = np.round(datos_W).astype(int)
    datos_W = np.clip(datos_W, minimo, maximo)

    return datos_W

def distribucion_triangular_tareas(cant):

    minimo = 1
    moda = 1
    maximo = 8

    datos_T = np.random.triangular(minimo,moda,maximo,cant)
    datos_T = np.round(datos_T).astype(int)
    datos_T = np.clip(datos_T, minimo, maximo)

    return datos_T

def tiempo_disp_trabajador(cant):

    return np.random.randint(30,56,size=cant)*10

def tiempo_nece_tareas(cant):

    return np.random.randint(3,40,size=cant)*10

def generacion_precioXsobrecalificacion(cant):

    valor = (np.random.randint(10000,30001,size=cant))
    return list(valor)

def generacion_costoXtiempo():

    rango_valores_costoXtiempo = [(5,10),(10,15),(15,20),(20,25),(25,30),(30,35),(35,40),(40,45)]
    
    valores = []

    for tp in rango_valores_costoXtiempo:

        valores.append(random.randint(tp[0],tp[1]))
        
    return valores

def generacion_presupuestos(cant_W, cant_T):

    valor_sup = int(cant_W*(2/3)*10000)
    valor_inf = int(cant_T*(4/5)*10000)
    return random.randint(valor_inf,valor_sup)

def generacion_costo_fijo(cant_W, cant_T):

    matrix = []

    for i in range(cant_T):
        
        valor = np.random.randint(4000,8000,size=cant_T)
        matrix.append(list(valor))
        
    return matrix

def eleccion_fn(eleccion):

    if eleccion == 1:
        archivo = "instancias_p.txt"
        tipo = "Pequeña_"
    elif eleccion == 2:
        archivo = "instancias_m.txt"
        tipo = "Mediana_"
    elif eleccion == 3:
        archivo = "instancias_g.txt"
        tipo = "Grande_"

    instancias = leer_instancias(archivo)

    string_archivo = "Instancia_"
    txt = ".txt"
    valor_i = 1

    for instancia in instancias:

        archivo = string_archivo + tipo + str(valor_i) + txt

        valor_aleatorio_trabajadores = random.randint(instancia[0], instancia[1])
        valor_aleatorio_tareas = random.randint(instancia[2], instancia[3])

        with open(archivo, 'w') as archivo:
            archivo.write(str(distribucion_triangular_trabajadores(valor_aleatorio_trabajadores)) + '\n')
            archivo.write(str(distribucion_triangular_tareas(valor_aleatorio_tareas)) + '\n')
            archivo.write(str(tiempo_disp_trabajador(valor_aleatorio_trabajadores)) + '\n')
            archivo.write(str(tiempo_nece_tareas(valor_aleatorio_tareas)) + '\n')
            archivo.write(str(generacion_costoXtiempo()) + '\n')
            archivo.write(str(generacion_costo_fijo(valor_aleatorio_trabajadores, valor_aleatorio_tareas)) + '\n')
            archivo.write(str(generacion_precioXsobrecalificacion(valor_aleatorio_tareas)) + '\n')
            archivo.write(str(generacion_presupuestos(valor_aleatorio_trabajadores, valor_aleatorio_tareas)) + '\n')

        valor_i += 1

        


##################################################

if __name__ == "__main__":

    procesos = []

    for i in range(1, 4):
        proceso = multiprocessing.Process(target=eleccion_fn, args=(i,))
        procesos.append(proceso)
        proceso.start()

    for proceso in procesos:
        proceso.join()







#MAIN:


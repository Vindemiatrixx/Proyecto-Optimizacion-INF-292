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
    elif eleccion == 2:
        archivo = "instancias_m.txt"
    elif eleccion == 3:
        archivo = "instancias_g.txt"

    instancias = leer_instancias(archivo)

    valores_costoXtiempo = []
    valores_sobrecalificacion = []
    presupuestos = []

    distribuciones_W = []
    distribuciones_T = []

    tiempos_disponible_trabajadores = []
    tiempos_necesario_tareas = []
    matrix = []

    for instancia in instancias:

        
        valor_aleatorio_trabajadores = random.randint(instancia[0], instancia[1])
        valor_aleatorio_tareas = random.randint(instancia[2], instancia[3])

        #distribucion_trabajadores = distribucion_triangular_trabajadores(valor_aleatorio_trabajadores)
        #distribuciones_W.append(distribucion_trabajadores) 
        
        #distribucion_tareas= distribucion_triangular_tareas(valor_aleatorio_tareas)
        #distribuciones_T.append(distribucion_tareas)
        
        #tiempos_disponible_trabajadores.append(tiempo_disp_trabajador(valor_aleatorio_trabajadores))
        #tiempos_necesario_tareas.append(tiempo_nece_tareas(valor_aleatorio_tareas))

        #valores_costoXtiempo.append(generacion_costoXtiempo())
        #valores_sobrecalificacion.append(generacion_precioXsobrecalificacion(valor_aleatorio_tareas))
        #presupuestos.append(generacion_presupuestos(valor_aleatorio_trabajadores,valor_aleatorio_tareas))

        #matrix.append(generacion_costo_fijo(valor_aleatorio_trabajadores, valor_aleatorio_tareas))

        print(distribucion_triangular_trabajadores(valor_aleatorio_trabajadores))
        print(distribucion_triangular_tareas(valor_aleatorio_tareas))
        print(tiempo_disp_trabajador(valor_aleatorio_trabajadores))
        print(tiempo_nece_tareas(valor_aleatorio_tareas))
        print(generacion_costoXtiempo())
        print(generacion_costo_fijo(valor_aleatorio_trabajadores,valor_aleatorio_tareas))
        print(generacion_precioXsobrecalificacion(valor_aleatorio_tareas))
        print(generacion_presupuestos(valor_aleatorio_trabajadores,valor_aleatorio_tareas))

    """  
    print (distribuciones_W)
    print(distribuciones_T)
    print(tiempos_disponible_trabajadores)
    print(tiempos_necesario_tareas)
    print(valores_costoXtiempo)
    print(valores_sobrecalificacion)
    print(valores_sobrecalificacion[0][0])
    
    print(presupuestos)
    """

    


        



while True:
    try:
        eleccion = int(input("Ingresa una opción de tamaño de instancia: \n\t1) Pequeña\n\t2) Mediana\n\t3) Grande\n\t4) Todas\n"))
        if 1 <= eleccion <= 4:
            break
    except ValueError:
            print("Ingresa un valor válido.")
    

if eleccion == 1: #Instancia pequeña
    eleccion_fn(eleccion)

elif eleccion == 2: #Instancia mediana
    eleccion_fn(eleccion)
    
elif eleccion == 3: #Instancia grande
    eleccion_fn(eleccion)

elif eleccion == 4: #Todos las instancias

    hilos = []
    eleccion = 1
    hilo1 = threading.Thread(target=eleccion_fn, args=(eleccion,))
    hilos.append(hilo1)
    hilo1.start()

    eleccion = 2
    hilo2 = threading.Thread(target=eleccion_fn, args=(eleccion,))
    hilos.append(hilo2)
    hilo2.start()

    eleccion = 3
    hilo3 = threading.Thread(target=eleccion_fn, args=(eleccion,))
    hilos.append(hilo3)
    hilo3.start()

    for hilo in hilos:
        hilo.join()







#MAIN:


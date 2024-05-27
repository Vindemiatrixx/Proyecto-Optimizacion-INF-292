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







#MAIN:


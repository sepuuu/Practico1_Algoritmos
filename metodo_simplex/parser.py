import re
import numpy as np
from tabulate import tabulate

def parser():

    # Obtener variables básicas de la función objetivo
    f_objetivo = input("Ingresa la función objetivo: ")
    f_obj = "1z + " + f_objetivo
    coef_var_list1 = re.findall("([+-]?(?:\d+(?:\.\d*)?|\.\d+))(?:([a-zA-Z]\d*))?", f_obj)

    coef_var_bas = []
    for i in coef_var_list1:
        coef_var_bas.append(i[0]) #Captura solo coeficientes
    coef_num = []
    for i in range(len(coef_var_bas)): #convertir a numeros la lista de coef_numericos
        coef_num.append(float(coef_var_bas[i]))

    coef_num = np.array(coef_num) #arreglo variables basicas(convierto a numpy array)
    coef_numericos = np.array(coef_num) #convirtiendo a array para multiplicar por  -1 (lo guardo en un arreglo para que sea como una matriz)

    #Creamos listas para tabular
    filaz = [] #filaz
    for i in coef_numericos:
        if i == 1:
            filaz.append(i)
        else:
            filaz.append(i*-1) #mutliplicamos por -1 (obtenemos la forma Z - 30000X1+50000X2)

    variables_f = [var for coef, var in coef_var_list1]


    # Obtener restricciones
    # Pedir al usuario que ingrese las restricciones

    # Obtener lista de variables básicas
    variables_basicas = list(variables_f) # orden z x1 y x2

    restricciones = []
    ladod = []


    for i in range(1): #añadiendo 0 al lado derecho antes de añadir los lados derechos de las restricciones(0 por el lado derecho de la Z)
         if i == 0:
             ladod.append(0)
         else:
             break
    # Pedimos al usuario que ingrese el número de restricciones
    num_rest = int(input("Ingresa el número de restricciones: "))

    for i in range(num_rest):
        inecuacion = input("Ingrese una inecuación (o presione Enter para finalizar): ")
        if inecuacion == '':
            break

        # Encontrar todos los valores de la inecuación
        coef_var_list = re.findall("([+-]?(?:\d+(?:\.\d*)?|\.\d+))(?:([a-zA-Z]\d*))?", inecuacion)
        # Crear lista de coeficientes de la restricción
        coeficientes_restriccion = [0] * len(variables_basicas)
        exp_ld = re.compile("[<>]=?\s*([-+]?\d*\.?\d+)")
        resultado = exp_ld.search(inecuacion)
        lado_derecho = resultado.group(1)
        ladod.append(lado_derecho)

        for coef, var in coef_var_list:
            if var in variables_basicas:
                if variables_basicas.index(var) != 0:
                    coeficientes_restriccion[variables_basicas.index(var)] = float(coef)
                elif var == 'z':
                    coeficientes_restriccion[variables_basicas.index(var)] = 0


        # Agregar lista de coeficientes a la lista de restricciones
        restricciones.append(coeficientes_restriccion)
    #CREAR ARREGLOS  DEPENDIENDO DE LA CANTIDAD DE VARIABLES DE HOLGURA

    ld = []
    for i in range(len(ladod)): #convertir a numeros la lista de coef_numericos
        ld.append(float(ladod[i]))
    ld = np.array(ld)



    variables_holgura = []
    coefs_var_holgura = []

    for i in range(num_rest): #Crear variables de holgura con respecto a el numero de restricciones
        variables_holgura.append('h'+str(i+1))
        coefs_var_holgura.append(0)

    identidad_holguras = np.identity(num_rest) #Matriz identidad para los intersectos de las variables de holgura


    fila1 = np.concatenate(([filaz],restricciones))
    bloque2 =np.concatenate(([coefs_var_holgura], identidad_holguras)) 

    # ld = [1, 1, 1, 1, 1]
    # bloque2 = [0,0,0,0,0]

    T = np.concatenate((fila1,bloque2), axis=1)
    TABLA = np.concatenate((T, np.array([ld]).T), axis=1)

    #for i in TABLA.tolist():
    #    print(i, end="")

    lado_derecho = ['LD']
    z = ['z']
    vb = ['VB']

    lado_derecho = np.array(lado_derecho)
    vb = np.array(vb)
    z = np.array(z)

    header = np.concatenate((vb, variables_basicas, variables_holgura, lado_derecho)) #lado der

    columna = np.concatenate((z, variables_holgura)) #lado izq

    TABLA = np.concatenate((np.array([columna]).T, TABLA), axis=1)

    TABLA = np.concatenate(([header], TABLA))

    return TABLA

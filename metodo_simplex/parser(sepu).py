import re

# Solicitamos el número de restricciones
num_restricciones = int(input("Ingresa el número de restricciones: "))

# Creamos una lista vacía para almacenar las restricciones
restricciones = []
cof_restriccion = []
# Solicitamos cada restricción y aplicamos expresiones regulares para extraer coeficientes y variables
for i in range(num_restricciones):
    restriccion = input("Ingresa la restricción número {}: ".format(i+1))
    restriccion = restriccion.replace('*','')
    coef_restriccion = re.findall(r'[-]?\d+x', restriccion )
    var_restriccion = re.findall(r'x\d+', restriccion)
    total_restriccion = re.findall(r'[-]?\d+', restriccion)
    total_restriccion = total_restriccion[-1]
    print('total restriccion= ', total_restriccion)
    vn = re.findall(r'\dx+', restriccion)
    #print(coef_restriccion)
    for i in range(len(coef_restriccion)):
        #print(coef_restriccion[i])
        cof_restriccion.append(str(coef_restriccion[i]).replace('x', ''))
    print(cof_restriccion)
    restricciones.append((list(map(int, cof_restriccion)), var_restriccion))

# Imprimimos las restricciones
print("Las restricciones son:")
for restriccion in restricciones:
    print(restriccion)

# tabla tiene que tener el mismo numero de variables que variables artificiales
#print('A'+str(1))
v_holgura = []
for i in range(len(var_restriccion)):
    v_holgura.append('A'+str(i+1))
print(v_holgura)

#map no funciona, ''.join(var_restriccion) junta todo el arreglo en 1 strin
#tabla = ['z', map(var_restriccion,i), map(v_holgura,i), 'total']
#print(tabla)
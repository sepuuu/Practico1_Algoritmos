import re

# Solicitamos la ecuación al usuario
ecuacion = input("Ingresa una ecuación del tipo c1 *x1+c2*x2 hasta cn*xn: ")

# Usamos expresiones regulares para encontrar los coeficientes y variables
coeficientes = re.findall(r'\d+', ecuacion)
variables = re.findall(r'x\d+', ecuacion)

# Creamos una lista de coeficientes separados
coeficientes_separados = [float(coeficientes[i]) for i in range(len(coeficientes)) if i % 2 == 0]

# Imprimimos los resultados
print("Los coeficientes son:", coeficientes_separados)
print("Las variables son:", variables)

# Solicitamos el número de restricciones
num_restricciones = int(input("Ingresa el número de restricciones: "))

# Creamos una lista vacía para almacenar las restricciones
restricciones = []

# Solicitamos cada restricción y aplicamos expresiones regulares para extraer coeficientes y variables
for i in range(num_restricciones):
    restriccion = input("Ingresa la restricción número {}: ".format(i+1))
    coef_restriccion = re.findall(r'[-]?\d+', restriccion)
    var_restriccion = re.findall(r'x\d+', restriccion)
    restricciones.append((list(map(int, coef_restriccion)), var_restriccion))

# Imprimimos las restricciones
print("Las restricciones son:")
for restriccion in restricciones:
    print(restriccion)




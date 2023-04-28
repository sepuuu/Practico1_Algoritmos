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

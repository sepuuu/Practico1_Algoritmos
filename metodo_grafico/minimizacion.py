import numpy as np
import matplotlib.pyplot as plt
import re

f_objetivo = input("Ingresa la función objetivo: ")
expregular = re.findall("([-]?\d*)?([a-zA-Z]\d*)", f_objetivo)


c_fobj = [] #coeficientes funcion objetivo
v_fobj = [] #variables de funcion objetivo
for i in expregular:
    c_fobj.append(i[0])
    v_fobj.append(i[1])

ladod = []
num_rest = int(input("Ingrese el número de restricciones:(No incluir no negatividad) "))
        # Crear lista de coeficientes de la restricción
 

restricciones = []
while True:
    inecuacion = input("Ingrese una inecuación (o presione Enter para finalizar): ")
    if not inecuacion:
        break
    coef_var_list = re.findall('([-]?\d*)?([a-zA-Z]\d*)', inecuacion)
    coef_restriccion = [0] * len(v_fobj)
    coeficientes_restriccion = [0] * len(v_fobj)

    exp_ld = re.compile("[<>]=?\s*([-+]?\d*\.?\d+)")
    resultado = exp_ld.search(inecuacion)
    lado_derecho = resultado.group(1)
    ladod.append(lado_derecho)

    for var_idx, var_f in enumerate(v_fobj):
        for coef, var in coef_var_list:
            if var == var_f:
                coef_restriccion[var_idx] = int(coef) if coef else 1
                break
    restricciones.append(coef_restriccion)

A = np.array(restricciones)
ladod = np.array(ladod)

coef_num = []
for i in range(len(ladod)): #convertir a numeros la lista de coef_numericos
    coef_num.append(int(ladod[i]))
    
coef_num = np.array(coef_num)
coef_num = coef_num.astype(float)

x1_min, x1_max = 0, max(coef_num)
x2_min, x2_max = 0, max(coef_num)

x1_vals, x2_vals = np.meshgrid(np.linspace(x1_min, x1_max, 100), np.linspace(x2_min, x2_max, 100))

z = np.zeros_like(x1_vals)
for i in range(num_rest):
    z += np.maximum(0, A[i,0]*x1_vals + A[i,1]*x2_vals - coef_num[i])
z[np.abs(z) < 1e-6] = 0
#calculo de puntos criticos
p_criticos = []

for i in range(num_rest):
    for j in range(i+1, num_rest):
        if abs(np.linalg.det(A[[i,j],:])) > 1e-6:
            x_crit = np.linalg.solve(A[[i,j],:], coef_num[[i,j]])
            if (x_crit >= [x1_min, x2_min]).all() and (x_crit <= [x1_max, x2_max]).all():
                p_criticos.append(x_crit)
print(p_criticos)
print("Puntos críticos:")
for p in p_criticos:
    print(f"x1 = {p[0]}, x2 = {p[1]}")

# Definir la función objetivo
def obj_func(x1, x2):
    return float(coef_num[0])*x1 + float(coef_num[1])*x2

# Calcular Z para cada punto crítico
print("\nValores de Z para los puntos críticos:")
for p in p_criticos:
    z_crit = obj_func(p[0], p[1])
    print(f"Z({p[0]}, {p[1]}) = {z_crit}")

#Graficar la región factible
plt.contourf(x1_vals, x2_vals, z, levels=[-1e-6, 1e-6], colors='blue')


# Agregar las restricciones en un rincón de la gráfica
text = "Restricciones:\n"
for i in range(num_rest):
    if A[i, 1] == 0:
        # Restricción vertical
        x1 = coef_num[i] / A[i, 0]
        text += f"x = {x1:.2f}\n"
    elif A[i, 0] == 0:
        # Restricción horizontal
        x2 = coef_num[i] / A[i, 1]
        text += f"y = {x2:.2f}\n"
    else:
        # Restricción diagonal
        x1 = np.linspace(x1_min, x1_max, 2)
        x2 = (coef_num[i] - A[i, 0]*x1) / A[i, 1]
        text += f"{A[i,0]:.2f}*x + {A[i,1]:.2f}*y <= {coef_num[i]:.2f}\n"
plt.text(x1_min, x2_max, text, ha='left', va='top', fontsize=10, color='k', bbox=dict(facecolor='white', edgecolor='black', pad=5))

# Graficar los puntos críticos
for p in p_criticos:
    plt.plot(p[0], p[1], 'ro')

# Graficar las restricciones
for i in range(num_rest):
    if A[i, 1] == 0:
        # Restricción vertical
        x1 = coef_num[i] / A[i, 0]
        plt.axvline(x=x1, color='k', linestyle='--')
    elif A[i, 0] == 0:
        # Restricción horizontal
        x2 = coef_num[i] / A[i, 1]
        plt.axhline(y=x2, color='k', linestyle='--')
    else:
        # Restricción diagonal
        x1_vals = np.array([0, 100])
        x2_vals = (coef_num[i] - A[i, 0]*x1_vals) / A[i, 1]
        plt.plot(x1_vals, x2_vals, color='k', linestyle='--')

# Configurar la gráfica
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(x1_min, x1_max)
plt.ylim(x2_min, x2_max)
plt.grid(True)
plt.show()
           
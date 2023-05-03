import numpy as np
from tabulate import tabulate
import parser
import maximizar

a = parser.parser()
z_original= np.array(a[1])
print("TABLA 1",tabulate(a))
#print(z_original)

#############################################################
#                   FASE 1
##########################################################

zzz= [1]
zzz = np.array(zzz)
a[1,1:] = np.concatenate((zzz, np.zeros(len(a[1])-2))) #lado izq
#estamos sumando hacia arriba
for i in range(len(a[:,1])):
     if i >0:
            a[1,2:] = a[1,2:].astype(np.float64) + a[i,2:].astype(np.float64)

#estamos poniendo menos -1
for i in range(len(a[1,:])):
    if i >0:
        if a[1,i] == '1.0':
            a[2:,i] = a[2:,i].astype(np.float64) * -1
        else:
            a[1,i] = a[1,i].astype(np.float64) * -1

print("TABLA 2",tabulate(a))

a = maximizar.maximizar(a)
print("TABLA 3",tabulate(a))
#print(z_original)
a[1] = z_original
#############################################################
#                   FASE 2
##########################################################

for i in range(len(a[1,:])):
    if i >0:
        if a[1,i].astype(np.float64) < 0:
            a[1,i] = a[1,i].astype(np.float64) * -1

print("TABLA 4",tabulate(a))


for i in range(len(a[1,:])):
    if i >1:
        if a[1,i] != '0.0':
            #print('a[1,i]',a[1,i])
            for e in range(len(a[:,i])):
                if e>0:
                    #print('a[e,i]',a[e,i])
                    if a[e,i] == '1.0':
                        hh = (a[1,i].astype(np.float64)*-1)
                        h= hh * a[e,1:].astype(np.float64)
                        a[1,1:] = a[1,1:].astype(np.float64) + h

print("TABLA FINAL",tabulate(a))

# EN LA FILA Z DONDE ALLA UN NUMERO DISTINTO DE 0 QUE NO ESTEN EN Z
# BUSCAR ATRAVEZ DE LA COLUMNA DE ESTE 
# PARA UBICAR LA FILA QUE TIENE EL 1 
# MULTIPLICARLA POR - EL VALOR EN Z 
# Y SUMARSELA A LA FUNCION OBJETIVO


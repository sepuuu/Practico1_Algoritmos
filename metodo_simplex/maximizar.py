import numpy as np
from tabulate import tabulate
import parser

##escribo el metodo simplex
#	z	x1	x2	h1	h2	h3	total	
#z	1	-30000	-50000	0	0	0	0	
#h1	0	1	0	1	0	0	4	
#h2	0	0	2	0	1	0	12	
#h3	0	3	2	0	0	1	18	

# a = np.array([["vars","z","x1","x2","h1","h2","h3","total"],
#               ["z", 1, -30000, -50000, 0, 0, 0, 0],
#               ["h1", 0,     1,      0, 1, 0, 0, 4],
#               ["h2", 0,     0,      2, 0, 1, 0, 12],
#               ["h3", 0,     3,      2, 0, 0, 1, 18]])

def maximizar(a):
    terminar=0
    while terminar < 1:
        #print("a:",a)
        lfila = a[0,:].size-1
        lcolumn = a[:,0].size

        z = np.array(a[1,1:lfila-1]) #selleciono solo la fila z 
        z = z.astype(np.float64) #el arreglo anterior esta en string, por lo cual lo convierto a int
        #print("z= ",z)
        # #El arreglo se pone en string, ya que en un arreglo los elementos deben ser iguales y predomina el string
        n_columna_pivote = int(np.amin(np.where(z == np.amin(z))))+1 #selecciono el numero mas pequeño
        #print("numero columna pivote=",n_columna_pivote) 
        columna_pivote = a[:,n_columna_pivote]
        #print("columna pivote =", columna_pivote)

        for i in range(lcolumn): # este es un ciclo para evitar que el primer valor que se selecciones no se divida por 0
            if i > 0:
                if float(a[i,lfila])!=0.0 and float(a[i,n_columna_pivote])!=0.0:
                    n = float(a[i,lfila])/float(a[i,n_columna_pivote])
                    n_fila_pivote = i
        ##print("n(filapivote)=",n)
        temp=0
        for i in range(0,lcolumn):
            if i >0:
                nc = float(a[i,n_columna_pivote])
                nt = float(a[i,lfila])
                if nc > 0 and nt > 0:
                    temp = nt/nc
                    if temp < n:
                        n_fila_pivote = i

        #print("numero fila pivote=",n_fila_pivote)
        fila_pivote = a[n_fila_pivote,:]
        #print("fila pivote =",fila_pivote)
        numero_pivote = float(a[n_fila_pivote,n_columna_pivote])
        #print("numero pivote",numero_pivote)

        a[n_fila_pivote,1:] = a[n_fila_pivote,1:].astype(np.float64)/numero_pivote
        #print("a(cambio de fila):", a)

        for i in range(lcolumn):
            if i>0 and i != n_fila_pivote:  
                temp_numero_c_pivote= float(a[i,n_columna_pivote]) #numero pivote temporal de la columna pivote 
                #ntemp - tempc-bpivot * tempf_npivot
                aa =  a[i,1:].astype(np.float64)
                aa -= temp_numero_c_pivote * a[n_fila_pivote,1:].astype(np.float64) 
                a[i,1:] = np.round(aa,3)
                #print("temp_numero_c_pivote", temp_numero_c_pivote)
                #print("fila mod:",a[i,1:])                 
        a[n_fila_pivote,0] = a[0,n_columna_pivote] 
        print("TABLA FINAL",tabulate(a))

        #hacer el ciclo while
        a = np.array(a)
        z = np.array(a[1,1::]) #selleciono solo la fila z 
        z = z.astype(np.float64) 
        if np.sum(z < 0) != 0:
            terminar=0
        else:
            terminar=1
    return a



#a = parser.parser()
#maximizar(a)
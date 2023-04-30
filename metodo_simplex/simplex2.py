import numpy as np

##escribo el metodo simplex
#	z	x1	x2	h1	h2	h3	total	
#z	1	-30000	-50000	0	0	0	0	
#h1	0	1	0	1	0	0	4	
#h2	0	0	2	0	1	0	12	
#h3	0	3	2	0	0	1	18	
a = np.array([["vars","z","x1","x2","h1","h2","h3","total"],
              ["z", 1, -30000, -50000, 0, 0, 0, 0],
              ["h1", 0,     1,      0, 1, 0, 0, 4],
              ["h2", 0,     0,      2, 0, 1, 0, 12],
              ["h3", 0,     3,      2, 0, 0, 1, 18]])

def maximizar(a):
    terminar=0
    while terminar < 1:
        print("a:",a)
        z = np.array(a[1,1::]) #selleciono solo la fila z 
        z = z.astype(np.float) #el arreglo anterior esta en string, por lo cual lo convierto a int
        print("z= ",z)           
        lfila = a[0,:].size-1
        lcolumn = a[:,0].size

        # #El arreglo se pone en string, ya que en un arreglo los elementos deben ser iguales y predomina el string
        n_columna_pivote = int(np.amin(np.where(z == np.amin(z))))+1 #selecciono el numero mas pequeño
        print("numero columna pivote=",n_columna_pivote) 
        columna_pivote = a[:,n_columna_pivote]
        print("columna pivote =", columna_pivote)

        for i in range(lcolumn): # este es un ciclo para evitar que el primer valor que se selecciones no se divida por 0
            if i > 0:
                if float(a[i,lfila])!=0.0 and float(a[i,n_columna_pivote])!=0.0:
                    n = float(a[i,lfila])/float(a[i,n_columna_pivote])
                    n_fila_pivote = i
        #print("n(filapivote)=",n)
        temp=0
        for i in range(0,lcolumn):
            if i >0:
                nc = float(a[i,n_columna_pivote])
                nt = float(a[i,lfila])
                if nc > 0 and nt > 0:
                    temp = nt/nc
                    if temp < n:
                        n_fila_pivote = i

        print("numero fila pivote=",n_fila_pivote)
        fila_pivote = a[n_fila_pivote,:]
        print("fila pivote =",fila_pivote)
        numero_pivote = float(a[n_fila_pivote,n_columna_pivote])
        print("numero pivote",numero_pivote)

        new_fila_pivote = []
        for i in range(lfila+1):
            if i > 0:
                n = float(a[n_fila_pivote,i])
                nn = n/numero_pivote
                #print("nn",nn)
                new_fila_pivote.append(nn)
            
        print("new fila pivote=",new_fila_pivote)
        #cambiamos la fila
        a[n_fila_pivote,1:] = new_fila_pivote
        print("a(cambio de fila):", a)

        arreglo_temp = []
        new_a = []
        for i in range(lcolumn):
            if i>0 and i != n_columna_pivote:  
                temp_numero_c_pivote= float(a[i,n_columna_pivote]) #numero pivote temporal de la columna pivote
                for e in range(lfila+1):
                    if e>0 :                     #lo que hago es saltarme siempre la primera, ya que corresponde a string
                        temp_numero_f_pivote = float(a[n_fila_pivote,e]) #numero pivote temporal de la fila pivote
                        numero_temp = float(a[i,e])
                        print("calculo = " , numero_temp ,temp_numero_c_pivote ,temp_numero_f_pivote)
                        new_n = numero_temp - temp_numero_c_pivote * temp_numero_f_pivote #numero nuevo temporal
                        arreglo_temp.append(new_n) # agrego el valor de los nuevos numeros aun vector para insetarlo a una matriz
                        #ntemp - tempc-bpivot * tempf_npivot
                arreglo_temp.insert(0,a[i,0])
                new_a.append(arreglo_temp)        
            elif i == n_columna_pivote:
                #arreglo_temp.append(new_fila_pivote)
                nf = new_fila_pivote
                nf.insert(0,a[0,n_columna_pivote]) #cambio el nombre de la variable de holgura por la variable
                new_a.append(nf)
            print("arreglo_temp =",arreglo_temp)
            arreglo_temp = []
        print('new_a =',new_a)
        
        new_a.insert(0,a[0,:].tolist())
        print(new_a)
        #hacer el ciclo while
        a = np.array(new_a)
        z = np.array(a[1,1::]) #selleciono solo la fila z 
        z = z.astype(np.float) 
        if np.sum(z < 0) != 0:
            terminar=0
        else:
            terminar=1

a = np.array([['vars', 'z', 'x1', 'x2', 'h1', 'h2', 'h3', 'total'],
 ['z', '1.0', '-30000.0', '0.0', '0.0', '25000.0', '0.0', '300000.0'],
 ['h1', '0.0', '1.0', '0.0', '1.0', '0.0', '0.0', '4.0'],
 ['x2', '0.0', '0.0', '1.0', '0.0', '0.5', '0.0', '6.0'],
 ['h3', '0.0', '3.0', '0.0', '0.0', '-1.0', '1.0', '6.0']])
maximizar(a)

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:15:39 2019

@author: Felipe
"""

def determinante(matriz):
    global c
    cambio=1    
    c = c+1
    for i in range(len(matriz)-1): 
        c=c+7
        for j in range(i+1, len(matriz)):
            c=c+6
            for k in range (i+1, len(matriz)):
                c=c+3
                try:
                    matriz[j][k] = float(matriz[j][k]-((matriz[j][i]*matriz[i][k])/matriz[i][i]))
                except ZeroDivisionError:
                    for m in range(j, len(matriz[j])):
                        if matriz[m][i]!=0:
                            aux=matriz[i]      
                            matriz[i]=matriz[m]
                            matriz[m]=aux
                            cambio*=-1
                            break
                    try:
                        matriz[j][k] = float(matriz[j][k]-((matriz[j][i]*matriz[i][k])/matriz[i][i]))        
                    except ZeroDivisionError:
                        for i in range (len(matriz)):
                            tot=""
                            for j in range (len(matriz)):
                                tot=tot+str(matriz[i][j])+" "
                            print(tot)
                        return "No se puede calcular el determinante por gauss"    
                    
                c+=14
    c+=1   
    det=1
    for i in range(len(matriz)):
        det=det*matriz[i][i]
    for i in range (len(matriz)):
        tot=""
        for j in range (len(matriz)):
            tot=tot+str(matriz[i][j])+" "
        print(tot)
    return det*cambio
                
n = int(input("Digite n: "))
c=0
matriz = []

for i in range (n):
    matriz.append([])
    k=[]
    for j in range (n):
        k.append(j)
    m=0
    for j in k:
        try:
            entrada = input("Inserte el valor de la fila {} y la columna {}: ".format(i+1,j+1-m))
            matriz[i].append(float(entrada))
        except (SyntaxError, ValueError):
            print("Debe insertar un numero")
            k.append(k[len(k)-1]+1)
            m=m+1

for i in range (len(matriz)):
    tot=""
    for j in range (len(matriz)):
        tot=tot+str(matriz[i][j])+" "
    print(tot)


print("")         
print("El determinante de la matriz es: "+str(determinante(matriz))+" y el numero de operaciones es: "+str(c))
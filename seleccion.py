# -*- coding: cp1252 -*-
def peorCaso(n):
    a=[]
    for k in range(n):
        a.append(n-k)
    return a
        
def mejorCaso(n):
    a=[]
    for k in range (1, n+1):
        a.append(k)
    return a

def medioCaso(n):
    a=[]
    for k in range (1, int(n/2)+1):
        a.append(k)
    for k in range(n, int(n/2), -1):
        a.append(k)
    return a

n=input("Ingrese el tamaño del vector: ")
vector=mejorCaso(n)
    
#Imprimo el vector normal
print
print(vector)
print

#Ordeno el vector
c=1
i=0
while i < n-1:
    j=i+1
    donde = i+1
    c=c+6
    while j < n:
        c+=1
        c+=3
        if vector[donde] > vector[j]:
            donde = j
            c+=1
        j=j+1
        c=c+2
    c+=1
    c+=3
    if vector[i] > vector[donde]:
        aux = vector[i]
        vector[i] = vector[donde]
        vector[donde] = aux
        c+=7
    i=i+1
    c+=2
c+=1

#Imprimo el vector ordenado
print(vector)
print("La ecuacion temporal da:  "+str(c))
print("La ecuacion temporal del peor caso por formula da:  "+str(((23*(n-1)) + 3) + 8*(n*(n-1) - (n-1) - ((n-2)*(n-1)/2))))
print("La ecuacion temporal del mejor caso por formula da:  "+str(8*(n*(n-1) - (n-1) - ((n-2)*(n-1)/2))))

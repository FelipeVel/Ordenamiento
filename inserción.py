# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:54:57 2019

@author: Felipe
"""
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

n=input("Ingrese el tamaño: ")
a=mejorCaso(n)
c=1
i=1

print("Vector original: "+str(a))

while i<n:
    j=i-1
    t=a[i]
    while j>=0 and a[j]>t:
        a[j+1]=a[j]
        j=j-1
        c=c+10
    a[j+1]=t
    i=i+1
    c=c+14
c=c+1

print("Vector ordenado: "+str(a))
print("Numero de operaciones contadas: "+str(c))
print("Peor caso segun ecuacion: "+str((((((n-1)*(n-2))/2) + (n-1))*10) + (14*(n-1)) + 2))
print("Mejor caso segun ecuacion: "+str((14*(n-1)) + 2))
print("Caso medio segun ecuacion: "+str((((((n-1)*(n-2))/2) + (n-1))*5)))
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:41:24 2019

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
    for k in range (int(n/2)):
        a.append(k)
    for k in range(n, int(n/2), -1):
        a.append(k)
    return a

def ordenar(lista):
    global c
    for i in range (len(lista)-1):
        c+=6
        for j in range(i+1, n):
            if lista[i]>lista[j]:
                t=lista[i]
                lista[i]=lista[j]
                lista[j]=t
                c+=7
            c+=5
    c+=2

c=1          
n=10   
lista=medioCaso(n)
print(lista)
ordenar(lista)
print("Lista ordenada: "+str(lista))
print("Numero de operaciones: "+str(c))
print("Peor caso con n="+str(n)+": "+str((6*n*n) - 3))
print("Mejor caso con n="+str(n)+": "+str(((5*n*n) + (7*n) - 6) / 2))
print("Caso medio con n="+str(n)+": "+str(((17*n*n) + (7*n) - 12) / 4))
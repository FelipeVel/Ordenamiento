# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:41:24 2019

@author: Felipe
"""


def ordenar(lista):
    global c
    for i in range (len(lista)-1):
        c+=6
        for j in range(i+1, n):
            if lista[i]>lista[j]:
                t=lista[i]
                lista[i]=lista[j]
                lista[j]=t
                c+=12
    c+=2

c=1             
lista=[]
n=10
for i in range(n):
    lista.append(n-i)
print(lista)
ordenar(lista)
print("Lista ordenada: "+str(lista))
print("Numero de operaciones: "+str(c))
print("Segun ecuacion: "+str((6*n*n) - 3))
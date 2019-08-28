# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:41:24 2019

@author: Felipe
"""

import random

def ordenar(lista):
    for i in range (len(lista)-1):
        for j in range(len(lista)):
            if lista[j]>lista[i]:
                t=lista[i]
                lista[i]=lista[j]
                lista[j]=t
                
lista=[]
for i in range(50):
    lista.append(random.randint(1, 50))
print(lista)
ordenar(lista)
print("Lista ordenada: "+str(lista))
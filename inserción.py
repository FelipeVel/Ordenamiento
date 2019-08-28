# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:54:57 2019

@author: Felipe
"""
def peorCaso():
    a=[]
    for k in range(6):
        a.append(6-k)
    return a
        
def mejorCaso():
    a=[]
    for k in range (7):
        a.append(k)
    return a

def casoMedio():
    a=[]
    for k in range(6, 3, -1):
        a.append(k)
    for k in range (3):
        a.append(k)
    return a

a=peorCaso()
c=1
i=1


print("Vector original: "+str(a))

while i<len(a):
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
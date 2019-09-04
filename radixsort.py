# -*- coding: utf-8 -*-
import random

class inicializar:
    def __init__(self, mat):
        self.__i = 0
        while self.__i < 10:
            mat[self.__i][0] = 1
            self.__i += 1

class recoger:
    def __init__(self, mat, vec, n):
        self.__i = 0
        self.__k = 0
        while self.__i < 10:
            self.__j = 1
            while self.__j < mat[self.__i][0]:
                vec[self.__k] = mat[self.__i][self.__j]
                self.__k += 1
                self.__j += 1
            self.__i += 1
            
print("Este programa ordena un vector por medio del")
print("Método de ordenamiento por radix sort")
print

#Pregunto la longitud del vector
longi = raw_input("Ingrese un numero entero:  ")
while longi == " " or longi.isdigit() == False or int(longi)<=0:
    longi = raw_input("Ingrese un numero entero:  ")

n=int(longi)
vector=range(n)

#Lleno el vector
for i in range(n):
    vector[i] = random.randint(0,999)

#Imprimo el vector
print
print(vector)
print

#Creo la matriz
m=[None]*10
for i in range(10):
   m[i] = [None]*(n+1)
   
temp=vector[0]
i=1
while i < n:
    if vector[i] > temp:
        temp=vector[i]
    i+=1
cont=1
control=10
while control <= temp:
    cont+=1
    control=control*10
    
inic = inicializar(m)

p=1
i=0
while i < cont:
    j=0
    while j < n:
        t = vector[j]
        t = t / p
        d = t % 10
        col = m[d][0]
        m[d][col] = vector[j]
        m[d][0] = m[d][0] + 1
        j+=1
    rec = recoger(m,vector,n)
    inic = inicializar(m)
    p=p*10
    i+=1

#Imprimo el nuevo vector
print(vector)
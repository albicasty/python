#!/usr/bin/env python
import random

def rand_list(lista):
    lista[:]=[random.randint(1,10) for i in range(0,random.randint(1,10))]


def single_list(lista):
    new=set(lista)
    lista[:]=list(new)


a=[]
b=[]
rand_list(a)
rand_list(b)
print(a)
print(b)
single_list(a)
single_list(b)
c=[el for el in a if el in b]
print(c)


#!/usr/bin/env python
def single_list(lista):
    new=[]
#    new=[i for i in lista if i not in new]
    for i in lista:
        if i not in new:
            new.append(i)
    lista[:]=list(new)


a=[1,2,3,2,1,2,3]
single_list(a)

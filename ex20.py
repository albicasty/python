#!/usr/bin/env python

import random
import sys


def generate_list():
    a=random.randint(1,20);
    l=[ random.randint(0,20)  for i in range(a)]
    l.sort()
    return l

def binary_search(n,l):
    a=len(l)//2+len(l)%2;
    print(a)
    if l[a-1]==n:
        return 1 
    elif a==1 :
        return 0
    elif n>l[a] :
        ret_val=binary_search(n,l[a-1:len(l)-1]);
    else :
        ret_val=binary_search(n,l[0:a-1])
    return ret_val
    

def insert_n():
    print "Inserisci numero da 0 a 20"
    a=raw_input()
    try:
        a=int(a);
        if  a<0 or a>20 :
            raise ValueError;
    except ValueError :
        print("errore input");
        sys.exit();
    return a

    

if __name__=="__main__":
    l=generate_list()
    n=insert_n();
    print (n,l)
    if binary_search(n,l) :
        print "number found!"
    else:
        print "number not found"


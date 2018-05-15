#!/usr/bin/env python

import string
import random
import sys

def ask_strong( ):
    print(" Password: 0 easy 1 hard. Insert your choice " );
    val=input();
    try: 
        if (val!=0 and val != 1 ):
            raise ValueError;
    except ValueError:
        print("error value as input");
        sys.exit();
    return val;


def read_dictionary():
    lista=[]
    try:
        with open("dizionario.txt","r") as f:
            for i in f:
                lista.append(i);
    except IOError:
        print "Dizionario non esiste";
        sys.exit();
    return lista;


def weak():
    lista=read_dictionary();
    val=random.choice(lista);
    return val;

def strong():
    l=random.randint(10,15);
    s=""
    p=string.digits+string.ascii_letters+string.punctuation;
    for i in range(l) :
        s+=p[random.randint(0,len(p)-1)];
    return s;

def main():
    strength=ask_strong();
    if strength == 0 :
        key=weak();
    else :
        key=strong();
    
    print key

main()






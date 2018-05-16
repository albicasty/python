#!/usr/bin/env python
import random
import sys

def gen_num( ):
    n=str(random.randint(1,9999)).zfill(4);
    return n;

def compare(a,b):
    cow=0;
    bull=0;
    match=str();
    for i in range(4):
        if (a[i]==b[i]):
            cow+=1;
            match+='1';
        else :
            match+='0';
    for i in range(4):
        if match[i]=='0' :
            flag=1;
            for l in range(4) :
                if b[i]==a[l] and l!=i and match[l]=='0' and flag :
                    bull+=1;
                    flag=0;
    print 'cow ',cow,'bull ',bull
    if cow==4:
        return 0;
    else: 
        return 1;


def input_numb():
    print('Enter a number');
    inp=raw_input();
    try:
        int(inp);
        if len(inp)!=4 :
            raise ValueError;
    except ValueError:
        print("errore input");
        sys.exit();
    return inp
    

if __name__=="__main__":
    a=gen_num();
    end=1;
    while(end) :
        value=input_numb();
        end=compare(a,value);


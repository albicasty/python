#!/usr/bin/env python



def invert(string):
    a =[ ] ;
    a=[ string[len(string)-i-1] for i in range(len(string)) ] ;
    return a ;

testring = " my name is alberto ";
split_support  = testring.split();
inv_s = invert(split_support) ;
join_support = " ".join(inv_s);
print ( join_support )

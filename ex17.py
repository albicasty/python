#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests

def parse( s ) :
    r = requests.get(s)
    return r.text



def b_soap (html ) :
    soup = BeautifulSoup(html, "lxml");
    c=soup.find_all("a",["title"])
    return c


if __name__=="__main__":
    url='https://www.gazzetta.it/'
    html= parse(url );
    out=b_soap(html);

    print out



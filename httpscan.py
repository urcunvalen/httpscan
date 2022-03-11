#!/usr/bin/python
from asyncore import read
from pdb import line_prefix
from pydoc import doc
import os
import sys

dir = "Results"
src = "urls"

try :
    os.makedirs(dir,0o777)
except OSError as e:
    if e.errno != 17:
        print("Error:", e)

if len(sys.argv) == 2:
    fic=str(sys.argv[1])
else:
    fic=src

try:
    f=open(fic,"r")
except OSError: 
    print("Erreur : le fichier ne semble pas exister.")
    sys.exit()


with f:
    lines = f.read().splitlines()
    for line in lines:
        res = line.partition("://")[2]
        bashCmd = "./shcheck/shcheck.py "+line+"> ./"+dir+"/"+res
        print("Evaluation de "+line+" en cours...", end="")
        os.system(bashCmd)
        print("OK")
f.close()
## Incluindo Servidor modelo como XML-RPC

#! usr/bin/python                      
# -*- coding: utf-8 -*-



#Modulo Persistencia
from persist import * 

###################################################################################################
#Model#
def somar(n1,n2):
    x = float(n1)
    y = float(n2)
    persistenciaArquivo(str(n1)+'+'+str(n2))
    return float(x+y)

def subtrair(n1,n2):    
    x = float(n1)
    y = float(n2)
    persistenciaArquivo(str(n1)+'-'+str(n2))
    return float(x-y)

def dividir(n1,n2):           
    x = float(n1)
    y = float(n2)
    persistenciaArquivo(str(n1)+'/'+str(n2))
    if y == 0 : return 0
    else:       return float(x/y)

def multiplicar(n1,n2):
    x = float(n1)
    y = float(n2)
    persistenciaArquivo(str(n1)+'*'+str(n2))
    return  float(x*y)

def formula(formula):
    persistenciaArquivo(formula)
    return eval(formula)



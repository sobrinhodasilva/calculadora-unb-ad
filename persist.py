#################################################################################
# Persistencia em Arquivos
import json

def persistenciaArquivo(formula,resultado):
    arquivo = open('calc.txt','ab')
    arquivo.write(formula +'=' + resultado +'\n') 
    arquivo.close()

def lerArquivo():
    try: 
        arquivo = open('calc.txt')
        linha=[]
        i=0
        for line in arquivo:
            formula,resultado = line.split ('=')
            linha.append( {'linha':i,'formula':formula,'resultado':resultado})   
            i = i+1
        return linha
        
        arquivo.close()
    except:
        print ("Erro de acesso de arquivo. Faca uma formula.")
        
def delArquivo(linha):
    try: 
        arquivo = open('calc.txt','w+')
        
        i=0
        while (i < linha):
            arquivo.readln()
            i = i+1
        #arquivo.write('')
        #arquivo.flush()
        arquivo.close()
    except:
        print ("ERRO - Verifique o numero da linha digitado")

#delArquivo(2)

#persistenciaArquivo('1+3','4')    
#    print lerArquivo()
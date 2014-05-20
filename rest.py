#!/usr/bin/env python
import web
import json

# Where the templates live:
#render = web.template.render('templates/')
render = web.template.render('templates/', cache=False)

from persist import * 


urls = (
    '/arquivo/(.*)/(.*)', 'arquivo',
    '/calc/formula/(.*)', 'get_formula',
    '/calc/soma/(.*)/(.*)', 'get_soma',
    '/calc/subtrai/(.*)/(.*)', 'get_subtrai',
    '/calc/multiplica/(.*)/(.*)', 'get_multiplica',
    '/calc/dividi/(.*)/(.*)', 'get_dividi',
    '/calc/arquivo/','arquivo'
    
)

class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('127.0.0.1', port))



class list_operacoes:        
    def GET(self):
        return str("operacoes")
    
class get_soma:
    def GET(self,n1,n2):
        x = float(n1)
        y = float(n2)
        web.header('Content-Type', 'application/json')
        resultado =  {'resultado':float(x+y)}
        return json.dumps(resultado)

class get_subtrai:
    def GET(self,n1,n2):
        x = float(n1)
        y = float(n2)
        web.header('Content-Type', 'application/json')
        resultado =  {'resultado':float(x-y)}
        return json.dumps(resultado)
class get_multiplica:
    def GET(self,n1,n2):
        x = float(n1)
        y = float(n2)
        web.header('Content-Type', 'application/json')
        resultado =  {'resultado':float(x*y)}
        return json.dumps(resultado)
class get_dividi:
    def GET(self,n1,n2):
        x = float(n1)
        y = float(n2)
        web.header('Content-Type', 'application/json')
        resultado =  {'resultado':float(x/y)}
        return json.dumps(resultado)    
        
class get_formula:    
    def GET(self, formula):    
       
        pyDict = {'resultado':eval(formula)}
        web.header('Content-Type', 'application/json')
        return json.dumps(pyDict)
    
class arquivo:
    def GET(self):
        text = {'formula': '1+3', 'resultado': '4\n', 'linha': 0}, {'formula': '1+3', 'resultado': '4\n', 'linha': 1}, {'formula': '1+3', 'resultado': '4\n', 'linha': 2}, {'formula': '1+3', 'resultado': '4\n', 'linha': 3}, {'formula': '1+3', 'resultado': '4\n', 'linha': 4}
        web.header('Content-Type', 'application/json')
        return json.dumps(text)
 
    def POST(self,formula,resultado):
        persistenciaArquivo(formula,resultado)
        return 0
          
        
        
if __name__ == '__main__':
    app = MyApplication(urls, globals())
    app.run()

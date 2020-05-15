class Capitulo:
    __titulo=''
    __cantPag=0
    def __init__(self,titulo,cantPag):
       self.__titulo=titulo
       self.__cantPag=int(cantPag)
    def getTituloc(self):
        return self.__titulo
    def getPag(self):
        return self.__cantPag
   
    
    


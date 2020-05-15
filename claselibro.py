from clasecapitulo import Capitulo

class Libro:
    __idLibro=0
    __titulo=''
    __autor=''
    __editorial=''
    __isbn=0
    __cantCap=0
    __capitulo=[]
    def __init__(self,idl,tit,aut,edi,isbn,cap):
        self.__idLibro=int(idl)
        self.__titulo=tit
        self.__autor=aut
        self.__editorial=edi
        self.__isbn=int(isbn)
        self.__cantCap=int(cap)
        self.__capitulo=[]
    def agregarCap(self,capitulo):
        if(type(capitulo)==Capitulo):
            self.__capitulo.append(capitulo)
        else:
            print('ERROR AL AGREGAR CAPITULO')
    def mostrarC(self):
        for i in range (self.__cantCap):
            print(self.__capitulo[i].getTituloc())
    def TotalPag(self):
        total=0
        for i in range (self.__cantCap):
            total+=self.__capitulo[i].getPag()
        return total    
    def getId(self):
        return self.__idLibro
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getEditorial(self):
        return self.__editorial
    def getCant(self):
        return self.__cantCap
    def __str__(self):
        s='Id Libro {}'.format(self.__idLibro)
        s+='Titulo {}'.format(self.__titulo)
        s+='Autor {}'.format(self.__autor)
        s+='Editorial {}'.format(self.__editorial)
        return s
    def buscarP(self,palabra):
        i=0
        band=False
        while not band and (i<len(self.__capitulo)):
            cap=str(self.__capitulo[i].getTituloc())
            c=cap.split()
            j=0
            while(j<len(c))and(band==False):
             if(c[j]==palabra):
                band=True
             else:
                j=j+1
             i=i+1
        if(band):
            return True
        else:
            return False
            
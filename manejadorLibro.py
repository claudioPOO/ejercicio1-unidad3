from claselibro import Libro
from clasecapitulo import Capitulo
import csv

class ManejaLibros:
    __libro=[]
    def __init(self):
        self.__libro=[]
    def cargarDatos(self):
        arc=open('Libros.csv')
        reader=csv.reader(arc,delimiter=',')
        aux=-1
        for fila in reader:
            if(len(fila)==6):
                Unlibro=Libro(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
                self.__libro.append(Unlibro)
                aux+=1
            else:
                if(len(fila)==2):
                    Uncapitulo=Capitulo(fila[0],fila[1])
                    self.__libro[aux].agregarCap(Uncapitulo)
        arc.close()
    def buscarId(self,ide):
            i=0
            band=0
            while (band==0)and(i<len(self.__libro)):
                if(ide==self.__libro[i].getId()):
                    band=1
                else:
                    i=i+1
            if(band==0):
                return False
            else:
                return i+1
            
    def mostrarD(self,j):
             print('TITULO')
             print(self.__libro[j].getTitulo())
             print('Capitulos')
             print(self.__libro[j].mostrarC())
             print('Total de paginas')
             print(self.__libro[j].TotalPag()) 
    def buscaPalabra(self,palabra):
        bandera=False
        i=0
        while not bandera and (i<len(self.__libro)):
            libro=self.__libro[i].getTitulo()
            lil=libro.split()
            j=0
            while(j<len(lil)and bandera==False):
                if(lil[j]==palabra):
                    bandera=True
                else:
                    j=j+1
            if not bandera:
                cap=self.__libro[i].buscarP(palabra)
                if cap==True:
                    bandera=True
                else:
                    i=i+1
        if bandera:
            return i+1            
        else:
            return False
        
    def mostrarTyA(self,i):
        print('LIBRO')
        print(self.__libro[i].getTitulo())
        print('Autor')
        print(self.__libro[i].getAutor())
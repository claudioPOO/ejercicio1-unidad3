import  os
class Menu :
    __switcher = None
    def  __init__ ( self ):
        self.__switcher  = { 1 : self.opcion1 ,
                            2 : self. opcion2 ,
                            3 : self . salir
                         }
    def  getSwitcher ( self ):
        return self. __switcher
    def  opcion ( self , op , libros ):
        func = self . __switcher . get ( op , lambda : print ( "Opción no válida" ))
        func ( libros )
    def  salir ( self,libros):
        print ( 'Salir' )
    def  opcion1 (self, libros ):
        band = 0
        while band ==0 :
            iden =  int ( input ( 'Ingrese el id del libro:' ))
            os.system( 'cls' )
            aux=libros.buscarId(iden)
            if(aux==False):
                print('ERROR ID NO ENCONTRAOD INGRESE NUEVAMENTE')
            else:
               libros.mostrarD(aux-1)
               band=1
    def  opcion2 ( self , libros ):
        palabra  =  input ( 'Ingrese una palabra:' )
        p=libros.buscaPalabra(palabra)
        if(p==False):
            print('No se encuentra la palabra')
        else:
            if(p>=0):
                print(libros.mostrarTyA(p-1))
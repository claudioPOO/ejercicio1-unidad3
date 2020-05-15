import os

from manejadorLibro import ManejaLibros

from claseMenu import Menu

if __name__ == '__main__':
    libros = ManejaLibros()
    libros.cargarDatos()

    menu = Menu()
    salir = False
    while not salir:
        print("\n------------Menu------------\n1. Inciso 1\n2. Inciso 2\n3. Salir")
        op = int(input('Ingrese una opcion: '))
        os.system('cls')
        menu.opcion(op, libros)
        salir = op == 3
    

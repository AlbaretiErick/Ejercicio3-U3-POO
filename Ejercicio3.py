from Manejadores import ManejadorPersonas
from Manejadores import ManejadorTalleres
from Manejadores import ManejadorInscripciones
from Manejadores import Menu
if __name__ == '__main__':
    mPersonas = ManejadorPersonas()
    mTalleres = ManejadorTalleres()
    mInscripciones = ManejadorInscripciones()
    menu = Menu()
    fin = False
    while fin == False:
        opcion = input ('Seleccione:\n1 - Cargar los datos de los talleres.\n2 - Inscribir una persona en un taller.\n3 - Consultar inscripción.\n4 - Consultar inscriptos.\n5 - Registrar pago.\n6 - Guardar inscripciones.\n7 - Salir del programa.\nOpcion: ')
        fin = menu.opcion (opcion, mPersonas, mTalleres, mInscripciones)
        print ('')
import csv
import numpy as np
from Clases import Persona
from Clases import TallerCapacitacion
from Clases import Inscripcion
class ManejadorPersonas:
    def __init__ (self):
        self.__personas = []
    def agregarPersona (self, persona):
        self.__personas.append (persona)

class ManejadorTalleres:
    __cantidad = 0
    __dimension = 1
    __incremento = 1
    __talleres = None
    def __init__ (self, dimension=1, incremento=1):
        self.__talleres = np.empty (dimension, dtype=TallerCapacitacion)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
    def agregarTaller (self, taller):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__talleres.resize (self.__dimension)
        self.__talleres[self.__cantidad] = taller
        self.__cantidad += 1
    def testTalleres (self):
        bul = False
        archivo = open ('Talleres.csv')
        reader = csv.reader (archivo, delimiter=';')
        for datos in reader:
            if bul == True:
                taller = TallerCapacitacion (datos[0], datos[1], datos[2], datos[3])
                self.agregarTaller (taller)
            bul = True
        archivo.close()
        print ('Datos cargados con exito.')
    def inciso2 (self, mP, mI, nombT):
        i = 0
        while i<len (self.__talleres) and nombT!=self.__talleres[i].getNombre():
            i += 1
        if i<len (self.__talleres):
            print ('Ingrese nombre, direccion, DNI y fecha de inscripcion:')
            nomb = input ('')
            direc = input ('')
            dni = input ('')
            fecha = input ('')
            persona = Persona (nomb, direc, dni)
            mP.agregarPersona (persona)
            inscripcion = self.__talleres[i].inscribirPersona (persona, fecha)
            mI.agregarInscripcion (inscripcion)
        else:
            print ('No se encontro el taller solicitado.')
    def inciso4 (self, id):
        i = 0
        while i<len (self.__talleres) and self.__talleres[i].getId()!=id:
            i += 1
        if i<len (self.__talleres):
            self.__talleres[i].listarPersonas()
        else:
            print ('No se encontro el taller especificado.')
    def inciso5 (self, mI, dni):
        bul = False
        i = 0
        while i<len (self.__talleres) and bul!=True:
            bul = self.__talleres[i].verInscripcion (dni)
            i += 1
        mI.buscarPersona (dni)
        if i<len (self.__talleres):
            print ('El cambio se realizo con exito, la persona de DNI {} no debe pagar.'.format (dni))
        else:
            print ('No se encontro una persona con el DNI facilitado.')

class ManejadorInscripciones:
    __cantidad = 0
    __dimension = 1
    __incremento = 1
    __inscripciones = None
    def __init__ (self, dimension=1, incremento=1):
        self.__inscripciones = np.empty (dimension, dtype=Inscripcion)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
    def agregarInscripcion (self, inscripcion):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__inscripciones.resize (self.__dimension)
        self.__inscripciones[self.__cantidad] = inscripcion
        self.__cantidad += 1
    def inciso3 (self, dni):
        bul = False
        i = 0
        while i<len (self.__inscripciones) and bul!=True:
            bul = self.__inscripciones[i].buscarDni(dni)
            i += 1
        if i<len (self.__inscripciones):
            self.__inscripciones[i].mostrar3()
        else:
            print ('No se encontro una persona con el DNI especificado.')
    def buscarPersona (self, dni):
        bul = False
        i = 0
        while i<len (self.__inscripciones) and bul!=True:
            bul = self.__inscripciones[i].modificarPago (dni)
            i += 1
    def guardarDatos (self):
        archivo = open ('Inscripciones.csv', '+w')
        writer = csv.writer (archivo, delimiter=';')
        for inscripcion in self.__inscripciones:
            lista = inscripcion.extraerDatos()
            writer.writerow (lista)
        archivo.close()
        print ('Guardado exitoso.')

class Menu:
    __switcher = None
    def __init__ (self):
        self.__switcher = {'1': self.opcion1,
                           '2': self.opcion2,
                           '3': self.opcion3,
                           '4': self.opcion4,
                           '5': self.opcion5,
                           '6': self.opcion6}
    def opcion (self, op, mP, mT, mI):
        bul = False
        funcion = self.__switcher.get (op)
        if op=='1' or op=='2' or op=='3' or op=='4' or op=='5' or op=='6':
            funcion (mP, mT, mI)
        else:
            bul = True
            print ('Fin del Programa...')
        return bul
    def opcion1 (self, mP, mT, mI):
        mT.testTalleres()
    def opcion2 (self, mP, mT, mI):
        taller = input ('Ingrese taller al que desea inscribir: ')
        mT.inciso2 (mP, mI, taller)
    def opcion3 (self, mP, mT, mI):
        dni = input ('Ingrese DNI de una persona: ')
        mI.inciso3 (dni)
    def opcion4 (self, mP, mT, mI):
        id = input ('Ingrese el identificador de un taller: ')
        mT.inciso4 (id)
    def opcion5 (self, mP, mT, mI):
        dni = input ('Ingrese DNI de la persona que pagara: ')
        mT.inciso5 (mI, dni)
    def opcion6 (self, mP, mT, mI):
        mI.guardarDatos()
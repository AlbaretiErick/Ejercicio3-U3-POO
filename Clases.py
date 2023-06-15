class Persona:
    __nombre = None
    __direccion = None
    __dni = None
    def __init__ (self, nombre, direccion, dni):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni
    def getNombre (self):
        return self.__nombre
    def getDireccion (self):
        return self.__direccion
    def getDni (self):
        return self.__dni

class TallerCapacitacion:
    __idTaller = None
    __nombre = None
    __vacantes = None
    __montoInscripcion = None
    __inscripciones = list
    def __init__ (self, id, nomb, vacantes, monto):
        self.__idTaller = id
        self.__nombre = nomb
        self.__vacantes = int (vacantes)
        self.__montoInscripcion = monto
        self.__inscripciones = []
    def getId (self):
        return self.__idTaller
    def getNombre (self):
        return self.__nombre
    def getVacantes (self):
        return self.__vacantes
    def getMonto (self):
        return self.__montoInscripcion
    def inscribirPersona (self, persona, fecha):
        inscripcion = Inscripcion (persona, self, fecha)
        self.__inscripciones.append (inscripcion)
        self.__vacantes -= 1
        return inscripcion
    def listarPersonas (self):
        for inscripcion in self.__inscripciones:
            inscripcion.mostrarPersona()
    def verInscripcion (self, dni):
        bul = False
        i = 0
        while i<len (self.__inscripciones) and bul!=True:
            bul = self.__inscripciones[i].modificarPago (dni)
            i += 1
        return bul

class Inscripcion:
    __fechaInscripcion = None
    __pago = False
    __persona = object
    __taller = object
    def __init__ (self, persona, taller, fecha, pago=False):
        self.__fechaInscripcion = fecha
        self.__pago = pago
        self.__persona = persona
        self.__taller = taller
    def getFecha (self):
        return self.__fechaInscripcion
    def getPago (self):
        return self.__pago
    def buscarDni (self, dni):
        if self.__persona.getDni() == dni:
            bul = True
        else:
            bul =  False
        return bul
    def mostrar3 (self):
        print ('Taller en el que se encuentra: {} / Adeuda: ${}'.format (self.__taller.getNombre(), self.__taller.getMonto()))
    def mostrarPersona (self):
        print ('Nombre: {}\nDireccion: {}\nDNI: {}\n'.format (self.__persona.getNombre(), self.__persona.getDireccion(), self.__persona.getDni()))
    def modificarPago (self, dni):
        if dni == self.__persona.getDni():
            self.__pago = True
        return self.__pago
    def extraerDatos (self):
        lista = [self.__persona.getDni(), self.__taller.getId(), self.__fechaInscripcion, self.__pago]
        return lista
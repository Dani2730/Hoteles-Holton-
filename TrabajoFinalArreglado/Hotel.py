from datetime import date
import numpy as np
import random
<<<<<<< HEAD
from Habitacion import Habitacion
=======
#from cadena import Cadena
from Habitación import Habitación
>>>>>>> leoMasJona


MAXIMODEPERSONAS = 4

class Hotel:
    def __init__(self, ciudad:str, nombre:str, tipoDeHotel:str, pisos:int, habitacionesPorPiso:int, zona: str):
        # Verificar que el número de pisos sea válido (6, 9, 12, o 15)
        if pisos in (6, 9, 12, 15):
            # Verificar que la cantidad de habitaciones por piso sea menor o igual al número de pisos
            if habitacionesPorPiso <= pisos:
                self.nombre = nombre
                self.tipoDeHotel = tipoDeHotel
                self.ciudad = ciudad
                self.pisos = pisos
                self.habitacionesPorPiso = habitacionesPorPiso
                self.habitaciones = np.full((pisos, habitacionesPorPiso), None)  # Matriz para almacenar las habitaciones
                self.cantidadTotalDeHabitaciones = pisos * habitacionesPorPiso
                self.zona = zona
<<<<<<< HEAD

    def CrearHabitaciones(self):
    # Inicializar las habitaciones del hotel
        for piso in range(self.pisos):
            for numeroDeHabitacion in range(self.habitacionesPorPiso):
=======
                


    def CrearHabitaciones(self, habita: Habitación):
    # Inicializar las habitaciones del hotel
        for piso in range(self.pisos):
            for numeroDeHabitacion in self.habitacionesPorPiso:
>>>>>>> leoMasJona
                estado = 'Libre'
                numero = numeroDeHabitacion + 1
                piso = f"Piso {piso + 1}"
                # Crear una instancia de Habitación y asignarla a la matriz de habitaciones del hotel
<<<<<<< HEAD
                self.habitaciones[piso][numeroDeHabitacion] = Habitacion(estado, numero, self.zona, MAXIMODEPERSONAS)
=======
                self.habitaciones[piso][numeroDeHabitacion] = habita

>>>>>>> leoMasJona


    def mostrarHotel(self):
        pass
    
<<<<<<< HEAD
    def RecomendarHabitacion(self, cantidadHuespedes, piso) -> int:
        habitacionesDisponibles = []
        for pisoActual in range(self.pisos):
            for habitacion in self.habitaciones[pisoActual]:
                if habitacion is not None:
                    # Verificar si la habitación cumple con los criterios para ser recomendada
                    if habitacion.estado == 'Libre' and habitacion.maximoPersonasHabitacion >= cantidadHuespedes and habitacion.piso == pisoActual:
                        habitacionesDisponibles.append(habitacion)
=======
    def RecomendarHabitación(self, cantidadHuespedes, piso) -> int:
        habitacionesDisponibles = []
        for pisoActual in range(self.pisos):
            for habitacion in self.habitaciones[pisoActual]:
                # Verificar si la habitación cumple con los criterios para ser recomendada
                if habitacion.estado == 'Libre' and habitacion.maximoPersonasHabitacion >= cantidadHuespedes and habitacion.piso == pisoActual:
                    habitacionesDisponibles.append(habitacion)
>>>>>>> leoMasJona
        if habitacionesDisponibles:
            # Si se encontraron habitaciones disponibles, elige una al azar
            habitacionRecomendada = random.choice(habitacionesDisponibles)
            return habitacionRecomendada
        else:
            return None


<<<<<<< HEAD

#    
#    def AsignarHabitacion(self ) ->bool:
#        pass
#    
#    
#    def Aceder_A_DatosHuespedesDeUnaHabitaciòn(self)-> bool:
#        pass
#
#    def RegistrarSalidaDeHuespedes(self) ->bool:
#        pass
#
#
#
#    def CalcularMonto_A_PagarHuspedesDeUnaHabitaciòn(self) ->float:
#        pass
#    
#    def EstablecerHabitacionComoNoDisponible(self) -> bool:
#        pass
#            
#
#    def CalcularIngresosObtenidos(self):
#        pass
#
#    def CalcularCantidadDeHuespedesAtendidos(self) -> int:
#        pass
#
#    def CalcularCantidadDeHabitacionesOcupadas(self) -> int:
#        pass
#
#    def DeterminarZonaConMayorAfluencia(self) -> str:
#        pass
#
#    def CalcularTasaDeOcupaciòn(self) -> float:
#        pass
#
#    def CalcularCantidadDeHombresYMujeresAtendidos(self) -> int:
#        pass
=======
    
    def AsignarHabitación(self ) ->bool:
        pass
    
    
    def Aceder_A_DatosHuespedesDeUnaHabitaciòn(self)-> bool:
        pass

    def RegistrarSalidaDeHuespedes(self) ->bool:
        pass



    def CalcularMonto_A_PagarHuspedesDeUnaHabitaciòn(self) ->float:
        pass
    
    def EstablecerHabitaciónComoNoDisponible(self) -> bool:
        pass
            

    def CalcularIngresosObtenidos(self):
        pass

    def CalcularCantidadDeHuespedesAtendidos(self) -> int:
        pass

    def CalcularCantidadDeHabitacionesOcupadas(self) -> int:
        pass

    def DeterminarZonaConMayorAfluencia(self) -> str:
        pass

    def CalcularTasaDeOcupaciòn(self) -> float:
        pass

    def CalcularCantidadDeHombresYMujeresAtendidos(self) -> int:
        pass
>>>>>>> leoMasJona

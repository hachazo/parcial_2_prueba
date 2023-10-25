# Desarrolle un sistema para la ciudad de Comodoro Rivadavia que gestione los datos
# de estaciones meteorológicas ubicadas en el aeropuerto, el puerto y la universidad.
# A estas estaciones se necesita poder incorporar sensores, y de forma transparente
# (sin necesidad de saber que sensores componen la estación) poner en modo de
# ahorro de energía a todos los sensores que componen la estación o grupo de
# estaciones.
# Cada sensor también debe poder disponibilizar su última medición y poder medir.
# Por último, se tiene un Panel de control que es notificado por cada medición de los
# sensores a los que está suscrito y este se encarga de mostrar por pantalla el valor
# medido.
# Para probar el sistema, cree una estación general y las tres ya mencionadas. Cada
# una de las estaciones incorpora al menos un sensor. Instancie el panel de control y
# realice la suscripción a los sensores que desee para poder ver por consola los
# valores sensados.

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from random import randint

class Component(ABC):
    def __init__(self,name) -> None:
        self._name = name

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_estacion(self) -> bool:
        return False
    
    def is_sensor(self) -> bool:
        return False
    
    def ahorro_energia(self) -> bool:
        return False
    
    @abstractmethod
    def print(self):
        pass

    # @abstractmethod
    # def crear(self) -> bool:
    #     pass

class sensor(Component):
    def __init__(self,name):
        self._name = name
        self._ultima_medicion = 0

    def print(self) -> str:
        return self._name
    
    def crear(self) -> bool:
        return super().crear()
    
    def ultima_medicion(self) -> int:
        return self._ultima_medicion

    def medir(self) -> int:
        self._ultima_medicion = randint(0, 100)
        return self._ultima_medicion

    def ahorro_energia(self) -> bool:
        return super().ahorro_energia()
 
class Estacion(Component):

    def __init__(self, name) -> None:
        self._name = name
        self._children: List[Component] = []
        
    def add(self, component: Component) -> None:
        self._children.append(component)
    
    def remove(self, component: Component) -> None:
        self._children.remove(component)
    
    def is_sensor(self) -> bool:
        return True

    def print(self) -> str:
        result = self._name
        for child in self._children:
            result += "\t" + child.print()
            result += "\n"
        return result

    def ahorro_energia(self) -> bool: ######
        self._children.ahorro_energia() #######
        
def cliente_sensor(component: Component):
    print(component.print())

def client_sensor_estacion(component: Component, component2: Component):
    if component.is_estacion():
        component.add(component2)
    print(component.print())

estacion_general = Estacion("Estacion General")
estacion_aeropuerto = Estacion("Estacion Aeropuerto")
estacion_puerto = Estacion("Estacion Puerto")
estacion_universidad = Estacion("Estacion Universidad")

sensor_aeropuerto = sensor("Sensor Aeropuerto")
sensor_puerto = sensor("Sensor Puerto")
sensor_universidad = sensor("Sensor Universidad")

estacion_aeropuerto.add(sensor_aeropuerto)
estacion_puerto.add(sensor_puerto)

estacion_general.add(estacion_aeropuerto)
estacion_general.add(estacion_puerto)
cliente_sensor(estacion_general)

# estacion_aeropuerto.add(sensor_aeropuerto)
# estacion_puerto.add(sensor_puerto)
# estacion_universidad.add(sensor_universidad)

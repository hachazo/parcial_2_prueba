import random
from composite import *

class Sensor(File):
    def __init__(self,name):
        super().__init__(name)
        self._ultima_medicion = 0
        self._ahorro_energia = False

    def ahorroenergia(self) -> None:
        return self._ahorro_energia
    
    def setahorroenergia(self, ahorro: bool) -> None:
        self._ahorro_energia = ahorro

    def medir(self) -> None:
        return random.randint(0, 100)
    
    def ultimamedicion(self) -> None:
        return self._ultima_medicion
    
class Estacion(Folder):
    def __init__(self,name):
        super().__init__(name)

    def ahorroenergia(self,energia) -> None:
        for child in self._children:
            child.setahorroenergia(energia)

sensor1 = Sensor("sensor 1")
estacion1 = Estacion("Estacion central")
estacion1.add(sensor1)

client_code(estacion1)


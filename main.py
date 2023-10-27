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
from composite  import *
import random

class Sensor(File):
    def __init__(self, name) -> None:
        super().__init__(name)
        self._medicion = 0
        self.energia = False
    
    def mostrar(self) -> str:
        return self._name

    def ultimamedicion(self) -> int:
        return self._medicion
    
    def medir(self) -> int:
        self._medicion = random.randint(0,100)
        return self._medicion
    
    def setahorroenergia(self,energia) -> bool:
        self.energia = energia
    
    def getahorroenergia(self) -> bool:
        return self.energia
    
class Estacion(Folder):
    def __init__(self, name) -> None:
        super().__init__(name)
    

sensor1 = Sensor("sensor1")
sensor2 = Sensor("sensor2")
print(sensor1.getahorroenergia())
estacion1 = Estacion("estacion1")
estacion1.add(sensor1)

client_code(estacion1)

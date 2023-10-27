# Permite definir un mecanismo de suscripcion para notificar a multiples objetos
# de un evento que ocurra sobre el objeto que estan observando.

# Ejemplo: subscribirse a un canal de youtube que 
# este se encarge de noficarte cuando suba un video nuevo.

from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Subject(ABC): # Metodos que tendra el objeto observable 
    @abstractmethod
    def attach(self, observer: Observer) -> None: # agregar un subscritor

        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None: # quitar un subscritor

        pass

    @abstractmethod
    def notify(self) -> None: # notificar a los subscritores
        pass

class Observer(ABC): # Metodos que tendra el objeto observador ( en este caso el subscritor)

    @abstractmethod
    def update(self, subject: Subject) -> None: # actualizar su estado cuando el objeto observable cambie su estado.
        pass
from abc import ABC, abstractmethod
import Interaction
import CLI

class Observer(ABC):
     @abstractmethod
     def update(self, mesagem: str):
          pass

class MenuIA:
     def __init__(self):
          self._observers = ["Cliente"]

     def nova_mensagem(self, text: str):
          mensagem = f"[Sistema] Nova mensagem para {self._observers[0]}: {Interaction.Context().ask(text)}"
          self.notify(mensagem)

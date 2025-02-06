from abc import ABC, abstractmethod
import Interaction
import Observer
import LLMs

class CLI(ABC):
     @abstractmethod
     def execute():
          pass

class ModelCLI:
     def ask(self, text: str):
          Observer.MenuIA().nova_mensagem(text)
     
     def switch(self, model: str):
          if model == "gemini":
               return LLMs.LLMsFactory.call("gemini")
          elif model == "openai":
               return LLMs.LLMsFactory.call("openai")
          else:
               raise ValueError("Não existe essa LLM em nosso sistema!\n")
     
     def exit(self):
          exit(0)

class InputCLI(CLI):
     def __init__(self, model: ModelCLI):
          self.model = model
     
     def execute(self):
          cli_input = input("Digite algo: ")
          self.model.ask(cli_input)

class SwitchCLI(CLI):
     def __init__(self, model: ModelCLI):
          self.model = model
     
     def execute(self):
          model = input("Digite o modelo: ").strip().lower()
          self.model.switch(model)

class HelpCLI(CLI):
     def execute(self):
          print("Comandos:")
          print("1: input - Para digitar algo")
          print("2: switch - Para mudar o modelo")
          print("3: help - Para ver os comandos")
          print("4: exit - Para sair")

class ExitCLI(CLI):
     def __init__(self, model: ModelCLI):
          self.model = model

     def execute(self):
          self.model.exit()

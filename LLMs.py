from google import genai
from openai import OpenAI
import os
from dotenv import load_dotenv
from abc import ABC, abstractmethod

load_dotenv()

class LLM(ABC):
     @abstractmethod
     def create():
          pass

class Gemini(LLM):
     def create():
          return genai.Client(api_key=os.getenv("GEMINI_KEY"))
     
class OpenAI(LLM):
     def create():
          return OpenAI(api_key=os.getenv("GPT_KEY"))

class LLMsFactory:
     @staticmethod
     def call(tipo: str):
          if tipo == "gemini":
               return Gemini.create()
          elif tipo == "openai":
               return OpenAI.create()
          else:
               raise ValueError("Não existe essa LLM em nosso sistema!\n")
          
          
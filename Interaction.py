from google import genai
from openai import OpenAI
from abc import ABC, abstractmethod
import LLMs

class LLMsOpetarions(ABC):
     @abstractmethod
     def response():
          pass

class GeminiInteract(LLMsOpetarions):
     def response(self, text: str):
          gemini = LLMs.Gemini
          response = "Gemini: " + gemini.models.generate_content(
          model="gemini-2.0-flash",
          contents=f"{text}"
          )
          return response.text

class OpenAIInteract(LLMsOpetarions):
     def response(self, text: str):
          openai = LLMs.OpenAI
          response = "ChatGPT: " + openai.chat.completions.create(
          model="gpt-4o-mini",
          messages=[
               {"role": "user", "content": f"{text}"}
          ]
          )
          return response.choices[0].message.content
     
class Context:
     def __init__(self, strategy: LLMsOpetarions):
          self._strategy = strategy
          
     def ask(self, text: str):
          self._strategy.response(text)
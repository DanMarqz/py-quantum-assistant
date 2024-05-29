import os
import typer
import google.generativeai as genai

from rich import print
from rich.prompt import Prompt
from rich.table import Table

# ~~~~~ LOAD ENVIRONMENT VARIABLES ~~~~~ #
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

# ~~~~~ END OF LOAD ENVIRONMENT VARIABLES ~~~~~ #

genai.configure(
  api_key = GEMINI_API_KEY
)

def main():
  
  print("💬 [bold green]Quantum AI Assistant ~ AI Generative with Gemini ♊[/bold green]")

  table = Table("[bold yellow]⚠️ Información[/bold yellow]")
  table.add_row("[yellow]Quantum AI Assistant es un agente desarrollado con Gemini by Google[/yellow]")
  table.add_row("[yellow]Para salir del agente escriba 'exit'[/yellow]")
  print(table)
  
  model = genai.GenerativeModel(
    GEMINI_MODEL
  )
  
  while True:
    content = __prompt()

    response = model.generate_content(
      content
    )

    print(f"[bold aquamarine1]> [/bold aquamarine1] [aquamarine1]{response.text}[/aquamarine1]")
  
def __prompt() -> str:
  prompt = Prompt.ask("\n[bold thistle1]¿Qué quieres consultarle a Quantum? [/bold thistle1]")

  if prompt == "exit":
    exit = typer.confirm("✋ ¿Estás seguro?")
    if exit:
      print("👋 ¡Hasta luego!")
      raise typer.Abort()

    return __prompt()

  return prompt

if __name__ == "__main__":
  typer.run(main)
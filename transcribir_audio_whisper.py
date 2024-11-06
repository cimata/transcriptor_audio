# -*- coding: utf-8 -*-
"""Transcribir_audio_whisper.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T1cju7HyQUWWlCiZQ87fNwT9plZ9CG3x
"""

!pip install gradio
!pip install openai-whisper
import whisper  # Importing the whisper library

try:
    import gradio as gr
except ModuleNotFoundError:
    !pip install gradio
    import gradio as gr

# Cargar el modelo de Whisper
model = whisper.load_model("base")

# Función principal que procesa el archivo de audio
def transcribe_and_translate(audio_file):
    # Paso 1: Transcripción en español
    result = model.transcribe(audio_file, language="es")
    spanish_text = result["text"]

    # Retornar la transcripción para que Gradio pueda mostrarla
    return spanish_text

# Crear la interfaz de Gradio
iface = gr.Interface(
    fn=transcribe_and_translate,  # La función a llamar
    inputs=gr.Audio(type="filepath"),  # Subir archivo de audio
    outputs=gr.Textbox(label="Transcripción en Español"),
    title="Transcriptor de audio",
    description="Sube un archivo de audio para obtener su transcripción."
)

# Iniciar la aplicación
iface.launch()
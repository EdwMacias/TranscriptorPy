import whisper
import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="whisper")

# Cargar el modelo
model = whisper.load_model("medium")

# Transcribir el audio
result = model.transcribe("JUNTA.mp4")

# Guardar el texto en un archivo .txt
with open("transcripcion.txt", "w") as file:
    file.write(result["text"])

print("Transcripción guardada en transcripcion.txt")

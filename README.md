# RevisarCUDA

## Descripción
El script `revisarCUDA.py` verifica la disponibilidad de CUDA en tu sistema y obtiene el nombre de la GPU activa. Es útil para asegurarte de que tu entorno está configurado correctamente para usar la aceleración por hardware.

## Funcionamiento
1. Comprueba si CUDA está disponible utilizando PyTorch.
2. Muestra el nombre de la GPU activa si CUDA está habilitado.

## Requisitos
- Python instalado en tu sistema.
- Biblioteca PyTorch configurada correctamente.
- Un entorno con una GPU compatible con CUDA.

## Uso
1. Ejecuta el script en tu terminal:
   ```bash
   python revisarCUDA.py

# Transcriptor

## Descripción
El script `transcriptor.py` utiliza la biblioteca `whisper` de OpenAI para transcribir automáticamente el audio o video de un archivo multimedia a texto. La transcripción se guarda en un archivo `.txt` para fácil consulta.

## Funcionamiento
1. **Carga del modelo**: Se utiliza el modelo `medium` de Whisper para procesar el archivo multimedia.
2. **Transcripción**: Convierte el contenido del archivo `JUNTA.mp4` a texto.
3. **Guardado**: Almacena la transcripción generada en un archivo llamado `transcripcion.txt`.

## Requisitos
- **Python** instalado en tu sistema.
- Biblioteca Whisper instalada. Puedes instalarla con el siguiente comando:
  ```bash
  pip install git+https://github.com/openai/whisper.git

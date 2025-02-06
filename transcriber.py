from openai import OpenAI
import os

class AudioTranscriber:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def transcrever_audio(self, audio_path):
        try:
            with open(audio_path, "rb") as audio_file:
                transcript = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    response_format="text"
                )
            return transcript
        except Exception as e:
            raise RuntimeError(f"Erro na transcrição: {str(e)}")
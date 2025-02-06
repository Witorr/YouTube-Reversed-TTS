from openai import OpenAI
import os

class SummaryGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def gerar_resumo(self, texto):
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{
                    "role": "system",
                    "content": "Resuma o texto de forma clara e concisa."
                }, {
                    "role": "user",
                    "content": texto
                }]
            )
            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f"Erro ao gerar resumo: {str(e)}")
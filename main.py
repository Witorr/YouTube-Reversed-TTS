#Criação da interface para o usuário inputar os dados
#Realizar o input dos dados - Baixar o aúdio do Youtube ou qualquer outro canal
#Realizar a transcrição do áudio
#Pede para um modelo de linguagem realizar um resumo da transcrição do áudio
#Salvar o resumo em um arquivo de texto/pdf
from Interface import InterfaceUsuario
from downloader import YouTubeDownloader
from transcriber import AudioTranscriber
from summarizer import SummaryGenerator
from saver import TextSaver, PDFSaver
import os

class ProcessadorVideo:
    def __init__(self):
        self.downloader = None
        self.transcriber = AudioTranscriber()
        self.summarizer = SummaryGenerator()
    
    def processar(self, url):
        # 1. Download do áudio
        self.downloader = YouTubeDownloader(url)
        audio_path = self.downloader.baixar_audio()
        
        # 2. Transcrição
        transcricao = self.transcriber.transcrever_audio(audio_path)
        
        # 3. Geração do resumo
        resumo = self.summarizer.gerar_resumo(transcricao)
        
        # 4. Salvamento
        TextSaver.salvar(resumo)
        PDFSaver.salvar(resumo)
        
        # Limpeza
        os.remove(audio_path)

if __name__ == "__main__":
    def iniciar_processamento(url):
        processador = ProcessadorVideo()
        processador.processar(url)
    
    InterfaceUsuario(iniciar_processamento)
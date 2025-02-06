from pytubefix import YouTube
import ffmpeg
import os

class YouTubeDownloader:
    def __init__(self, url):
        self.url = url
        self.output_dir = "downloads"
        os.makedirs(self.output_dir, exist_ok=True)

    def baixar_audio(self):
        try:
            yt = YouTube(self.url)
            audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
            
            temp_path = audio_stream.download(output_path=self.output_dir)
            mp3_path = os.path.join(self.output_dir, "audio_temp.mp3")
            
            # Converter para MP3 usando FFmpeg
            ffmpeg.input(temp_path).output(mp3_path).run(overwrite_output=True, quiet=True)
            os.remove(temp_path)  # Remover arquivo temporário
            
            return mp3_path
        except Exception as e:
            raise RuntimeError(f"Erro ao baixar áudio: {str(e)}")
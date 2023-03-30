from pytube import YouTube
import time
class download:
    def __init__(self, url):
        youtube = YouTube(url)
        time.sleep(3)
        name = youtube.title.replace(":", "")
        name = name.replace("/", "")
        name = name.replace("?", "")
        name = name.replace('"', "")
        time.sleep(3) 
        audio_stream = youtube \
            .streams \
            .filter(only_audio=True, audio_codec='opus') \
            .order_by('bitrate') \
            .last()
        self.downloadAudio(audio_stream, name)
    
    def downloadAudio(self, audio_stream, name):
        
        audio_stream.download(
            output_path="audio",
            filename=f"{name}.mp3")
        self.output = f"{name}.mp3"
        return self.output
        
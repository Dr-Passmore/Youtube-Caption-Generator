from pytube import YouTube

class download:
    def __init__(self, url):
        youtube = YouTube(url)
        name = youtube.title.replace(":", "")
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
        
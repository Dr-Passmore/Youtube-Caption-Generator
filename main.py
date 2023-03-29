import downloadMP3
import secret
import createSRT
import pvleopard

downloadAudioFile = downloadMP3.download('https://www.youtube.com/watch?v=youJhzSYK04')


key = secret.access_key


leopard = pvleopard.create(access_key=key)

transcript, words = leopard.process_file(f"audio/{downloadAudioFile.output}")

print(transcript)
generator = createSRT.SubtitleGenerator()

with open(f"srt files/{downloadAudioFile.output}.srt", 'w') as f:
    f.write(generator.to_srt(words))



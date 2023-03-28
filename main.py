import downloadMP3
import secret
import pvleopard

downloadAudioFile = downloadMP3.download('https://www.youtube.com/watch?v=QKIW5_q8FX4')


key = secret.access_key


leopard = pvleopard.create(access_key=key)

transcript, words = leopard.process_file(f"audio\{downloadAudioFile.output}")

print(transcript)
print("-------")
print(words)
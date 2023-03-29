import downloadMP3
import secret
import createSRT
import pvleopard
import csv

key = secret.access_key
leopard = pvleopard.create(access_key=key)

with open("./videolist.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row[1])
        downloadAudioFile = downloadMP3.download(row[0])
        transcript, words = leopard.process_file(f"audio/{downloadAudioFile.output}")
        print(downloadAudioFile.output)
        print("--------------------------------")
        print(transcript)
        print("--------------------------------")
        generator = createSRT.SubtitleGenerator()

        with open(f"srt files/{downloadAudioFile.output}.srt", 'w') as f:
            f.write(generator.to_srt(words))



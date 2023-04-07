#import python files
import downloadMP3
import secret
import createSRT

#import python libraries
import pvleopard
import csv
import time
import tkinter
from tkinter import ttk
import sv_ttk

key = secret.access_key
leopard = pvleopard.create(access_key=key)

root = tkinter.Tk()

button = ttk.Button(root, text="Click me!")
button.pack()

# This is where the magic happens
sv_ttk.set_theme("dark")

root.mainloop()
'''
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
        
        time.sleep(10)

'''

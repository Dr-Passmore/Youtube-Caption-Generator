#import python files
import downloadMP3
import secret
import createSRT

#import python libraries
import pvleopard
import tkinter
from tkinter import ttk
import sv_ttk
import configparser
import logging
import os

class srtGeneration():
    def __init__(self):
        config = configparser.ConfigParser()
        configFile = os.path.exists('config.ini')
        if configFile == False:
            print("No file found")
            srtGeneration.configurationFileCreation(self, config)
            
        
    def configurationFileCreation(self, config):
        config.add_section('API Key')
        config.set('API Key', 'Key', '')
        with open(r"config.ini", 'w') as configuration:
            config.write(configuration)
        
        


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
logging.basicConfig(filename='YouTube Caption Generator.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

srtGeneration()
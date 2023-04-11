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
import requests


class srtGeneration():
    def __init__(self):
        #checks config.ini exists
        config = configparser.ConfigParser()
        configFile = os.path.exists('config.ini')
        if configFile == False:
            #if the file does not exist then create one
            logging.info("No config file found")
            srtGeneration.configurationFileCreation(self, config)
        else:
            logging.info("config.ini exists")
        
        #load user interface
        srtGeneration.userInterface(self, config)    
        
    def configurationFileCreation(self, config):
        logging.info("Creating 'config.ini' file")
        try:
            config.add_section('API Key')
            config.set('API Key', 'Key', '')
            with open(r"config.ini", 'w') as configuration:
                config.write(configuration)
            logging.info('config.ini created successfully')
        except Exception as e:
            logging.error(f"Failed to create config.ini: {e}")
    
    def userInterface(self, config):
        logging.info("User Interface Loading")
        root = tkinter.Tk()
        root.geometry("800x500")
        root.title("SRT Generator")
        button = ttk.Button(root, text="Click me!")
        button.pack()
        sv_ttk.set_theme("dark")

        root.mainloop()

    def updateConfig(self, config):
        print("Requires adding")
        
    def downloadAudio(self, url):
        if srtGeneration.checkURL(self, url) == False:
            logging.info("URL failed validation")
            
        else:
            print("hi")
            
    
    def checkURL(self, url):
        checkContent = '"playabilityStatus":{"status":"ERROR","reason":"Video unavailable"'
        try:
            logging.info("Checking Youtube URL is accessible")
            request = requests.get(url)
            return False if checkContent in request.text else True
        except Exception as e:
            logging.error(f"Request processing of URL failed: {e}")
            
        
    
    
key = secret.access_key
leopard = pvleopard.create(access_key=key)





# This is where the magic happens

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
import pyttsx3
import smtplib
import datetime
import os 
import webbrowser
import wikipedia

print("Initializing Jarvis :")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-62)

def speak(audio): 
   print("Jarvis : "+audio) 
   engine.say(audio) 
   engine.runAndWait() 

import speech_recognition as sr

def command(): 
   cmd = sr.Recognizer() 
   with sr.Microphone() as source: 
      cmd.adjust_for_ambient_noise(source)
      print('Listening .... ') 
      audio = cmd.listen(source) 
      try: 
          query = cmd.recognize_google(audio,language='en-in') 
          print('User: ‘+query+’\n') 
      except sr.UnknownValueError: 
          speak('Sorry ! I did not get that. Could you please type  it out ?')
          query = str(input('Command: ')) 
   return query

def greeting(): 
   currentH = int(datetime.datetime.now().hour) 
   if currentH >= 0 and currentH < 12 : 
      speak('Good Morning') 
   if currentH >= 12 and currentH < 17 : 
      speak('Good Afternoon') 
   if currentH >= 17 and currentH != 0 : 
      speak('Good Evening')

import pyaudio
import os
import random
from pygame import mixer
def playMusic(): 
   music_folder = r"E:\kabir singh" 
   music = os.listdir(music_folder) 
   random_music = music_folder + random.choice(music) 
   mixer.init() 
   mixer.music.load(random_music) 
   mixer.music.play()


import webbrowser
from googlesearch import search
def searchOnGoogle(query, outputList): 
   speak('The top five search results from Google are listed below.')
   for output in search(query, tld="co.in", num=10, stop=5, pause=2):
      print(output) 
      outputList.append(output) 
   return outputList 
def openLink(outputList): 
   speak("Here’s the first link for you.")
   webbrowser.open(outputList[0])  

greeting()
speak('Jarvis here.')
speak('What would you like me to do for you ?') 
print("Listening .....")

if __name__ == '__main__': 
  while True: 
     query = command() 
     query = query.lower()
     if 'play music' in query or 'play a song' in query : 
        speak("Here’s your music. Enjoy !") 
        playMusic() 
     if 'stop the music' in query or 'stop the song' in query or 'stop' in query : 
        mixer.music.stop() 
        speak('The music is stopped.')
     if 'search' in query:            
        outputList = []
        speak('What should I search for ?')
        query = command()            
        searchOnGoogle(query, outputList)
        speak('Should I open up the first link for you ?')
        query = command()
        if 'yes' in query or 'sure' in query:
           openLink(outputList)
        if 'no' in query:
           speak('Alright.')


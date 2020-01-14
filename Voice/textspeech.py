# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 23:24:13 2020

@author: ABHINAV
"""
import speech_recognition as sr 

  
# use the audio file as the audio source 
  
r = sr.Recognizer() 
  
with sr.Microphone() as source:
   
    audio = r.listen(source)   
  
try: 
    print(  r.recognize_google(audio)) 
  
except sr.UnknownValueError: 
    print("Google Speech Recognition could not understand audio") 
  
except sr.RequestError as e: 
    print("Could not request results from Google SpeechRecognition service".format(e))
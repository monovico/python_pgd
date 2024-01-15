import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
with sr.Microphone() as source:
    print('\nsay somthing!\n')
    audio = r.listen(source)
    
    
voice_text = r.recognize_google(audio)



if 'hi computer'in voice_text:
    engine = pyttsx3.init()
    engine.say('hi bastian')
    engine.runAndWait()
else :
    engine = pyttsx3.init()
    engine.say('bye bastian')
    engine.runAndWait()

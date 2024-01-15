import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
with sr.Microphone() as source:
    print('\nsay somthing!\n')
    audio = r.listen(source)
    
    
voice_text = r.recognize_google(audio)

print(voice_text)

if ('hi' in voice_text) or ('hello' in voice_text):
    engine = pyttsx3.init()
    engine.say('hi there')
    engine.runAndWait()
    
if ('bye' in voice_text) or ('goodbye' in voice_text):
    engine = pyttsx3.init()
    engine.say('later aligator')
    engine.runAndWait()
    
if 'Sebastian' in voice_text:
    engine = pyttsx3.init()
    engine.say('Sebastian you are the master of the universe')
    engine.runAndWait()
 
for i in range(1):    
    engine = pyttsx3.init()
    engine.say('I always feel that someone is watching me...peeeeppeeee')
    engine.runAndWait()
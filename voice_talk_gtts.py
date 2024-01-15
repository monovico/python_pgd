from gtts import gTTS
import os
import pyttsx3
from playsound import playsound

text = "Hello! My name is Sebastian.a little silly"
tts = gTTS(text, lang='en')
tts.save("hi.mp3")
playsound('hi.mp3')
os.remove('hi.mp3')

text = "Hola, me llamo Sebastian. Un poco loco"
tts = gTTS(text, lang='es')
tts.save("hi2.mp3")
playsound('hi2.mp3')
os.remove('hi2.mp3')


engine = pyttsx3.init()
engine.say("Hello! My name is Sebastian a little silly")
engine.runAndWait()
engine = pyttsx3.init()
engine.say("ola! mee yamoe Sbastean oon pohcoh lohcoh")
engine.runAndWait()
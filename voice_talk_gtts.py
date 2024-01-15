from gtts import gTTS
import os
import pyttsx3
from pydub import AudioSegment
from pydub.playback import play

# updated with PyDub, now the sounds work

text = "Hello! My name is Mono Vico. I am a little silly"
tts = gTTS(text, lang='en')
tts.save("hi.mp3")
sound = AudioSegment.from_mp3('hi.mp3')
play(sound)
os.remove('hi.mp3')

text = "Hola, me llamo Mono Vico. Un poco loco"
tts = gTTS(text, lang='es')
tts.save("hi2.mp3")
sound = AudioSegment.from_mp3('hi2.mp3')
play(sound)
os.remove('hi2.mp3')


engine = pyttsx3.init()
engine.say("Hello! My name is Vico a little silly")
engine.runAndWait()
engine = pyttsx3.init()
engine.say("ola! mee yamoe Vicoooo oon pohcoh lohcoh")
engine.runAndWait()

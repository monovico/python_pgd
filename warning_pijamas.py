import pyttsx3
import time

engine = pyttsx3.init()
engine.say("put on your pajamas ")
engine.runAndWait()

time.sleep(30)

engine = pyttsx3.init()
engine.say("this is your second warning to put on your pajamas put on your pajamas ")
engine.runAndWait()

time.sleep(30)

engine = pyttsx3.init()
engine.say("this is your last warning to put on your pajamas put on your pajamas ")
engine.runAndWait()

time.sleep(15)

engine = pyttsx3.init()
engine.say("if you did not put on your pajamas then youll get a consaqunce")
engine.runAndWait()
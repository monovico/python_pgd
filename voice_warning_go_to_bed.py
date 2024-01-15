import time
import pyttsx3

engine = pyttsx3.init()
engine.say("go to bed")
engine.runAndWait()

time.sleep(60)

engine = pyttsx3.init()
engine.say("this is your second warning to go to bed go to bed")
engine.runAndWait()

time.sleep(60)

engine = pyttsx3.init()
engine.say("this is your third warning to go to bed go to bed")
engine.runAndWait()

time.sleep(60)

engine = pyttsx3.init()
engine.say("this is your fourth warning to go to bed go to bed")
engine.runAndWait()

time.sleep(60)

engine = pyttsx3.init()
engine.say("this is your last warning to go to bed go to bed")
engine.runAndWait()

time.sleep(30)

engine = pyttsx3.init()
engine.say("if you are not in bed youll get a consequence")
engine.runAndWait()
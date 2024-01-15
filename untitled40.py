import pyttsx3
import time   

time.sleep(63000)

engine = pyttsx3.init()    
engine.say("happy new year")
engine.runAndWait()


print("happy new year")
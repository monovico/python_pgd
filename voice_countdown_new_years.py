import time
import pyttsx3
import datetime

new_years_time = datetime.datetime(2022, 1, 1, 00, 00)

for i in range(1000):
    time.sleep(6)
               
    now = datetime.datetime.now()
    phrase = "the time is now "+str(now.hour)+" hours with "+ str(now.minute)+ " minutes"
    print(phrase)
    engine = pyttsx3.init()
    engine.say(phrase) 
    engine.runAndWait()
    diff = new_years_time - now
    diff_min = diff.total_seconds() / 60
    phrase2 = "there are "+ str(int(diff_min)) + " minutes left for the new year"
    print(phrase2)
    engine = pyttsx3.init()
    engine.say(phrase2) 
    engine.runAndWait() 


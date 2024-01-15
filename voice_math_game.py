import time
import pyttsx3
import random

x = random.randint(50,100)
y = random.randint(0,49)
z = x - y

phrase = "what is " + str(x) + " minus " + str(y) + "  "

engine = pyttsx3.init()
engine.say(phrase)
engine.runAndWait()


start = time.time()
answer = input(phrase)
end = time.time()

time_for_answer = end - start


if int(answer) == z:
    engine = pyttsx3.init()
    engine.say("your answer is correct")
    engine.runAndWait()    
else:
    engine = pyttsx3.init()
    engine.say("your answer is incorrect, the answer is")
    engine.runAndWait()    
    engine = pyttsx3.init()
    engine.say(str(z))
    engine.runAndWait()
    
engine = pyttsx3.init()
engine.say("it took you")
engine.runAndWait()   
engine = pyttsx3.init()
engine.say(time_for_answer)
engine.runAndWait()
engine = pyttsx3.init()
engine.say("seconds")
engine.runAndWait()
import pyttsx3

phrase1="enter number from 0 to 99  "
engine = pyttsx3.init()
engine.say(phrase1)
engine.runAndWait()
x = input(phrase1)
x = int(x)

from random import randrange
y=randrange(100)
phrase2 = 'python chose ',y
engine = pyttsx3.init()
engine.say(phrase2)
engine.runAndWait()
print(phrase2)

if x>y:
    phrase="you win"
    engine = pyttsx3.init()
    engine.say(phrase)
    engine.runAndWait()
elif x==y:
    phrase="it is a tie"
    engine = pyttsx3.init()
    engine.say(phrase)
    engine.runAndWait()
else:
    phrase='python wins'
    engine = pyttsx3.init()
    engine.say(phrase)
    engine.runAndWait()


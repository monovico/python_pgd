import pyttsx3

engine = pyttsx3.init()
engine.say("please enter your name where it says please enter your name over on the right and down    ")
engine.runAndWait()


name = input("please enter your name    ")

name_letters = list(name)

engine = pyttsx3.init()
engine.say("I love you")
engine.runAndWait()

engine = pyttsx3.init()
engine.say(name)
engine.runAndWait()

engine = pyttsx3.init()
engine.say("your name is spelled")
engine.runAndWait()

for letter in name_letters:
    print(letter)
    engine = pyttsx3.init()
    engine.say(letter)
    engine.runAndWait()
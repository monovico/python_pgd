import random
import pyttsx3

cooking = ['stewed', 'boiled', 'mashed', 'air fried']

food = ['dead mice','brocoli','beans', 'sebastian', 'mariana', 'mono veeco','poopy slugs']

location = ['on the floor','in the shoe','upon the door','on the ceiling','on the cats face','in the toilet']

for i in range(5):
    phrase = random.choice(cooking) + random.choice(food) + random.choice(location)
    
    engine = pyttsx3.init()
    engine.say(phrase)
    engine.runAndWait()






















































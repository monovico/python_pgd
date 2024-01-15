import pyttsx3

array1 = ['papa','mama','bastian','mari']

array2 = [47,39,7,4]


for i in range(4):
    
    phrase = array1[i],"is",array2[i],"years old"
    
    print(phrase)
    
    engine = pyttsx3.init()
    engine.say(phrase)
    engine.runAndWait()
       

    

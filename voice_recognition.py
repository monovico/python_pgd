import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('\nsay somthing!\n')
    audio = r.listen(source)
    
    
voice_text = r.recognize_google(audio)

print(voice_text)
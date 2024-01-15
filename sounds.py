mport winsound
import random




for i in range(60):
    freq = random.randint(37,5000)
    duration = int(0.5*1000)
    print('the frequency is',freq,'the duration is',duration/1000,'seconds')
    winsound.Beep(freq, duration)

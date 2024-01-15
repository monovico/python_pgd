import winsound
listkeys = ['a','b','c','d','e','f','g']
freqs = [220,207,262,294,330,349,392]

duration  = 500
for i in range(10):
    key = input('play a keyboard key')
    index = listkeys.index(key)
    print(key,index)
    winsound.Beep(freqs[index], duration)
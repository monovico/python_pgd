import winsound
import numpy as np
from PIL import Image

list1 = [
[0,1,0,1,0],
[0,1,0,1,0],
[0,0,1,0,0],
[1,0,0,0,1],
[0,1,1,1,0], 
 ]

list1 = [
[1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1],
[1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,1],
[1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1],
[1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1],
[1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1],
 ]

# list1 =[
# [0,1],
# [0,1]
# ]

duration  = 1000
freq_high = 5000
freq_low  = 200

rows = len(list1)
cols = len(list1[0])
pixels = 50
h, w = pixels*rows, pixels*cols
data = np.zeros((h, w, 3), dtype=np.uint8)


for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j],end='')
        if list1[i][j] == 0:
            winsound.Beep(freq_low, duration)
            color = [255,255,255]
            data[i*pixels:(i+1)*pixels, j*pixels:(j+1)*pixels] = color
        else:
            winsound.Beep(freq_high, duration)
            color = [255,0,0]
            data[i*pixels:(i+1)*pixels, j*pixels:(j+1)*pixels] = color
    print()
img = Image.fromarray(data, 'RGB')
img.show()
            
    
















































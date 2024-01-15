import winsound


list5 = [
[0,0,1,0,0],
[0,1,1,0,0],
[0,0,1,1,1],
[0,0,1,1,1],
[0,0,1,0,1], 
 ]

list5 =[
[0,1],
[0,1]

        ]

duration = 1000

freq_high = 5000
freq_low = 500

for i in range(len(list5)):
    for j in range(len(list5[i])):
        print(list5[i][j],end='')
        if list5[i][j] == 0:
            winsound.Beep(freq_low, duration)  
        else:
            winsound.Beep(freq_high, duration)
    print()
    

    


















































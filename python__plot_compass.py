import matplotlib.pyplot as plt


x = [0]
y = [0]

plt.plot(x,y)
print ('enter letter n for North e for East s for South w for West nw for NorthWest sw for SouthWest se for SouthEast ne for NorthWest and exit for exit: ')
while True:
    a = input('enter letter:')
    
    #west
    if a == 'w':
        x.append(x[-1]-1)
        y.append(y[-1]+0)
    if a == 'n':
        x.append(x[-1]+0)
        y.append(y[-1]+1)
    if a == 's':
        x.append(x[-1]+0)
        y.append(y[-1]-1)
    if a == 'e':
        x.append(x[-1]+1)
        y.append(y[-1]+0)
    if a == 'nw':
        x.append(x[-1]-1)
        y.append(y[-1]+1)
    if a == 'sw':
        x.append(x[-1]-1)
        y.append(y[-1]-1)
    if a == 'se':
        x.append(x[-1]+1)
        y.append(y[-1]-1)
    if a == 'ne':
        x.append(x[-1]+1)
        y.append(y[-1]+1)
    if a == 'exit':
        break
    plt.plot(x,y)
    plt.gca().set_aspect('equal')
    plt.show()

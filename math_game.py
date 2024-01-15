import random
import time

score = 0
time_start = time.time()

while time.time() - time_start < 60:
    print('hi, do you want to divide(/),subtract(-) ,multiply(*) or add(+)or exit(x)')
          
    x = input()
    number1 = random.randint(0,10)
    number2 = random.randint(0,10) 
    if x == 'x':
        break
    if x == '+':
        print(number1, "+", number2, "= ?")
        answer = input()
        if int(answer) == number1 + number2:
            score = score + 1
            print("correct answer!")
            print(score)
        else:
            print("wrong answer")
        print('the answer was =', number1 + number2)
    if x == '*':
        print(number1, "*", number2, "= ?")
        answer = input()
        if int(answer) == number1 * number2:
            score = score + 2
            print("correct answer!")
            print(score)
        else:
            print("wrong answer") 
        print('the answer was =', number1 * number2)
    print("you score is now", score)
    if x == '/':
        print(number1, "/", number2, "= ?")
        answer = input()
        if int(float(answer)) == number1 / number2:
            score = score + 4
            print("correct answer!")
            print(score)
        else:
            print("wrong answer")
        print('the answer was =', number1 / number2)
    if x == '-':
        print(number1, "-", number2, "= ?")
        answer = input()
        if int(answer) == number1 - number2:
            score = score + 1
            print("correct answer!")
            print(score)
        else:
            print("wrong answer")
        print('the answer was =', number1 - number2)

import os
import r2d2 as r2d2
os.system('r2d2.py')
r2d2.main()

print('thank you for playing, your 60secs are up, your score is', score)
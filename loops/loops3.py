import random

number =1
previousNumber = 0
trilas =0





my_number = random.randint(0,20)
guess = 0

while my_number != guess:
    print("Guess my number!")
    guess = int(input())
    trilas +=1
    if my_number > guess:
        print("Sorry- my number is greater than your guess, Try again!")
    elif my_number < guess:
        print("Sorry- my number is smaller than your guess, Try again!")
    else:
        print("you win, trials:",trilas)


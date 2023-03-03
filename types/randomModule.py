import random


number1 = random.randint(1,100)
print(number1)

number2 = 0
count = 0
while number1 != number2:
    number2 = random.randint(1,100)
    count +=1
    print(count,number2)


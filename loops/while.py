initialCapital = 20000
percent = 0.03
maxTimeYears = 10
interest = 0
minTimeYears = 0


interest = initialCapital * (1 + percent) ** maxTimeYears
print(interest)

number=20730906
deletLastNumber = number
sumOfDigits = 0

while deletLastNumber >0:
    digit = deletLastNumber % 10
    sumOfDigits += digit

    deletLastNumber = deletLastNumber //10


print(sumOfDigits)
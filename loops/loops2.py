numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

firstValue = 0
secondValue = 1
thirdValue = 2
while secondValue < len(numbers):

    if numbers[firstValue]**2 == numbers[secondValue]:
        print("squares:", numbers[firstValue], numbers[secondValue])

    firstValue +=1
    secondValue +=1
    
while thirdValue < len(numbers):

    if numbers[firstValue]**2 == numbers[secondValue] and numbers[secondValue]**2 == numbers[thirdValue]:
        print( numbers[firstValue], numbers[secondValue],numbers[thirdValue])
    firstValue += 1
    secondValue += 1
    thirdValue += 1



texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

while secondValue < len(texts):

    if len(texts[firstValue]) == len(texts[secondValue]):
        print( texts[firstValue], texts[secondValue])
    firstValue += 1
    secondValue += 1







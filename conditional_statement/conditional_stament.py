likes = 500
shares= 100

num_likes = 3121
num_shares = 312
if num_likes > likes and num_shares > shares:
    print("price has been lowered")
else:
    print("not enough likes and shares")


isPizzaOrdered = True
isBigDrinkOrdered = True
isWeekend = False

if isPizzaOrdered or isBigDrinkOrdered  and not isWeekend:
    print("Discount for burger")
else:
    print("to get a discount please buy something")

diskSize = 140
diskSizeUsed = 133
fileSize = 10

if diskSize-diskSizeUsed >= fileSize:
    print("enough space to download file")
else:
    print("not enough space")



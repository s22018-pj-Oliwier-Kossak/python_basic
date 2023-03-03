
lastRow = 31
currentRow = 1
while currentRow <= lastRow:

    print("Row number ",currentRow)
    currentRow +=1

for i in range(1,14):
    print("kwadrat liczby: ", i * i)
    print("szescian liczby: ", i * i * i)

treeHight = 8
start = 1
space = treeHight//2
while start <= treeHight:
    tree = start*'x'
    print(space*' '+tree)
    start +=2
    space -=1

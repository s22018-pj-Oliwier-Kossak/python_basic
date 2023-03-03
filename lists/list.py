list = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
list.append('CHILD IN TIME')
list.append('AGAIN')

list.insert(2,'HOTEL CALIFORNIA')
list.insert(0,'THE SOUND OF SILENCE')

print(list.index('HOTEL CALIFORNIA'))
list.remove(('HOTEL CALIFORNIA'))

list[0] ="ENJOY THE SILENCE"
print(list)

hitsToRead =list.copy()
hitsToRead.reverse()
print(hitsToRead)

hitsToRead.sort()
hitsToRead.pop(0)
hitsToRead.pop(1)
print(hitsToRead)

additionalSongs = ['NOTHING COMPARES 2 U' , 'WISH YOU WERE HERE']

hitsToRead.extend(additionalSongs)
print(hitsToRead)
print(hitsToRead.count('WISH YOU WERE HERE'))
hitsToRead.clear()
print(hitsToRead)
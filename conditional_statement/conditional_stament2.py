likes = 500
shares= 100

num_likes = 311
num_shares = 133
if num_likes > likes and num_shares > shares:
    print("price has been lowered")
elif  num_shares < shares:
    print("not enough shares")
elif num_likes < likes:
    print("not enough likes")


musclePain = True
fever = True
weakness = True
isMan = False
if isMan and (fever or weakness or musclePain):
    print("suspicion of influenza")
elif musclePain and fever and weakness:
    print("suspicion of influenza")
elif not musclePain and not fever and  weakness:
    print("Just take a rest!")
else:
    print("you may be cold")
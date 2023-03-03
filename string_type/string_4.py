q = "THE EYES"
print(q[0],q[1],q[2],q[5],q[3],q[7],q[4],q[6])

line = "'Program \"Kropka nad i\" nadamy o: 22:00'"
time = line[34:39]
print(time)
tmp = line[10:]
print(tmp)
title = tmp[:tmp.find('"')]
print(title)

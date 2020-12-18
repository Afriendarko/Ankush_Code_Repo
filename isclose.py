import math
c=0
l = [[20,10],[20,50],[30,40],[35,40],[35,6]]
for i in range(len(l)-1):
    if math.isclose(l[i][0],l[i+1][0]):
        c+=1
    if math.isclose(l[i][1],l[i+1][1]):
        c+=1
print(c)
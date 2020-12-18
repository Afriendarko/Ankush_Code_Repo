# l= [[1,2,3,4,5,6],[2,3,0,4,7,2],[5,2,3,1,0,8],[2,3,4,3,0,0],[0,0,0,5,3,1],[1,0,5,2,3,5]]
# l= [[1,2,3],[0,0,0],[1,2,-5]]
max_sum = 0
for i in range(len(l)-2):
    for j in range(len(l)-2):
        print(l[i][j], l[i][j+1], l[i][j+2], l[i+1][j+1], l[i+2][j], l[i+2][j+1], l[i+2][j+2])

        sum = l[i][j] + l[i][j+1] + l[i][j+2] + l[i+1][j+1] + l[i+2][j] + l[i+2][j+1] + l[i+2][j+2]
        print(sum)
        if max_sum < sum:
            max_sum = sum
print()
print("Max sum of hour glasses is: ",max_sum)
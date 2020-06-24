names = []
scores = []
total=0
avg=0

# 詢問班上人數
n = input('How many people in this class? ')
n = int(n)

# 利用迴圈和input讓班上同學輸入名字和成績
for i in range(n):
    name = input('Please input the name: ')
    names.append(name)
    score = input('Please input the score: ')
    score = int(score)
    scores.append(score)
    
# 計算平均分數
for item in scores:
    total = total+item

print("The average is ", (total/n))    

# 計算最高分
highest=0
for i in range(n):
    if scores[i] > highest:
        highest = scores[i] 
        highestname = names[i]
        
print(highestname, 'got the highest score', highest)

# 計算最低分
lowest = 100
for i in range(n):
    if scores[i] < lowest:
        lowest = scores[i]
        lowestname = names[i]
print(lowestname, "got the lowest score", lowest)
    

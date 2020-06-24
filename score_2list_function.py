names=[]
scores=[]
avg=0

# 計算平均值的函式
def average(scores):
    total = 0
    n = len(scores)
    # average score
    for item in scores:
        total = total+item
    average = total/n
    return average

# 計算最高分的函式
def highestscore(scores):
    highest=0
    n = len(scores)
    for i in range(n):
        if scores[i] > highest:
            highest = scores[i] 
            highestname = names[i]
    person = list()
    person.append(highestname)
    person.append(highest)
    return person
        
# 計算最低分的函式
def lowestscore(scores):
    lowest = 100
    n = len(scores)
    for i in range(n):
        if scores[i] < lowest:
            lowest = scores[i]
            lowestname = names[i]
    person = list()
    person.append(lowestname)
    person.append(lowest)
    return person

# 主程式
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
    
#使用前面定義的函式直接找出最高、最低、平均
ave = average(scores)
high = highestscore(scores)
low = lowestscore(scores)
    
print("The average is", ave)    
print(high[0], 'got the highest score', high[1])
print(low[0], "got the lowest score", low[1])

scores = []

# 函式:enterscores
# 功能:輸入成績
# 輸入: 無
# 輸出: 分數的list-->scores
def enterscores():
    n = int(input('有多少人參加考試? '))
    for i in range(n):
        s = int(input('請依序輸入分數: '))
        scores.append(s)

# 函式:average
# 功能:計算平均分數
# 輸入:分數的list-->scores 
# 輸出:scores的平均分數
def average(scores):
    total = 0
    return sum(scores)/len(scores)

# 函式:highest
# 功能:找出最高分
# 輸入:分數的list-->scores 
# 輸出:scores的最高分
def highest(scores):
    return max(scores)
    
# 函式:lowest
# 功能:找出最低分
# 輸入:分數的list-->scores 
# 輸出:scores的最低分
def lowest(scores):
    return min(scores)

########
#主程式#
########
# 1. 輸入成績
enterscores()


# 2. 算平均分數
ave = average(scores)

print('數學平均分數為', ave)

# 3. 找出最高分
top = highest(scores)
print('全班數學最高分是', top, '分')


# 4. 找出最低分
bottom = lowest(scores)
print('全班數學最低分是', bottom, '分')

names=list()
scores=list()
avg=0

# function: average
def average(scores):
    total = 0
    n = len(scores)
    # average score
    for item in scores:
        total = total+item
    average = total/n
    return average

# function highestscore
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
        
# lowest score
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

# main function
# How many people in the class?
n = input('How many people in this class? ')
n = int(n)

# Input names & scores and establish the score list
for i in range(n):
    name = input('Please input the name: ')
    names.append(name)

    score = input('Please input the score: ')
    score = int(score)
    scores.append(score)

    ave = average(scores)
    high = highestscore(scores)
    low = lowestscore(scores)
    
print("The average is", ave)    
print(high[0], 'got the highest score', high[1])
print(low[0], "got the lowest score", low[1])

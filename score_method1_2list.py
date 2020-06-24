names=list()
scores=list()
total=0
avg=0

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
    
# average score
for item in scores:
    total = total+item

print("The average is ", (total/n))    

# highest score
highest=0
for i in range(n):
    if scores[i] > highest:
        highest = scores[i] 
        highestname = names[i]
        
print(highestname, 'got the highest score', highest)

# lowest score
lowest = 100
for i in range(n):
    if scores[i] < lowest:
        lowest = scores[i]
        lowestname = names[i]
print(lowestname, "got the lowest score", lowest)
    

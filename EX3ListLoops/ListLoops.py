words = []
sentence = input('Enter a sentence: ')
words = sentence.split(' ')
print(words)
#Gets a sentence and splits it into seperate words in a list.


points = []
gamePoints = (input('Enter the points for the game played (E.g. 5,6,7): '))
points = gamePoints.split(',')
print(points)
#Makes a list of all the numbers entered, seperated by commas.

total = 0
for x in points:
    total += int(x)
print('Total score is:' , total)
#Adds the integers entered and prints the result.
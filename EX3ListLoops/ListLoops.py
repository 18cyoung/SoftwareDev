words = []
sentence = input('Enter a sentence: ')
words = sentence.split(' ')
print(words)

points = []
gamePoints = (input('Enter the points for the game played (E.g. 5,6,7): '))
points = gamePoints.split(',')
print(points)

total = 0
for x in points:
    total += int(x)
    print('Total score is:' , total)
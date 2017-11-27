print('This program is deigned to give you data about your rainfall data.')
print('\n')
#Prints a start up message for user

Rainfall = []

monthlyFall = input('Enter your monthly rainfall data in mm (e.g. 20,23,18): ')
#Receives users data

Rainfall = monthlyFall.split(',')
print('Your data is:' , Rainfall)
#splits data into list

Rainfall = [int(x) for x in Rainfall]
Rainfall.sort()
#sorts rainfall in order from lowest to highest

Max = Rainfall[-1]
print('Your highest rainfall is:',Max)
#Prints last list value which will be max

Min = Rainfall[0]
print('Your lowest rainfall is:',Min)
#prints first list value which is min

Average = (sum(Rainfall,0))/len(Rainfall)
print('Your average rainfall is:',round(Average,2))
#Calculates and prints average of data

Total = (sum(Rainfall,0))
print('Your total rainfall is:',Total)
#Adds up all the values and prints total
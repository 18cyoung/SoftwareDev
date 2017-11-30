#Create a main function that runs when this file is executed
def menu():
    print('Hello,')
    print('This program will help you convert measurements.')
    print('----------')
    print('''The options are:
        1) Farenheit to Celcius
        2) Celcius to Farenheit
        3) Kilometres to Metres
        4) Metres to Kilometres''')

#Create a function to convert farenheit to celcius
def ftoc(fah):
    cel = round((fah-32)*(5/9),2)
    print(fah,'farenheit =',cel,'degrees celcius')

#Create a function to convert celcius to farenheit
def ctof(cel):
    fah2 = round((cel2*1.8+32),2)
    print(cel2,'farenheit =',fah2,'degrees farenheit')

#Create a function to kilometres to metres
def ktom(k):
    m = round(k*1000,2)
    print(k,'kilometres =',m,'metres')

#Create a function to kilometres to metres
def mtok(m):
    k = round(m/1000,2)
    print(m,'metres =',k,'kilometres')

menu()

val = 0
while val == 0:
    val = int(input('Please choose an option: '))
    if val == 1:
        fah = int(input('Enter a temperature: '))
        ftoc(fah)
        print('')
        val = 0
        menu()
    if val == 2:
        cel2 = int(input('Enter a temperature: '))
        ctof(cel2)
        print('')
        val = 0
        menu()
    if val == 3:
        k = int(input('Enter number of kilometres: '))
        ktom(k)
        print('')
        val = 0
        menu()
    if val == 4:
        m = int(input('Enter number of metres: '))
        mtok(m)
        print('')
        val = 0
        menu()



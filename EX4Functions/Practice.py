#Create a main function that runs when this file is executed
def main():
    print('Hello,')
    print('This program will ask you for a temperature in farenheit.')
    print('----------')
    val = int(input('Enter a value:'))
    ftoc(val)

#Create a function to convert farenheit to celcius
def ftoc(fah):
    #fah = int(input('Enter a temperature: '))
    cel = round((fah-32)*(5/9),2)
    print(fah,'farenheit =',cel,'degrees celcius')

main()


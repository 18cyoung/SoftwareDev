#Set variables to each file
Fragment = open("Fragment1.txt")
DNA = open("Suspect1.txt")

#Reads the files and sets as same variables
Fragment = Fragment.read()
DNA = DNA.read()

#Finds the location of the first letter of the fragment
Sus = DNA.find(Fragment)

#Analyses if fragment is in the suspect DNA then calculate the array location and print
if Fragment in DNA:
    print("The DNA fragment is present in the provided sequence. It is at the location [",Sus,",",(Sus+len(Fragment)),"]")
else:
    print("The DNA fragment is not present in the provided sequence.")

#Confirm that the found fragment is correct
print("The fragment is:",DNA[98:102])
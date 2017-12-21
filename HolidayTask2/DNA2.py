#Set variables to each file
Frag1 = open("Fragment1.txt")
Frag2 = open("Fragment2.txt")
Frag3 = open("Fragment3.txt")
Frag4 = open("Fragment4.txt")
Frag5 = open("Fragment5.txt")
Frag6 = open("Fragment6.txt")

Sus1 = open("Suspect1.txt")
Sus2 = open("Suspect2.txt")
Sus3 = open("Suspect3.txt")
Sus4 = open("Suspect4.txt")
Sus5 = open("Suspect5.txt")

#Reads the files and sets as same variables
Frag1 = Frag1.read()
Frag2 = Frag2.read()
Frag3 = Frag3.read()
Frag4 = Frag4.read()
Frag5 = Frag5.read()
Frag6 = Frag6.read()

Sus1 = Sus1.read()
Sus2 = Sus2.read()
Sus3 = Sus3.read()
Sus4 = Sus4.read()
Sus5 = Sus5.read()

#Finds the location of the first letter of each fragment for each suspect
Frag1Sus1 = Sus1.find(Frag1)
Frag2Sus1 = Sus1.find(Frag2)
Frag3Sus1 = Sus1.find(Frag3)
Frag4Sus1 = Sus1.find(Frag4)
Frag5Sus1 = Sus1.find(Frag5)
Frag6Sus1 = Sus1.find(Frag6)

Frag1Sus2 = Sus2.find(Frag1)
Frag2Sus2 = Sus2.find(Frag2)
Frag3Sus2 = Sus2.find(Frag3)
Frag4Sus2 = Sus2.find(Frag4)
Frag5Sus2 = Sus2.find(Frag5)
Frag6Sus2 = Sus2.find(Frag6)

Frag1Sus3 = Sus3.find(Frag1)
Frag2Sus3 = Sus3.find(Frag2)
Frag3Sus3 = Sus3.find(Frag3)
Frag4Sus3 = Sus3.find(Frag4)
Frag5Sus3 = Sus3.find(Frag5)
Frag6Sus3 = Sus3.find(Frag6)

Frag1Sus4 = Sus4.find(Frag1)
Frag2Sus4 = Sus4.find(Frag2)
Frag3Sus4 = Sus4.find(Frag3)
Frag4Sus4 = Sus4.find(Frag4)
Frag5Sus4 = Sus4.find(Frag5)
Frag6Sus4 = Sus4.find(Frag6)

Frag1Sus5 = Sus5.find(Frag1)
Frag2Sus5 = Sus5.find(Frag2)
Frag3Sus5 = Sus5.find(Frag3)
Frag4Sus5 = Sus5.find(Frag4)
Frag5Sus5 = Sus5.find(Frag5)
Frag6Sus5 = Sus5.find(Frag6)

#Checks if fragment is in the suspect's DNA then calculates the array location for each fragment present per suspect
if Frag1 in Sus1:
    print("Fragment 1 is present in suspect 1's DNA sequence.")
    print("It is at the location [",Frag1Sus1,",",(Frag1Sus1+len(Frag1)),"]")

if Frag2 in Sus1:
    print("Fragment 2 is present in suspect 1's DNA sequence.")
    print("It is at the location [",Frag2Sus1,",",(Frag2Sus1+len(Frag2)),"]")

if Frag3 in Sus1:
    print("Fragment 3 is present in suspect 1's DNA sequence.")
    print("It is at the location [",Frag3Sus1,",",(Frag3Sus1+len(Frag3)),"]")

if Frag4 in Sus1:
    print("Fragment 4 is present in suspect 1's DNA sequence.")
    print("It is at the location [",Frag4Sus1,",",(Frag4Sus1+len(Frag4)),"]")

if Frag5 in Sus1:
    print("Fragment 5 is present in suspect 1's DNA sequence.")
    print("It is at the location [",Frag5Sus1,",",(Frag5Sus1+len(Frag5)),"]")

if Frag6 in Sus1:
    print("Fragment 6 is present in suspect 1's DNA sequence.")
    print("It is at the location [",Frag6Sus1,",",(Frag6Sus1+len(Frag6)),"]")

print("\n")

if Frag1 in Sus2:
    print("Fragment 1 is present in suspect 2's DNA sequence.")
    print("It is at the location [",Frag1Sus2,",",(Frag1Sus2+len(Frag1)),"]")

if Frag2 in Sus2:
    print("Fragment 2 is present in suspect 2's DNA sequence.")
    print("It is at the location [",Frag2Sus2,",",(Frag2Sus2+len(Frag2)),"]")

if Frag3 in Sus2:
    print("Fragment 3 is present in suspect 2's DNA sequence.")
    print("It is at the location [",Frag3Sus2,",",(Frag3Sus2+len(Frag3)),"]")

if Frag4 in Sus2:
    print("Fragment 4 is present in suspect 2's DNA sequence.")
    print("It is at the location [",Frag4Sus2,",",(Frag4Sus2+len(Frag4)),"]")

if Frag5 in Sus2:
    print("Fragment 5 is present in suspect 2's DNA sequence.")
    print("It is at the location [",Frag5Sus2,",",(Frag5Sus2+len(Frag5)),"]")

if Frag6 in Sus2:
    print("Fragment 6 is present in suspect 2's DNA sequence.")
    print("It is at the location [",Frag6Sus2,",",(Frag6Sus2+len(Frag6)),"]")

print("\n")

if Frag1 in Sus3:
    print("Fragment 1 is present in suspect 3's DNA sequence.")
    print("It is at the location [",Frag1Sus3,",",(Frag1Sus3+len(Frag1)),"]")

if Frag2 in Sus3:
    print("Fragment 2 is present in suspect 3's DNA sequence.")
    print("It is at the location [",Frag2Sus3,",",(Frag2Sus3+len(Frag2)),"]")

if Frag3 in Sus3:
    print("Fragment 3 is present in suspect 3's DNA sequence.")
    print("It is at the location [",Frag3Sus3,",",(Frag3Sus3+len(Frag3)),"]")

if Frag4 in Sus3:
    print("Fragment 4 is present in suspect 3's DNA sequence.")
    print("It is at the location [",Frag4Sus3,",",(Frag4Sus3+len(Frag4)),"]")

if Frag5 in Sus3:
    print("Fragment 5 is present in suspect 3's DNA sequence.")
    print("It is at the location [",Frag5Sus3,",",(Frag5Sus3+len(Frag5)),"]")

if Frag6 in Sus3:
    print("Fragment 6 is present in suspect 3's DNA sequence.")
    print("It is at the location [",Frag6Sus3,",",(Frag6Sus3+len(Frag6)),"]")

print("\n")

if Frag1 in Sus4:
    print("Fragment 1 is present in suspect 4's DNA sequence.")
    print("It is at the location [",Frag1Sus4,",",(Frag1Sus4+len(Frag1)),"]")

if Frag2 in Sus4:
    print("Fragment 2 is present in suspect 4's DNA sequence.")
    print("It is at the location [",Frag2Sus4,",",(Frag2Sus4+len(Frag2)),"]")

if Frag3 in Sus4:
    print("Fragment 3 is present in suspect 4's DNA sequence.")
    print("It is at the location [",Frag3Sus4,",",(Frag3Sus4+len(Frag3)),"]")

if Frag4 in Sus4:
    print("Fragment 4 is present in suspect 4's DNA sequence.")
    print("It is at the location [",Frag4Sus4,",",(Frag4Sus4+len(Frag4)),"]")

if Frag5 in Sus4:
    print("Fragment 5 is present in suspect 4's DNA sequence.")
    print("It is at the location [",Frag5Sus4,",",(Frag5Sus4+len(Frag5)),"]")

if Frag6 in Sus4:
    print("Fragment 6 is present in suspect 4's DNA sequence.")
    print("It is at the location [",Frag6Sus4,",",(Frag6Sus4+len(Frag6)),"]")

print("\n")

if Frag1 in Sus5:
    print("Fragment 1 is present in suspect 5's DNA sequence.")
    print("It is at the location [",Frag1Sus5,",",(Frag1Sus5+len(Frag1)),"]")

if Frag2 in Sus5:
    print("Fragment 2 is present in suspect 5's DNA sequence.")
    print("It is at the location [",Frag2Sus5,",",(Frag2Sus5+len(Frag2)),"]")

if Frag3 in Sus5:
    print("Fragment 3 is present in suspect 5's DNA sequence.")
    print("It is at the location [",Frag3Sus5,",",(Frag3Sus5+len(Frag3)),"]")

if Frag4 in Sus5:
    print("Fragment 4 is present in suspect 5's DNA sequence.")
    print("It is at the location [",Frag4Sus5,",",(Frag4Sus5+len(Frag4)),"]")

if Frag5 in Sus5:
    print("Fragment 5 is present in suspect 5's DNA sequence.")
    print("It is at the location [",Frag5Sus5,",",(Frag5Sus5+len(Frag5)),"]")

if Frag6 in Sus5:
    print("Fragment 6 is present in suspect 5's DNA sequence.")
    print("It is at the location [",Frag6Sus5,",",(Frag6Sus5+len(Frag6)),"]")
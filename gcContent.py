Sequence = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
C = int(Sequence.count('C'))
G = int(Sequence.count('G'))
Content = int((len(Sequence)))

### GC CONTENT

print('There are {0} Cs as well as {1} Gs out of a total of {2}'.format(C, G, Content))

PercentageGC = round(((G+C)/Content)*100, 2)

print(PercentageGC , "% of the line is composed of Cs and Gs.")

### REPLACE

Sequence2 = Sequence.replace("T", "U")

print(Sequence2)

### FRAGMENT LENGTHS

Fragment1 = ("ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT" [0:22])
Fragment2 = ("ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT" [23:56])

print(len(Fragment1) , len(Fragment2))
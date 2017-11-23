Sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
C = int(Sequence.count('C'))
G = int(Sequence.count('G'))
Content = int((len(Sequence)))

### LENGTH

print('There are {0} Cs as well as {1} Gs out of a total of {2}'.format(C, G, Content))

### PERCENTAGE

PercentageGC = round(((G+C)/Content)*100, 2)

print(PercentageGC , "% of the line is composed of Cs and Gs.")

### REPLACE

Sequence2 = Sequence.replace("T", "U")

print(Sequence2)


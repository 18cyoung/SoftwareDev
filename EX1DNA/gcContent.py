Sequence = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
C = int(Sequence.count('C'))
G = int(Sequence.count('G'))
Content = int((len(Sequence)))

### GC CONTENT

print('There are {0} Cs as well as {1} Gs out of a total of {2}'.format(C, G, Content))

PercentageGC = round(((G+C)/Content)*100, 2)

print(PercentageGC , "% of the line is composed of Cs and Gs.")


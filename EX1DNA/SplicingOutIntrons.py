Sequence = '''ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGA
TCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'''

# Made the Exons of correct fragments
Exon1 = Sequence[0:64]

Exon2 = Sequence[91:125]

# Prints Sequence without Intron
print(Exon1 + Exon2)

### PART 2

#Find lengths of sequences and Exons
SeqLen = len(Sequence)
Exon1Len = len(Exon1)
Exon2Len = len(Exon2)

# Find number of letters that are Exons
ExonNum = Exon1Len+Exon2Len

# Calculates percentage using Exons letters and sequence
Percentage = round((ExonNum/SeqLen)*100,2)

print(Percentage , "% is coding")

# Identifies the Intron
Intron1 = Sequence[65:91]

# Ensures Exons are printed in uppercase and Intron is in lowercase
print(Exon1.upper() + Intron1.lower() + Exon2.upper())
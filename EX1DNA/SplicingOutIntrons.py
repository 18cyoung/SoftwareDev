Sequence = '''ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGA
TCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'''

Exon1 = Sequence[0:64]

Exon2 = Sequence[91:125]

print(Exon1 + Exon2)

### PART 2

SeqLen = len(Sequence)
Exon1Len = len(Exon1)
Exon2Len = len(Exon2)

ExonNum = Exon1Len+Exon2Len

Percentage = round((ExonNum/SeqLen)*100,2)

print(Percentage , "% is coding")


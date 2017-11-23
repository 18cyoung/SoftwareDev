Sequence = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
Sequence = Sequence.lower()

Sequence2 = Sequence.replace("a", "C")
Sequence2 = Sequence2.replace("c", "A")
Sequence2 = Sequence2.replace("t", "G")
Sequence2 = Sequence2.replace("g", "T")


print(Sequence2)


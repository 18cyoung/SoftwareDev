Sequence = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
# Make sequence lower case so that replacement doesn't replace already affected letters.
Sequence = Sequence.lower()

#Replace letters with uppercase letters
Sequence2 = Sequence.replace("a", "C")
Sequence2 = Sequence2.replace("c", "A")
Sequence2 = Sequence2.replace("t", "G")
Sequence2 = Sequence2.replace("g", "T")


print(Sequence2)


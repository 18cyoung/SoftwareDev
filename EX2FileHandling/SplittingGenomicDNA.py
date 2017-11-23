File = open("GenomicDNA.txt")
DNA = File.read()

Exon1 = DNA[0:64]
Exon2 = DNA[91:124]
Intron1 = DNA[65:91]

print(len(DNA))

Coding = (Exon1 + "\n" + Exon2)

Exons = open("CodingDNA.txt","w")

Exons.write(Coding)

Introns = open("NonCodingDNA.txt","w")

Introns.write(Intron1)
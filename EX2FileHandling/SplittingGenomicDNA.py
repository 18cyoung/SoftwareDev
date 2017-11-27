# Open the DNA txt file
File = open("GenomicDNA.txt")
# Set DNA as the text in the File
DNA = File.read()

# Clarify the Exons and Introns
Exon1 = DNA[0:64]
Exon2 = DNA[91:124]
Intron1 = DNA[65:91]

# So I knew what the data length was when making fragments
print(len(DNA))

# Combines the Exons
Coding = (Exon1 + "\n" + Exon2)

# Writes Exons into CodingDNA.txt file
Exons = open("CodingDNA.txt","w")

Exons.write(Coding)

# Writes Introns into NonCodingDNA.txt file
Introns = open("NonCodingDNA.txt","w")

Introns.write(Intron1)
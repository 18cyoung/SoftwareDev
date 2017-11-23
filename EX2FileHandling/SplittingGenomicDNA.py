File = open(GenomicDNA.txt)
DNA = File.read()

Exon1 = File[0:64]
Exon2 = File[91:]

print(len(DNA))
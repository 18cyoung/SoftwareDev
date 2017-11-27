# Open the DNA txt file
File = open("input.txt")
#Open the file data is being inputed into
TrimmedFile = open('TrimmedDNA.txt','w')

for line in File:
    length = len(line)
    TrimmedLine = line[15:length]
    print(TrimmedLine)
    print('Trimmed line is:',len(TrimmedLine),'values long.')
    TrimmedFile.write(TrimmedLine)
    TrimmedFile.write('\n')
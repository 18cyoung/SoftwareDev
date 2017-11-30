def aa_Content():
    DNA = input('Please enter a protein sequence: ')
    RC = input('Please enter an amino acid residue code: ')
    DNA = list(DNA)
    RCnum = DNA.count(RC)
    DNAlen = len(DNA)
    rcComp = round((RCnum/DNAlen)*100,2)
    print('There is',RCnum,'of your letter(s):',RC)
    print('There is',DNAlen,'letter(s) in your protein sequence')
    print('The percentage composition of',RC,'is therefore',rcComp,'percent')

aa_Content()
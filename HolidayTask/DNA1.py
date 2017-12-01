Fragment = open("Fragment1.txt")
DNA = open("Suspect1.txt")
Fragment = Fragment.read()
DNA = DNA.read()

Sus = DNA.find(Fragment)

if Fragment in DNA:
    print("The DNA fragment is present in the provided sequence. It is at the location [",Sus,",",(Sus+len(Fragment)+1),"]")
else:
    print("The DNA fragment is not present in the provided sequence.")
#findLargest function finds and returns the largest DNA string
def findLargest(AA1, AA2):
    largest = ""
    
    if len(AA1) >= len(AA2):
        largest = AA1
    else:
        largest = AA2

    return largest

#align function compares two amino acid sequences and prints any differences (mutations)
def align(AA1, AA2):
    index = 0
    match = 0.0
    alignment = []
    largestAA = findLargest(AA1, AA2)
    print largestAA

    while index < len(largestAA):
        currentAA1 = AA1[index]
        currentAA2 = AA2[index]
        
        if currentAA1 != currentAA2:
            alignment.append("_")

        else:
            alignment.append("*")
            match += 1
        
        index += 1

    alignString = "".join(alignment)
    percent = round((match/len(largestAA))*100, 2)
    
    print "AA Sequence 1: " + AA1
    print "AA Sequence 2: " + AA2
    print '{:>15}'.format(alignString)
    print "Alignment: " + str(percent)

AASeq1 = raw_input("Input first amino acid sequence to be compared. \nAlternatively you can type 'q' to quit. \n")
AASeq2 = raw_input("Input second amino acid sequence to be compared. \nAlternatively type 'q' to quit. \n")

while AASeq1 != "q" and AASeq2 != "q":
    
    align(AASeq1, AASeq2)
    AASeq1 = raw_input("Input first amino acid sequence to be compared. \nAlternatively you can type 'q' to quit. \n")
    AASeq2 = raw_input("Input second amino acid sequence to be compared. \nAlternatively type 'q' to quit. \n")

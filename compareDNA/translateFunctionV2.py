def translate(dna):
    dna = dna.upper()
    start = 0
    output = []
    slcListI = ["ATT","ATC","ATA"]
    slcListL = ["CTT","CTC","CTA","CTG","TTA","TTG"]
    slcListV = ["GTT","GTC","GTA","GTG"]
    slcListF = ["TTT","TTC"]

    while start < len(dna)-2:
        currentCodon = dna[start:start+3]
        currentSLC = ""

        print "Processing %s ..." % currentCodon

        if currentCodon in slcListI:
            output.append("I")
            currentSLC = "I"

        elif currentCodon in slcListL:
            output.append("L")
            currentSLC = "L"

        elif currentCodon in slcListV:
            output.append("V")
            currentSLC = "V"

        elif currentCodon in slcListF:
            output.append("F")
            currentSLC = "F"

        elif currentCodon == "ATG":
            output.append("M")
            currentSLC = "M"

        else:
            output.append("X")
            print "The SLC of %s is not within the program's scope, therefore categorising as 'X' \n" % currentCodon
            currentSLC = "X"

        print "The SLC of %s is %s \n" % (currentCodon, currentSLC)

        start += 3

    print "The SLCs of the input DNA are: " + "".join(output) + "\n"

#Test

inputDNA = raw_input("Input DNA here, or type 'q' to quit: ")

while inputDNA != "q":
    translate(inputDNA)
    inputDNA = raw_input("Input DNA here, or type 'q' to quit: ")

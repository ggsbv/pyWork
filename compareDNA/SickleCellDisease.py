#Translate function accepts a string of DNA as input and finds the SLC code for
#each codon within that string.
def translate(dna):
    dna = dna.upper() #change all input to capital letters to avoid comparison issues
    start = 0 #Initialise the starting index as 0, since we will begin looking from index 0
    output = [] #Initialise output as list
    outputString = "".join(output)

    #Categorise all possible codon variations as lists respective of the Amino Acid they represent
    Isoleucine      =   ["ATT","ATC","ATA"]
    Leucine         =   ["CTT","CTC","CTA","CTG","TTA","TTG"]
    Valine          =   ["GTT","GTC","GTA","GTG"]
    Phenylalanine   =   ["TTT","TTC"]
    Methionine      =   ["ATG"]
    Cysteine        =   ["TGT","TGC"]
    Alanine         =   ["GCT","GCC"]
    Glycine         =   ["GGT","GGC","GGA","GGG"]
    Proline         =   ["CCT","CCC", "CCA", "CCG"]
    Threonine       =   ["ACT","ACC", "ACA", "ACG"]
    Serine          =   ["TCT","TCC", "TCA", "TCG", "AGT", "AGC"]
    Tyrosine        =   ["TAT","TAC"]
    Tryptophan      =   ["TGG"]
    Glutamine       =   ["CAA","CAG"]
    Asparagine      =   ["AAT","AAC"]
    Histidine       =   ["CAT","CAC"]
    GlutamicAcid    =   ["GAA","GAG"]
    AsparticAcid    =   ["GAT","GAC"]
    Lysine          =   ["AAA","AAG"]
    Arginine        =   ["CGT","CGC", "CGA", "CGG", "AGA", "AGG"]
    stopCodon       =   ["TAA","TAG", "TGA"]
    
    #While the starting index is less than the length of dna minus two, there must be valid codon,
    #therefore we will process it. We cannot assign an SLC to an incomplete codon.
    while start < len(dna)-2: 
        currentCodon = dna[start:start+3] #A codon is a substring of 3 nucleotides

        #if a codon is found within an amino acid list, then append the corresponding SLC code to the output
        #list. If a codon cannot be found in any list, categorise that codon as 'X'.
        if currentCodon in Isoleucine:
            output.append("I")

        elif currentCodon in Leucine:
            output.append("L")

        elif currentCodon in Valine:
            output.append("V")

        elif currentCodon in Phenylalanine:
            output.append("F")

        elif currentCodon in Methionine:
            output.append("M")

        elif currentCodon in Cysteine:
            output.append("C")

        elif currentCodon in Alanine:
            output.append("A")
            
        elif currentCodon in Glycine:
            output.append("G")

        elif currentCodon in Proline:
            output.append("P")

        elif currentCodon in Threonine:
            output.append("T")

        elif currentCodon in Serine:
            output.append("S")

        elif currentCodon in Tyrosine:
            output.append("Y")

        elif currentCodon in Tryptophan:
            output.append("W")

        elif currentCodon in Glutamine:
            output.append("Q")

        elif currentCodon in Asparagine:
            output.append("N")

        elif currentCodon in Histidine:
            output.append("H")

        elif currentCodon in GlutamicAcid:
            output.append("E")

        elif currentCodon in AsparticAcid:
            output.append("D")

        elif currentCodon in Lysine:
            output.append("K")

        elif currentCodon in Arginine:
            output.append("R")

        elif currentCodon in stopCodon:
            output.append("*")

        else:
            output.append("X")

        start += 3 #increment starting index by 3 in order to start processing the following codon

    #join the output list, which should the Amino Acid sequence of the input DNA string
    return "".join(output)

#Mutate function accepts a text filename as input and locates the first occurence
#of the letter 'a'. Two new output files are then created, one representing an example
#of normal DNA, and another representing a mutated version of the input DNA string. The input text
#is then copied and written to each new output file, with the letter 'a' translated to a suitable nucleotide.
    
def mutate(filename):
    inputFile = open(filename, 'r')
    normalDNA = open('normalDNA.txt', 'w')
    mutatedDNA = open('mutatedDNA.txt', 'w')
    index = 0
    

    for line in inputFile: #iterate over each line in the input file
        while index < len(line): #if line has not ended, we iterate over each character in the line
            currentChar = line[index]
            
            if currentChar == 'a': #if the current character is 'a', we overwrite that with the correct char depending on output file
                normalDNA.write('A')
                mutatedDNA.write('T')
                
            else: #otherwise we write the current character
                normalDNA.write(currentChar)
                mutatedDNA.write(currentChar)
                
            index+=1 #move on to next character

        index = 0 #line ends so we exit the while loop, and therefore index must be reset for the new line
    
    inputFile.close()
    normalDNA.close()
    mutatedDNA.close()

def txtTranslate(filename):
    inputFile = open(filename, 'r')
    dna = inputFile.read().replace('\n','') #take the text in the file and save it to variable 'dna' as a string for processing
    string = translate(dna)
    return string
    inputFile.close()

#Test

inputDNA = raw_input("Input name of the text file containing DNA string to be processed (Do not include file extension). \nAlternatively type 'q' to quit. \n") + ".txt"

while inputDNA != "q":
    translatedDNA = txtTranslate(inputDNA)
    outputFile = open(inputDNA + "_AASequence" + ".txt", 'w')
    outputFile.write(translatedDNA)
    outputFile.close()
    inputDNA = raw_input("Input name of the text file containing DNA string to be processed (Do not include file extension). \nAlternatively type 'q' to quit. \n") + ".txt"

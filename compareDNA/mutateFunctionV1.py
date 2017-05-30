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
            

mutate('DNA.txt')

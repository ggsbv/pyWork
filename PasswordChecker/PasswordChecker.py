#function countDifference compares two strings and returns the amount of characters that differ between the two
def countDifference(string1, string2):
    count = 0
    charIndex = 0
    len1 = len(string1)
    len2 = len(string2)
    
    if len1 < len2:
        count = count + (len2 - len1)

    for char in string1: 
        if charIndex >= len(string2):
            count += 1
            
        elif char != string2[charIndex]:
            count += 1
            
        charIndex += 1 
        
    return count 
	
#initialise global vars
password            = raw_input("Please enter your password: " )
correct_password    = "rusty" 
incorrect_passwords = []
current             = 0

while password != correct_password:
    current += 1
    incorrect_passwords.append("Incorrect password " + str(current) + ": " + password + ", wrong by " + str(countDifference(password, correct_password)) + " characters.")
    password = raw_input("Please try again: " )
    
    if password == correct_password:
        current +=1
        incorrect_passwords.append("Correct password entered on attempt number " + str(current))

print incorrect_passwords

f = open('wrongpasswords.txt', 'w')

#write all incorrect passwords into wrongpasswords.txt
for entry in incorrect_passwords:
    f.write(entry + "\n")

f.close()

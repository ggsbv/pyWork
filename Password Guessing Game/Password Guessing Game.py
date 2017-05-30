#Password guessing game!
#
#Enter a secret password and then someone else tries to decode it before they
#run out of tries!

print ''' 
#Password guessing game!
#
#Enter a secret password and then someone else tries to decode it before they run out of tries! 
'''

secret_password = raw_input("Enter the secret password to use: ") #input secret password
max_tries = int(raw_input("Enter max number of tries allowed: ")) #User inputs max number of tries
incorrect_names = [] #Initialise list
name = raw_input("Enter your name: " ) #User inputs name
current_tries = 0 #Initialise current number of tries the user is on.

while name != secret_password and current_tries < max_tries:
    current_tries += 1 #Increment by one per user attempt
    incorrect_names.append(name) #We append the user's attempted name to the list
    if current_tries < max_tries - 1:
        name = raw_input("Your guess was incorrect, please try another name: " )
    
    elif current_tries == max_tries - 1:
        name = raw_input("Warning! This is your last try! Enter your final guess: " )

print "Incorrect names: " + str(incorrect_names[0:]) #print the array of incorrect phrases entered

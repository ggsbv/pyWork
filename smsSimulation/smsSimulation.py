#An SMS Simulation
class SMSMessage(object):
    
    def __init__(self, messageText, fromNumber):
        self.number         = fromNumber
        self.hasBeenRead    = False
        self.messageText    = messageText


    def markAsRead(self):
        self.hasBeenRead = True
 
SMSStore = ['']

def add_sms(text, number):
    newSMS = SMSMessage(text, number)
    SMSStore.append(newSMS)

def get_count(inbox):
    return len(inbox)

def get_message(index):
    SMSStore[index].markAsRead()
    return SMSStore[index].messageText

def get_unread_messages(inbox):
    unread_messages = []
    for element in inbox:
        if element.hasBeenRead == False:
            unread_messages.append(element.messageText)
    return unread_messages

def remove(index):
    del SMSStore[index]

userChoice = ""

while userChoice != "q":
    userChoice = raw_input('''
What would you like to do?

Enter \"r\" to read your messages.
Enter \"s\" to send a message.
Enter \"u\" to check your unread messages.
Enter \"t\" to check total messages in you Inbox.
Enter \"d\" to delete a message.
Enter \"q\" to quit the program.

''')
    if userChoice == "r":
        index = int(raw_input("Enter the integer index of the message which you want to read: "))
        print get_message(index)
    elif userChoice == "s":
        text = raw_input("Enter your message: ")
        number = int(raw_input("Enter your number here: "))
        add_sms(text, number)
    elif userChoice == "u":
        print get_unread_messages(SMSStore)
    elif userChoice == "t":
        print get_count(SMSStore)
    elif userChoice == "d":
        index = int(raw_input("Enter the integer index of the message which you want to delete: "))
        remove(index)
    elif userChoice == "quit":
        print "Goodbye"
    else:
        print "Oops - incorrect input"

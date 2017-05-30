import re

#Ordinal function
def ordinal(num):
    suffixes = {1: 'st', 2: 'nd', 3: 'rd'}

    if 10 <= num % 100 <= 20:
        suffix = 'th'
        
    else:
        suffix = suffixes.get(num % 10, 'th')
    return str(num) + suffix

#Is number function, to check if a char is a number
def is_number(c):
    try:
        int(c)
        return True
    
    except ValueError:
        return False
    
#Min function
def minimum(list):
    min = list[0]
    for n in list:
        if n < min:
            min = n
    return min

#Max function
def maximum(list):
    max = list[0]
    for n in list:
        if n > max:
            max = n
    return max
    
#Average function
def avg(list):
    sum = 0
    for n in list:
        sum += float(n)
        
    avg = sum/(len(list))
    
    return avg

#Percentile function
def percentile(list, percentage):
    percentage = float(percentage) / 100
    p = len(list) * percentage
    p = int(round(p,0))
    return list[p-1]

in_file = open('input.txt', 'r')
o_file = open('output2.txt', 'w')

#read one line at a time
for line in in_file:
    line = line.rstrip("\n")
    current_list = re.split(',|:', line) #split strings in line into elements in a list
    int_list = current_list[1:]
    int_list = [int(string) for string in int_list]
    
    if current_list[0] == "max":
        o_file.write("The max of " + str(int_list) + " is " + str(maximum(int_list)) + "\n")
        print maximum(int_list)
    elif current_list[0] == "min":
        o_file.write("The min of " + str(int_list) + " is " + str(minimum(int_list)) + "\n")
    elif current_list[0] == "avg":
        o_file.write("The avg of " + str(int_list) + " is " + str(avg(int_list)) + "\n")
    elif current_list[0][0] == "p":
        num = int(current_list[0][1:])
        o_file.write("The " + str(ordinal(num)) + " percentile of " + str(int_list) + " is " + str(percentile(int_list, num)) + "\n")

in_file.close()
o_file.close()

import math #Import math in order to use math.sqrt on variance to find standard deviation

#Min function
def minimum(list):
    min = list[0]
    for n in list:
        if n < min:
            min = n

    f.write("The min of " + str(list) + " is " + str(min) + "\n")

#Max function
def maximum(list):
    max = list[0]
    for n in list:
        if n > max:
            max = n

    f.write("The max of " + str(list) + " is " + str(max) + "\n")

#Sum function, reused in avg function and Standard Deviation function, so I chose to make it return an int value
def Sum(list):
    sum = 0
    for n in list:
        sum += n

    return sum

#Average function, uses Sum function. Re-used avg function in computing Standard Deviation, so I chose to make it return an int value
def avg(list):
    sum = Sum(list)
    avg = sum/(len(list))
    
    return avg

#Standard Deviation function, uses avg function in order to compute
def standard_deviation(list):
    mean = avg(list)
    sum = 0
    
    for n in list:
        sum += (n - mean)**2
        
    variance = sum/len(list)
    std_dev = math.sqrt(variance)
    
    f.write("The standard deviation of " + str(list) + " is " + str(std_dev) + "\n")

#Test functions
list = [1, 5, 8, 77, 24, 95]
f = open('output.txt', 'w')
minimum(list)
maximum(list)
average = avg(list)#Demonstrate that I can assign a variable to a function's return value
f.write("The sum of " + str(list) + " is " + str(Sum(list)) + "\n")#Demonstrate that I can use function without assigning its return value to a variable
f.write("The average of " + str(list) + " is " + str(average) + "\n")
standard_deviation(list)

print "Results have been written to output.txt!"

f.close()

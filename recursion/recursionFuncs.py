def string_reverse(string):
#recursion ends when string == "", either as user input or via slicing iteratively
   if string == "":
      return string
#since iteration 1 of function suspends, the final letter will be the first one appended to string.
   else:
      return string_reverse(string[1:]) + string[0]

def factorial(n):
   if n == 0:
      return 1

   else:
      return factorial(n-1) * n

def fibonacci(n):

   if n <= 1:
      return n
   else:
      return fibonacci(n-1) + fibonacci(n-2)

n = int(raw_input("Enter number: "))
fibList = [fibonacci(n) for n in range(n)]
print fibList
   

def search_replace(s, w, r):

   if s == "":
      return s
   elif s[0:len(w)] == w:
      print "Replace \"%s\" with \"%s\"" % (s[0:len(w)], r)
      return r + search_replace(s[len(w):], w, r)
   else:
      return s[0] + search_replace(s[1:], w, r)

s = raw_input("Enter String: " )
w = raw_input("Enter word to find: ")
r = raw_input("Enter word to replace it with: ")

print search_replace(s, w, r)

# creating functions in python
def printHelloWorld():
    print("Hello World")
# calling the function    
# printHelloWorld()

def addTwoNumbers(a, b):
    return a + b

result = addTwoNumbers(2, 3)  # 5

# print("The result is: ", result)

def addThreeNumbers(a, b, c):
      print(a + b + c)
        
# addThreeNumbers(2, 3, 4)

# def homeWork():
#       print("Do your homework")
#       def members():
#             print("Members")
        
#       members()
# homeWork()

# announmous functions
add = lambda a, b: a + b
# print(add(2, 3)) # 5

# self closing function
def selfClosingFunction():
    pass

# selfClosingFunction()

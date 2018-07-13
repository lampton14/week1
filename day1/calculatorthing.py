
def Addition(a, b):
    result = a + b
    return result



def Subtraction(a, b):
    result = a - b
    return result

def Multiplication(a, b):
    result = 0
    for x in range (b):
        result= result + a
    return result



def Division(a, b):
    remainder = 0
    result = 0
    remainder = float(remainder)
    while (a >= b and a - b >= 0):
        a -= b
        result = result + 1
    if not (a == 0):
        remainder = a
    return result
    print (remainder)

unit20 = input("What would you like to do? 1-Addition, 2-Subtraction, 3-Multiplication, 4-Division")
if unit20 == "1":
    n1= input("please enter number 1: ")
    n2 = input("please enter number 2: ")
    print (Addition(int(n1), int(n2)))
elif unit20 == "2":
    n1= input("please enter number 1: ")
    n2 = input("please enter number 2: ")
    print (Subtraction(int(n1), int(n2)))
elif unit20 == "3":
    n1= input("please enter number 1: ")
    n2 = input("please enter number 2: ")
    print (Multiplication(int(n1), int(n2)))
elif unit20 == "4":
    n1= input("please enter number 1: ")
    n2 = input("please enter number 2: ")
    print (Multiplication(int(n1), int(n2)))

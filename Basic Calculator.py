import time
import math
def Add(a,b):
    return a + b
def Sub(a,b):
    return a - b
def Multiply(a,b):
    return a*b
def Divide(a,b):
    if b == 0:
        print("Can not divide by 0.")
        return ans
    else:
        return a/b
def SquareRoot(a):
    return math.sqrt(a)
def Square(a):
    return a**2
def sin(a):
    return math.sin(a)
def cos(a):
    return math.cos(a)
def tan(a):
    return math.tan(a)
def NlogF(a):
    return math.log(a)
def expeF(a):
    return math.exp(a)

def ScOpperation(a):
    if a == "Sr":
        ans = SquareRoot(I1)
        print(ans)
    elif a == "Sq":
        ans = Square(I1)
        print(ans)
    elif a == "Sn":
        ans = sin(I1)
        print(ans)
    elif a == "Cs":
        ans = cos(I1)
        print(ans)
    elif a == "Tn":
        ans = tan(I1)
        print(ans)
    elif a == "Nl":
        ans = NlogF(I1)
        print(ans)
    elif a == "Ee":
        ans = expeF(I1)
        print(ans)
    else:
        print("Incorrect abbreviation enter. Please Try Again")

def DecideOpperation(a):
    if a == "+":   
        ans = Add(I1,I2)
        print(ans)
    elif a == "-":
        ans = Sub(I1,I2)
        print(ans)
    elif a == "*":
        ans = Multiply(I1,I2)
        print(ans)
    elif a == "/":
        ans = Divide(I1,I2)
        print(ans)
    else:
        print("You didn't input a valid symbol please try again")

def CFF(a):
    if a.replace(".", "").isnumeric():
        return True
    else:
        return False



ans = 0
x = 1
while x == 1:
    print("Input 1 for normal calculator \nInput 2 for Scientic Calculator")
    SCorRC = int(input())
    while SCorRC == 1:
        print("Enter the first number.")
        I1 = input()
        if CFF(I1) == True:
            I1 = float(I1) 
            print("Enter symbol for operation: ")
            R1 = input()
            print("Enter the second number.")
            I2 = input()
            if CFF(I2) == True:
                I2 = float(I2)
                DecideOpperation(R1)
            else:
                print("You didn't enter a number please try again.")
        else:
            print("You didn't enter a number please try again.")
        print("To exit program enter 1 if not please press enter")
        c = input()
        if c == "1":
            x = 0
            SCorRC = 1000
        else:
            print("Input 1 for normal calculator \nInput 2 for Scientic Calculator")
            SCorRC = int(input())
    while SCorRC == 2:
        print("Enter the first number.")
        I1 = input()
        if CFF(I1) == True:
            I1 = float(I1) 
            print("Enter abbreviation: \n Square Root - Sr\n Square - Sq\n Sin - Sn \n Cos - Cs\n Tan - Tn \n Natural Log - Nl \n Exponential e - Ee")
            R1 = input()
            ScOpperation(R1)
        else:
            print("You didn't enter a number please try again.")
        print("To exit program enter 1 if not please press enter")
        c = input()
        if c == "1":
            x = 0
            SCorRC = 1000
        else:
            print("Input 1 for normal calculator \nInput 2 for Scientic Calculator")
            SCorRC = int(input())
    if SCorRC != 1 and SCorRC != 2 and SCorRC != 1000:
        print("Incorrect Input, Please Try Again.")
print("Thank you for using this calculator")
print("G")
time.sleep(1)
print("O")
time.sleep(1)
print("O")
time.sleep(1)
print("D")
time.sleep(1)
print("B")
time.sleep(1)
print("Y")
time.sleep(1)
print("E")

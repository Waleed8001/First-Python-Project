# Bano Qabil Calculator
a = 1
b = 2
c = 3
d = 4
e = 1
print("Calculator")
while e == 1:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

# For enter first number
    f = int(input("Enter First Number : "))

# For enter Second number
    g = int(input("Enter Second Number : "))
    print("What do you want ?")
    h = int(input("Please enter the number which is mention above : "))

# For Calculating Addition
    if h == a:
        i = f + g
        print("The answer is : ",i)
# For Calculating Subtraction
    if h == b:
        i = f - g
        print("The answer is : ",i)
# For Calculating Multiplication
    if h == c:
        i = f * g
        print("The answer is : ",i)
# For Calculating Division
    if h == d:
        i = f / g
        print("The answer is : ",i)
# If the user enter the wrong number 
    if h != a and h != b and h != c and h != d:
        print("You entered the wrong number")
# If the user want to calculate again
    e = int(input("If you want to perform calculation again then press 1 otherwise 0 : "))
else:
    print("Thank You $")
        
    

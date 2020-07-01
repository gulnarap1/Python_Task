#Following operations will be assigned if you enter:
#   1 - Addition
#   2 - Substraction
#   3 - Division
#   4 - Multiplication
#   5 - Average

#Asking the user to choose the operation type
x=input("Please enter a number from 1-5: ")

#if user enter 1
if x==1:
    first=input("Enter the first number: ")
    second=input("Enter the second number: ")
    first + second
    print("You performed addition. The output is: ", first + second )
    #if the outcome is negative value
    if (first + second)<0:
        print('Zsa')

#if user enter 2
if x==2:
    first=input("Enter the first number: ")
    second=input("Enter the second number: ")
    first - second
    print("You performed substraction. The output is: ", first - second )
    #if the outcome is negative value
    if (first - second)<0:
        print('Zsa')

#if user enter 3
if x==3:
    first=input("Enter the first number: ")
    second=input("Enter the second number: ")
    first / second
    print("You performed division. The output is: ", first / second )
    #if the outcome is negative value
    if (first / second)<0:
        print('Zsa')

#if user enter 4
if x==4:
    first=input("Enter the first number: ")
    second=input("Enter the second number: ")
    first / second
    print("You performed multiplication. The output is: ", first * second )
    #if the outcome is negative value
    if (first * second)<0:
        print('Zsa')

#if user enter 5
if x==5:
    first1=input("Enter the first number: ")
    second2=input("Enter the second number: ")
    float((first1 + second2)/2)
    print("You calculated the average of two numbers. The output is: ", float((first1 + second2)/2) )
    #if the outcome is negative value
    if float((first1 + second2)/2)<0:
        print('Zsa')
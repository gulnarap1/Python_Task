#Question 1
i=input("Please enter a number: ")
if i%3==0 and i%5==0:
    print('Consultadd Python Training')
    
elif i%3==0:
    print('Consultadd')

elif i%5==0:
        print('c ')


#Question 2
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


#Question 3
age=38

if age>=11:
    print('You are eligible to see the Football match')
    if age<=20 or age>=60:
        print('Ticket price is $12')
    else:
        print('Ticket price is $20')

else:
    print('You are not eligible to buy a ticket')


#Question 4
x=input('Enter a number: ')

#If a user enters a negative number just break the loop and print “It’s Over”

while x<0:
    print('It`s Over')
    break
    
#If a user enters a positive number just continue in the loop and print “Good Going”
while x>0:
    print('Good Going')
    continue


#Question 5
#Write a program in Python which will find all such numbers which are divisible 
# by 7 but are not a multiple of 5, between 2000 and 3200.
i = input('Please enter a number: ')

for i in range(2000, 3201):
    if i%7==0 and not i%5==0:
        print(i)
    continue

#Question 6
#A. The output of the above code is TypeError: 'int' object is not iterable
x=123 

for i in x:
    print(i)

#B.In the below code the output is 0, error, 1,error, 2. There is while loop which iterates till the condition within
the if statement is met which is when i becomes 3, break the loop. Else print error after every iterated i+=1
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")


#C. The output is from 0 to 4. Once count becomes equal to 1 loop breaks.
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break


#Question 7
x= range(0,7)

for i in x:
    if not i==3 and not i==6:
        print(i)

#Question 8
#Write a program that accepts a string as an input from the user and calculates the number of 
# digits and letters.Expected output: consul12, Letters 6, Digits 2

s= input("Enter digits and/or letters: ")
d=l=0

for i in s:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        l+=1
    else:
        pass
print("The number of letters is", l)
print("The number of digits is", d)

#Question 9
lucky=9

listed=['yes', 'Yes', 'YES']

while True:
    number= int(input('Guess lucky number: '))
    print(number)
    if number==lucky:
        print('The end!')
        break
    elif number!=lucky:
        answer = input("Would you like to guess again?")
        print(answer)
        if answer in listed:
            continue
        else:
            break

#Question 10
lucky=5

counter=1

while counter<=5:
    number=int(input('Guess the lucky number. You may do so only 5 times:'))
    print("You typed", number)
    if number==lucky:
        print('Good guess!')
        continue
    elif number!=lucky and counter==5:
        print('Game Over!')
        break
    elif number!=lucky:
        print('Try again!')
        counter=counter+1
        continue

#Quesion 11
lucky=5

counter=1

while counter<=5:
    number=int(input('Guess the lucky number. You may do so only 5 times:'))
    print("You typed", number)
    if number==lucky:
        print('Good guess!')
        break
    elif number!=lucky and counter==5:
        print('Sorry but that was not very successful.')
        break
    elif number!=lucky:
        print('Try again!')
        counter=counter+1
        continue
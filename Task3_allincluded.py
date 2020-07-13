#Question 1
# Create a list of the 10 elements of four different types of Data Types like int, string, 
#complex, and float.
c=[2, 6, 2+4j, 3.67, "Dear Client", 9, 7.9, "Hey!", 4-3j, 10]
print(c)

#Question 2
#Create a list of size 5 and execute the slicing structure 
my_list=[10, 20, ["It is me!"], 40, 50]

#Slicing
S1=my_list[:3]
print(S1)
S2=my_list[1:]
print(S2)
S3=my_list[::2]
print(S3)
S4=my_list[2][0]
print(S4)
S5=my_list[2][0][1]
print(S5)

#Question 3
list = list(range(1,21)) # use argument-unpacking operator i.e. *
sum_items = 0
multiplication = 1

for i in list:
  sum_items = sum_items + i 
  multiplication = multiplication * i

print ("Sum of all items is: ", sum_items)
print ("Multiplication of all items is: ", multiplication)

# Question 4: Find the largest and smallest number from a given list.

x=[3,2,7,4,5,10,1,8,9]

print(max(x))
print(min(x))

#Question 5: Create a new list that contains the specified numbers after removing 
# the even numbers from a predefined list. 

my_list=list(range(1,91))

for i in my_list:
    if i%2==0:
        my_list.remove(i)  

print(my_list)


# Question 6: Create a list of first and last 5 elements where the values 
# are square of numbers between 1 and 30 (both included).

initial_list=range(1,31)


x=[]
for i in initial_list:
    x=i**2
    print(x)

#Slicing - I couldnt do the slicing part but tried beneath code which didnt work out

a= list(([x[:4], x[-4:]]))
print(a)

# Question 7: Write a program to replace the last element in a list with another list.
# Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
# Expected output: [1,3,5,7,9,2,4,6,8]


sample_list=[[1,3,5,7,9,10],[2,4,6,8]]

begin= sample_list[0][:5]
end= sample_list[1][:]

a=sample_list[0][:]+sample_list[1][:]
print(a)
a.remove(10)
print(a)

#Question 8: Create a new dictionary by concatenating the following two dictionaries:
#a={1:10,2:20}
#b={3:30,4:40}
#Expected Result: {1:10,2:20,3:30,4:40}

a={1:10,2:20}
b={3:30,4:40}

concatenate={}
for i in (a,b): concatenate.update(i)
print(concatenate)


#Question 8: Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
#Expected Output: {1:1,2:4,3:9,4:16,5:25}

n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d) 

#Question 9: Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
#Expected Output: {1:1,2:4,3:9,4:16,5:25}

n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d) 

#Question 10: Write a program which accepts a sequence of comma-separated numbers from the console and generate 
# a list and a tuple which contains every number. Suppose the following input is supplied to the program:
#34,67,55,33,12,98

ln = str(input())
li = ln.split(',')
tup = tuple(li)
li = list(li)
print(tup)
print(li)


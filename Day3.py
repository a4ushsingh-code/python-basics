"""Loops"""
# allow us to execute a block of code multiple times without rewritting it

#Two types of loops in python
# 1. for loop: use when you know the number of iterations
# range() use for loop (start, stop, step) . it has default value (start = 0,step=1)

for i in range(16,0,-1): # i is varible you can use anything
    print(i)

for i in range(0,17):
    print(i) 

for i in range(-5,-25,-1):
    print(i)

# Table of 5
n = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{n} x {i} = {n * i}")

# loops for string

a = "Ayush is a good boy" #iterating by index values
for i in range(0,9):
    print(a[i]) 

a = "A loves B" #iterate directly over string
for i in a: # it means a ke har character ko ek ek krke i me store karo
    print(i) # i print kra rhe h Kyuki har iteration me current character i me hota hai.

# break : stop execution current loop and move to other loop
for i in range (1,21):
    if i ==15:
        break
    else:
        print(i)

# # continue : only skip current iteration not stops execution of loop
for i in range (1,21):
    if i==15:
        continue
    print(i)

# else in loops : exectes only if loop executes normally without using break

for i in range(1,20):
    if i == 5:
        break
    print(i)

# else:  # else not executes bcz break is used
    print("loop executed")


for i in range (1,20):
    if i ==5:
        continue
    print(i)

# else: # executes with continue block
    print("loop executed")

"""Practice of for loops"""

n = int(input("please tell your number"))
for i in range (n) :
    print("hello World")

n = int(input("Enter number up to u want"))
for i in range (1,n+1):
    print(i)

for j in range(n,0,-1):
    print(j)

n = int(input("Enter a number"))
for i in range (1,11):
    print(f"n x {i} = {n*i}")

n = int(input("enter a number that you want sum up to:"))
sum = 0
for i in range(1,n+1):
    sum = sum+i
print(sum)

n = int(input("Enter the number you want to find its factorial"))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print(fact) 

n = int(input("Enter the number "))
sum_odd = 0
sum_even = 0
for i in range (1,n+1):
    if i%2 == 0:
        sum_even = sum_even + i
    else:
        sum_odd = sum_odd + i

print(f"your even and odd sum are : {sum_even} , {sum_odd}")

n = int(input("Which number factors you want"))
for i in range (1,n+1):
    if n % i ==0 :
        print(f"This is your factor {i}")

n = int(input("enter the number : "))
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum = sum + i

if sum==n:
    print(f"{n} is a perfect number")

else :
    print(f"{n} is not a perfect number")

n =int(input("Check your number whether is prime or not :"))
count = 0
for i in range(1,n+1):
    if n%i == 0:
        count += 1
if count == 2:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not prime number")

a = "AYUSH"
b= ""
for i in range(len(a)-1,-1,-1):
    print(a[i])
    b = b + a[i]
print(b)

a = input("Enter the string :")
b = ""
for i in range (len(a)-1,-1,-1):
    b = b+a[i]

if b == a:
    print("It is a Palindrome")

else:
    print("Not Palindrome")

a = "dsdhhbx126645@#$%%^&*"
char = 0
digit = 0
spchr = 0
for i in a:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        char += 1
    else:
        spchr += 1

print(f"No of digits are {digit} \nNo of characters are {char} \nNo of special characters are {spchr}")
#2. While loops : while loop repests a block of code as long as a condition is true

# it is useful when the number of iterations is unknown before execution 
# it also have break , continue and else.

a = 1
while (a<=30):
    print(a)
    a+=1
"""Practice of While loop"""

#Seperation of digit
n = int(input("Tell your number"))
while n>0:
    print (n%10)
    n = n//10

# Print reverse of input
n = int(input("Enter the number to be reversed :"))
rev_digit = 0
num = n
while (n>0):
    last_digit= n%10
    rev_digit= rev_digit*10 + last_digit
    n//=10
print(f"The reverse of {num} is {rev_digit}")

# Palindrome :if num == rev_num
n = int(input("Enter the number to be checked"))
rev_num = 0
num = n
while n>0:
    last_digit = n%10
    rev_num = rev_num*10 + last_digit
    n//=10

if rev_num == num:
    print(f"{num} is a Palindrome number")

else:
    print(f"{num} is not a Palindrome number")

    



    

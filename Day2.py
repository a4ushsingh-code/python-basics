""" conditional statements"""
# It allows decision making by executing differnt blocks of code base on conditions
# It means we will control the flow of our program based on some conditions thats why these statements are also known as control flow statement

# 1. IF conditon : execute if condition is true
a = 12
if a>10:
    print(a)

# 2. Else condition : Check this condition first. If it is True, do the first thing. If it is False (not true), otherwise do the thing inside the else block."
age = int(input("Enter your age :"))
if age >= 18:
    print("Able to cast vote")

else :
    print("not able to cast vote")

# 3. Elif condition 
if age>18:
    print("able to cast vote ")

elif age==18:
    print("able to cast vote")

else:
    print("not able to cast vote")

"""Practice"""
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number"))
if num1>num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")


gen = input("please enter your gender")
if gen=="male"or gen=="Male":
    print("hello sir")
elif gen=="female" or gen=="Female":
    print("hello ma'am")
else:
    print("Invalid ! input")

num = int(input("Enter the number:"))
if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

year = int(input("enter the year"))
if year%400 == 0 or(year%4 == 0 and year%100 != 0):

    print(f"{year} is a leap year")
else:
    print(f"{year} is a non leap year")

tem = int(input("Enter temperature in celsius :"))
if tem<0:
    print("Freezing cold")
elif tem>=0 and tem<=10:
    print("Very Cold")
elif tem>10 and tem <= 20:
    print("cold")
elif tem>20 and tem <= 30:
    print("pleasant")
elif tem>30 and tem <= 40:
    print("hot")
elif tem >40:
    print("Very hot")


 

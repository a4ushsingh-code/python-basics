""" Data Types"""
a = 12
print(type(a))

b = 12.5
print(type(b))

c = -12
print(type(c))

d = 12/4
print(type(d)) #float

e = 12//4
print(type(e)) #int

""""strings"""

st = "My name is Lovely"
print(type(st))

# #indexing

a = "hello"
print(a[3])  #Positive indexing
print(a[-2]) #Negative indexing

#Slicing

a = "Modi Jee"
print(a[0:4:1]) #[start:stop:skip]
print(a[0:4])   #if skip is not given it interpreter takes default value 1
print(a[5:8:1])
print(a[5::1]) # if end point not given it takes value till end
print(a[:4:1]) #if start point not given it takes value from start

""""Type Conversion"""
# two types of conversion 

#1. Explicit Cconversion : user use in build functions to convert one data type to another 
a = 12
print(type(a))
a = str(a)
print(type(a))

#2. Implicit conversion : python automatically converts data from one data type to another
a = 12
print(12/3) # output : 4.0 python automatically converts output in float value

name = "Modi"
age = 100

print ("hello my name is ", name ,"my age is ",age )  
print(f"my name is {name} and my age is {age}") # Formatted String

"""Input"""

age = int(input("Enter your age :"))
print(age)


"""Operators"""
# 1. Arithmetic Operators
a = 8
b = 14
print(a+b) #Addition
print(a-b) #Subtraction
print(a*b) #Multiplication
print(b/a) #float Division
print(b//a) #floor Division
print(5**100) # 5 power 100
print(b%a) #modulus (output is remainder) 

# 2. Assignment Operators :use to assign values to variables
a = 20
a+=20 # a = a+20
a+=40 # a = a+40
print(a) 

# 3. comparison operators : used to compare two values
# # output will be true or false 
a = 12.1
b = 12
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
#comparison operators will work with numbers but you can use them with strings as well 
#strings will be comparing the Ascii values of string

print(ord("a")) #ord() is a built-in Python function that takes a single character and returns its corresponding integer Unicode code point
print(ord("b"))
print("a">"b") #compares corresponding ascii values
print("a">42)# type error

#4. logical operators
print(123>100 and 34==34) # AND = all conditions should be true then output is true
print(123>100 or 34!=34) # OR = if any condition is true then output is true
print(not 12 == 12) # NOT = it reverse the output(EX: 12==12 -> True but output is false )

print(126>130)
print((235==235) != (235==236)) 
print(12<10 or 45==56 or 69>70 or 15!=13)
print(True and bool(0))

""""Practice Questions"""
# #1. Hello world
print("Hello,World")

# #2. Name Print
name = "Ayush"
print("Hello, My name is ",name)
print(f"Hello, My name is {name}")

# #3. sum of two numbers
a = int(input("Enter first number"))
b = int(input("Enter second number"))
print(f"sum of {a} and {b} is {a+b}")

# #4. average of three numbers
c = int(input("Enter first number"))
d = int(input("Enter second number"))
e = int(input("Enter third number"))
print(f"The average of {c} ,{d},{e} is{(c+d+e)/3}")

# #5. Area of Rectangle 
f = int(input("Enter the length of a rectangle"))
g = int(input("Enter the width of a rectangle"))

print(f"The area of rectangle is {f*g}")



def sum(a,b):
    print(f"The sum of {a} and {b} is {a+b}  ")

sum(12,12)

def greet(name,age):  # Positional Arguments
    print(f"Hello My name is {name} and I'm {age} years old")

greet("ayush",30)

def student_info(name, branch="CSE", year=3): #Default Arguments
    print(f"{name} | {branch} |YEAR {year}")

student_info("Palak")
student_info("Palak","IT")
student_info("Palak","ME",2)
student_info("Palak",branch="CIVIL",year=4)

def add_numbers(*args):
    print(args)
    print(sum(args))

add_numbers(1, 2, 3)
add_numbers(1,2,3,4,5,6,7,8,9)

def student_info(**kwargs):
    print(kwargs)

student_info(name="Palak", age=18)

def students_info(name,age,branch):
    print(f"Name: {name}, Age: {age}, Branch: {branch}")

students_info("Palak",18,"CSE") #Positional argument(order matters)
students_info(age=19,branch="ME",name="Palak") # Keyword argument(order doesn't Matters)

def palindrome(st):
    rev = ""
    for i in range (len(st)-1,-1,-1):
        rev = rev + st[i]

    if rev == st:
        print("palindrome")

    else:
        print("Not Palindrome")

palindrome("ayush")
palindrome("naman")
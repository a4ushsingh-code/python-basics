#Armstrong Number
# num = int(input("Enter the Number"))
# digits = str(num)
# n = len(digits)
# total = 0
# for i in digits:
#     total += int(i) ** n
# if total==num:
#     print(f"{num} is an armstrong number ")
# else:
#     print(f"{num} is not an armstrong number")

#Palindrome number 
# num = int(input("Enter a number"))
# original_num = num
# reversed_num = 0
# while num>0:
#     last_digit = num%10
#     reversed_num = reversed_num*10 + last_digit
#     num = num//10
# if original_num == reversed_num:
#     print(f"{original_num} is a palindrome number")
# else:
#     print(f"{original_num} is not a palindrome nummber")

#Table of any number
num = int(input("Enter the number"))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")


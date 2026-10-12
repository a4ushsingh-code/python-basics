num = int(input("Enter number that has to be extracted: "))
#it prints extracted letter in reverse order
n = num  
while num>0:
    last_digit = num%10
    print(last_digit)
    num = num//10

# to tackle reverse order store digit in list and then reverse the list after extracting all digits
digits = [] 
while num>0:
    last_digit = num%10
    digits.append(last_digit)
    num = num//10
digits.reverse()
print(digits)

    
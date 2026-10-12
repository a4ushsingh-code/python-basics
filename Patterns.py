n =int(input("numbers of star you want :"))
# for i in range (n):
#     for j in range (n):
#         print("*",end='')
#     print() #when one row is printed we need to add a newline

# for i in range (1,n+1):
#     for j in range (i):
#         print("*",end='')
#     print()

# for i in range (1,n+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()


# for i in range(n+1):
#     for j in range(1,n+1-i+1):
#         print("*",end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(1,5):
#     for j in range(i):
#         print(i , end="")
#     print()

# for i in range(n,0,-1):
#     for j in range(i):
#         print(i,end='')
#     print()

# for i in range(1,n):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()


# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()

# for i in range (1,6):
#     for j in range(i,0,-1):
#         print(j,end='')
#     print()

# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(j,end='')
#     print()

# col = 1
# k = 1
# for i in range(1,n):
#     for j in range(1,col+1):
#         print(k,end='')
#         k +=1
#     col +=2
#     print()

# for i in range(1,n):
#     for j in range(1,i+1):
#         print(j,end=' ') 

#     for k in range(j-1,0,-1):
#         print(k,end=' ')
#     print()
    
# for i in range(1,n):
#     for j in range(n,i,-1):
#         print(" ",end='')

#     for k in range(1,i+1):
#         print("*",end='')
#     print()

for i in range(n,0,-1):
    for j in range(n,i,-1):
        print(" ",end=' ')
    for k in range(1,i+1):
        print("*",end=' ')

    print()


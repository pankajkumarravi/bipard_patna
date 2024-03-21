#print (".......simple calculator.....  ")
# num1= int(input("enter the first number :"))
# num2=int(input("enter the second no :"))
# num3=int(input("enter the third no :"))


# num1,num2,num3=10,20,30
# if num1>num2:
#     if num1>num3:
#         print(num1, "is max")
#     else:
#         print(num3, "is max")
# else:       
#     if num2>num3:
#             print(num2, " is max")
#     else:
#             print(num3," is max")
    


# for i in range (2000,2101):
#     if i %7==0 and i%5!=0:
#         if i <2093:
#             print(i, end=",")
#         else:
#             print(i)


#logic for prime no
# num=int(input("enter a no " ))
# for n in range (2,(num//2)+1):
#     if num%n==0:
#         print(num, "no is not prime")
#         break
# else:
#     print(num, "no is prime")

#function def 
# def check_prime (num):
#         for n in range (2,(num//2)+1):
#             if num%n==0:
#                 return False 
#         retunTrue
# #function calling
# if check_prime(34):
#     print ("prime")
# else:
#     print("non prime")


# def add(list):
#     list=["cdac","india"]

# list=["patna"]
# add(list)
# print(list)

# def add (list):
#     list.append("araria")
# list=("ranihanj")
# add(list)
# print(list)



#....building a simple calculator............
num1=float(input("enter first number: "))
num2=float(input("enter second number:"))
print("enter 1 for addition \n enter 2 for subtraction\n enter 3 for multiplication\n enter 4 for division")

choice=int(input("inter your choice from 1-4: "))
if choice==1:
    print("sum is" ,num1+num2,)
elif choice==2:
    print("sub is" ,num1-num2)
elif choice==3:
    print("mul is " ,num1*num2)
elif choice==4:
    print("div is ",num1/num2)
else:
    print("invalid input")


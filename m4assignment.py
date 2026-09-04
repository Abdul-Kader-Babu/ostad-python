#problem-1
# numberOne = int(input("Enter The First Number: "))
# numberTwo = int(input("Enter The Second Number: "))
# numberThree = int(input("Enter The Third Number: "))

# sum = numberOne+numberTwo+numberThree
# average = round(sum//3)


# print(f"Sum Of The Three Number is {sum} and average is {average}")

#problem-2
# number = int(input("Enter A Number: "))

# if number%2==0:
#     if number%5==0:
#         print ("Even")
#         print("divisible by both 2 and 5")
#     else:
#         print("Even and Divisible by Only 2")
# else:
#     print ("Odd And Divisible by only 5")

#problem-3

# a = int(input("Enter A Number: "))
# b = int(input("Enter A Number: "))
# c = int(input("Enter A Number: "))

# if a<b and b<c: #123
#     print(f"Smallest is {a} and largest is {c}")
# elif a>b and b>c: #321
#     print(f"Smallest is {c} and largest is {a}")
# elif a<b and b>c: #132
#     print(f"Smallest is {a} Largest is {b}")
# elif a==b or b==c or a==c:
#     print("two Number is Similar")

#problem-4
# number = int(input("Enter A Number: "))

# if number>0:
#     if number%2==0:
#         print("Positive and Even")
#     else:
#         print("Positive And Odd")
# elif number<0:
#     if number%2==0:
#             print("Negative and Even")
#     else:
#             print("Negative And Odd")
# else:
#      print("Zero")



#problem-5

English = int(input("Enter The Marks: "))
mathematics = int(input("Enter The Marks: "))
Science = int(input("Enter The Marks: "))

Total = English+mathematics+Science
Average = Total/3
print(f"Total = {Total}")
print(f"Average = {Average:.2f}")

if Average>100 or Average<0:
    print("Result = Invalid Marks")
elif Average>=80:
    print("Result = Excellent")
elif Average>=60:
    print("Result = Good")
elif Average>=40:
    print("Result = Pass")
else:
    print("Result = Fail")





    

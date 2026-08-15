# # একটি number input নিয়ে দেখাতে হবে সেটা Positive নাকি Negative
# number = int(input("Enter A Number: "))
# if number>0:
#     print ("Positive Number")
# elif number<0:
#     print("Negative Number")
# else: print("The Number Is Zero")

# # একটি integer input নিয়ে দেখাতে হবে সেটা Even নাকি Odd
# number = int(input("Enter A Number: "))
# if number%2==0:
#     print("Even Number")

# else: print("Odd Number")

# একটি student-এর marks input নিয়ে দেখাতে হবে সে Passed নাকি Failed
# Passing mark: 40

# marks = float(input("Enter Your Total Marks: "))
# if marks<0 and marks<100:
#     print("Invalid Marks")
# elif marks>=40:
#     print("Pass")
# else: print("Fail")

# একটি number input নিয়ে দেখাতে হবে সেটা 10-এর Greater নাকি Less than or Equal to 10
number = int(input("Enter A Number: "))
if number>10:
    print("The Number Is Greater Than 10")
elif number<=10:
    if number == 10:
        print("Number Is Equal to 10")
    else: print("The Number Is Less Than 10")

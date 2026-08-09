#1. Write a Python program that will print your name.
# print("Abdul Kader Babu");

#2. Write a Python program that will print your name, your father's and mother's name in three separate lines.
# myName = "Abdul Kader Babu";
# fatherName = ("Md Ali");
# motherName = "Ayesha Siddka";
# print(myName);
# print(fatherName);
# print(motherName);

#3. Write a Python program that will print the sum of two variables a and b; where a = 10 and b = 20.
# a = 10;
# b = 20;
# print(a+b);

#4. Write a Python program to calculate the sum of two integer numbers (given by the user) and print it.
# numOne = int(input("Enter The First Number: "));
# numTwo = int(input("Enter The Second Number: "));
# print(f"Sum Of Your Two Numer is: {numOne+numTwo}");

#5. Write a Python program that will take three numbers from the user and find their average.
# numberOne = int(input("Enter The First Number: "));
# numberTwo = int(input("Enter The Second Number: "));
# numberthree = int(input("Enter The Third Number: "));
# average =(numberOne+numberTwo+numberthree)/3;
# print(f"Average Of Your Numbers is : {average:.2f}");

#6. Write a Python program that will take three integers as input from the user and print their average. (Use type-cast to get the proper result)
# numberOne = int(input("Enter The First Number: "));
# numberTwo = int(input("Enter The Second Number: "));
# numberthree = int(input("Enter The Third Number: "));
# average =(numberOne+numberTwo+numberthree)/3;
# print(f"Average Of Your Numbers is : {average:.2f}");

#7. Write a Python program to convert a Km value into a meter value.
# kmValue = float(input("Enter The Distance in km: "));
# meter = int(kmValue*1000); # 1 kilometer = 1000 meter;
# print(f"{kmValue} kilometer is Equal to {meter} meter");

#8. Write a Python program to convert a Celsius value into a Fahrenheit value. (Formula: F = C * 9/5 + 32)
# temperature = float(input("Enter The temperature in celsius: "));
# Farenheit = temperature*9/5+32; # clus of celsius to farenheit = C * 9/5 + 32;
# print(f"{temperature} celsius is equal to {Farenheit} farenheit");

#9. Write a Python program to interchange the values of two numbers using a third variable.
# a = 100;
# b = 200;
# temp = a;
# a = b;
# b = temp;

# print(a,b);

#10. Write a Python program to interchange the values of two numbers without using a third variable.
# a = 100;
# b = 200;
# a,b = b,a;

# print(a, b);

#11. Write a Python program to input two numbers and print their quotient and remainder.
# numberOne = int(input("Enter The first number:  "));
# numberTwo = int(input("Enter The Second Number: "));
# quotinent = numberOne//numberTwo;
# reminder = numberOne%numberTwo;
# print(f"quotinent of {numberOne} is {quotinent} and reminder is {reminder}");

#12. Write a Python program to accept any character from the user and display its ASCII number on screen.
# character = input("Enter The Character: ");
# ascii = ord(character);
# print(f"ASCII CODE OF {character} is {ascii}");

#13. Write a Python program to input any ASCII number and display the appropriate character on screen.
# asciiNumber = int(input("Enter The Valid ascii code: "));
# character = chr(asciiNumber);
# print(f"character of {asciiNumber} is {character}");

#14. Write a Pyth#n program to input any capital letter and display it in small letter.
# cpletter = input("Enter Any Capital Letter : ");

# print(f"Small Letter Of {cpletter} is {cpletter.lower()}");

#15. Write a Python program to input any small letter and display it in capital letter.
# smletter = input("Enter Any capital letter: ");

# print(f"Capital Letter Of {smletter} is {smletter.upper()}");

#16. Write a Python program to input any capital letter and display it in small letter. (Without using the `lower()` method)
# cpletter = input("Enter Any Capital Letter : ");
# ascii = ord(letter)+32;
# print(f"Small Letter Of {letter} is {chr(ascii)}");

#17. Write a Python program to input any small letter and display it in capital letter. (Without using the `upper()` method)
# smletter = input("Enter Any capital letter: ");
# ascii = ord(smletter)-32;
# print(f"Capital Letter Of {smletter} is {chr(ascii)}");

#18. Write a Python program to input the number of days from the user and convert it into years, months and days.
# userday = int(input("Enter The Number of Days: "));
# years = int(userday/365);
# month = (userday-365*years) //30;
# day = (userday-365*years)-month*30;

# print(f"{userday} is {years} years, {month} month and {day} day");

#19. Write a Python program to input a three-digit number from the user and calculate the sum of the first and last digits. (Hint: Input: 358, Output: 11)
# number = int(input("Enter The Three digit number: "));
# firstDigit = int (number/100);
# lastDigit = (number-firstDigit*100)%10;
# sum = firstDigit+lastDigit;
# print(f"Sum of the first digit and last digit of {number} is {sum}");

#20. Write a Python program to input a three-digit number from the user and display the square of the first and last digits. (Hint: Input: 358, Output: Square of 3 is 9 and Square of 8 is 64)
# number = int(input("Enter A Three Digit Number: "));
# firstDigit = int(number/100);
# secondDigit = (number-firstDigit*100)%10;
# print(f"Square of {firstDigit} is {firstDigit**2} and square of {secondDigit} is {secondDigit**2}");

#21. Write a Python program to input a two-digit number from the user and display it with digits reversed. (Hint: Input: 32, Output: 23)

# number = int(input("Enter A Two Digit Number: "));
# firstNumber = number//10;
# secondNumber = int(number-firstNumber*10);
# firstNumber,secondNumber = secondNumber,firstNumber;
# reverse = firstNumber*10+secondNumber; 
# print(f"reverse of {number} is {reverse}");

#22. Write a Python program to find the quotient and remainder of two numbers. (Without using the modulus `%` operator)
firstNumber = int(input("Enter The First Number: "))
secondNumber = int(input("Enter The Second Number: "));
quotinent = firstNumber//secondNumber;
modulus = firstNumber-(secondNumber*quotinent);
print(f"quotation of {firstNumber} / {secondNumber} is {quotinent} and modulus is {modulus} ");

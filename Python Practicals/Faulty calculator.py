# Create a faulty calculator :-
#          Design a calculator which will correctly solve all the problems except the following ones :
#          45 * 3 = 555, 56 + 9 = 77, 56/6 = 4
#          Your program should take operator and two numbers as input from the user and them return the results.


print("If you want to calculate two numbers then, \n"
      "Enter + for addition \n"
      "Enter - for subtraction \n"
      "Enter * for multiplication \n"
      "Enter / for division \n"
      )

opt = input("Enter operator of any one :\n")
num1 = int(input("Enter first number : \n"))
num2 = int(input("Enter second number : \n"))

if opt == '+':
    if num1==56 and num2==9:
        print("56 + 9 = 77")
    else:
        print(num1, '+', num2,'=',num1+num2 )

elif opt=='-':
    print(num1, '-', num2,'=',num1-num2 )

elif opt == '*':
    if num1==45 and num2==3:
        print("45 + 3 = 555")
    else:
        print(num1, '*', num2,'=',num1*num2 )

elif opt == '/':
    if num1==56 and num2==6:
        print("56 + 6 = 4")
    else:
        print(num1, '/', num2,'=',num1/num2 )

else:
    print("please again check your entered value !!")










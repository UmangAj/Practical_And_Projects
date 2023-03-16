# write a program to know about you are eligible for voting or not.

print("Enter Your Age : ")
age = int(input())

if 18 <= age < 100:
    print("You can vote !!")
elif age < 18:
    print("You can not vote because you are not eligible !!")
else:
    print("Please enter valid age !!!")


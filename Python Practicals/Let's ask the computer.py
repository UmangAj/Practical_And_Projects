
# Let's ask the computer !!

import random
import time

print("Let's ask the computer if I go or not !!\nWe ask 5 times")
num = []

for i in range(1,6):
    a = int(random.randint(0, 1))
    time.sleep(2)
    if a==1:
        print(f"{i} : Yes. You can go !! ")
    else:
        print(f"{i} : Please don't go there !!! ")
    num.append(a)
a = num.count(1)
b = num.count(0)
time.sleep(2)
print(f"Computer says that '{a}' times 'Yes' and '{b}' times 'No' ")
time.sleep(2)
print("Your final or average answer is :-\n")
time.sleep(2)
if a > b :
    print("Yes. You can go !!")
else:
    print("Please don't go there !!!")



















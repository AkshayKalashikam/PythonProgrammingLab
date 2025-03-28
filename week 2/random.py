import random

n=random.randint(1,100)
while True: 
    x = int(input("guess the number:"))
    if(x<n):
    	print("the number is too low")
    elif(x>n):
        print("the number is too high")
    else:
        print("your guess is correct")

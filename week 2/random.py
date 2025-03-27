import random
n= random.randint (1,100)
while True:
    x= int(input("enter a number:"))
    if(x>n):
        print("too low")
    elif(x>n):
        print("too high")
    else:
        print("congralutions,you found the number")
    break

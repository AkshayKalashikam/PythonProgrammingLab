def print_list(elements):

    for i in elements:
        print (i,end=" ")
        
        
def largest(elements):
    for i in elements:
        largest=0
        largest=max(largest,i)
    print()
    print("largest=",largest)
                
    
elements=[]
limit=int(input("enter the length of list:"))
for i in range(limit):
    temp=int(input("enter number:"))
    elements.append(temp)
print_list(elements)
largest(elements)

def print_list(elements):
    for i in range(limit):
        print(elements)
limit = int(input("enter the length of the list:"))

elements = []
for i in range(limit):
    temp=int(input(f"enter number {i+1}:"))
    elements.append(temp)
print_list(elements)

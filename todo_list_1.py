# The todo list program rel #1

items = []

while True:
    myList = input ("Enter todo list item: ")
    if myList == "":
        break
    items.append(myList)
    print(items)
print("Thanks!\n", items)    

'''Develop a program that allows users to add, remove, and check off items on a shopping list 
stored in a dictionary.'''

dict = {}
while True:
    
    item = input("Enter a item: ")
    quantity = int(input("Enter the Quantity of Items: "))
    
    if item in dict:
        print(f" {item} is already Avail ")
    else:
        dict[item] = quantity

    user_input = input("r = remove / c = continue / q = quit  ")
    if user_input == 'r':
        remove_item = input("Enter the item you want to remove ")
        if remove_item in dict:
            dict.pop(remove_item)
            print(dict)

    if user_input == 'q':
        break
print(dict)
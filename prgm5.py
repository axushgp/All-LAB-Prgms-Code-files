numbers = []

n = int(input('Enter Size of the List: '))

while True:
    if n > 0:
        i = int(input('Enter the Element to Insert: '))
        numbers.append(i)
        n = n-1
    else:
        break

# Printing the Content of the List
print('List:', numbers)

# Performing the List Operation
while True:
    print('\n===== MENU =====')
    print('1. Inserting at Specific Position \n2. Remove the Values from the List \n3. Adding the Elements to the List\n4. Display the List\n5. Exit')

    choice = int(input('Enter the Choice: '))
    
    if(choice == 1):
        position = int(input('Enter the Position to Insert: '))
        item = int(input('Enter the Item to Insert at the Given position: '))
        numbers.insert(position, item)

    elif(choice == 2):
        position = int(input('Enter the Position to Delete an Item: '))
        numbers.pop(position)

    elif(choice == 3):
        item = int(input('Enter an Item to add: '))
        numbers.append(item)

    elif(choice == 4):
        print('\n===== List Content =====')
        print(numbers)

    elif(choice == 5):
        print('Exiting.....')
        break
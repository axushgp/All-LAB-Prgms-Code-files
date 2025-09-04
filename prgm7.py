setdata= set()
tupledata = tuple()

while 1:
    choice = input("Enter your choice \nS: Set Operation\nT: Tuple Operations\nN:Terminate\n")

    if choice=="s":
        while 1:
            print("Choose the Set operation")
            print("1: Add/Insert")
            print("2: Remove/Delete")
            print("3: Update/Append")
            print("4: Display/View")
            print("0: Exit")

            operations = int(input())

            if operations == 1:

                data = input("Enter the elements to add: ")
                setdata.add(data)
                print(setdata)
            
            elif operations == 2:

                data = input("Enter the elements to delete:") 
                setdata.discard(data)
                print(setdata)

            elif operations == 3:

                data = input("Enter the elements to update: ")
                setdata.update(data)
                print(setdata)

            elif operations == 4:

                print(setdata)

            elif operations == 0:
                break

            else:
                print("Invalid Choice")

    elif choice == "t":
        while 1:
            print("Choose the Tuple operation")
            print("1: Add/Insert")
            print("2: Delete Tuple")
            print("3: display/View")
            print("0: Exit\n")

            operations = int(input())

            if operations == 1:

                data = input("Enter the elements to add: ")
                tupledata+=(data,)
                
            elif operations == 2:

                del tupledata 
                print("Tuple Deleted")

            elif operations == 3:
                print(tupledata)

            elif operations == 0:
                break

            else:
                print("Invalid Choice")

    elif choice == "n":
        break
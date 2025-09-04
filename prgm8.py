def write():
    str = input("Enter the paragraph: ")
    with open("C:/Users/Ayush/Desktop/thezap/opencv/my_file.txt.txt", 'w') as file:
        file.write(str)
        file.close()            #not necessary, but good practice

def read():
    with open("C:/Users/Ayush/Desktop/thezap/opencv/my_file.txt.txt", 'r') as file:
        data=file.read()
        file.close()            #not necessary, but good practice

    print("\n--------------------")
    print("Original Content")
    print("--------------------")
    print(data)

    print("\n--------------------")
    print("Modified Content")
    print("--------------------")
    print(data.title())

# Function calls
write()
read()
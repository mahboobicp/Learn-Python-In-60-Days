# In this exercise we will work with files to save the user input data
while True:
    print("***"*10)
    uaction = input("Enter add , show , edit , complete or exit : ")
    user_action = uaction.lower()
    user_action = user_action.strip()        # Remove The spaces
    print("***"*10)
    path = r"D:\Python\Learn-Python-In-60-Days\Day 06 To Do App\todos.txt"
    match user_action:
        case 'add':
            todo = input("Enter To Do : ") + '\n'

            file = open(path , 'r')                     # Will open the file in read mode
            todos = file.readlines()                    # Read all the line from the file and return as list
            file.close()                                # After reading the data close the file
            
            todos.append(todo)                          # Add the user input to the list
            
            file = open(path , 'w')                     # Open the file in write mode for writing the new input
            file.writelines(todos)                      # Write the lines to the file
            file.close()                                # Close
        case 'show':
            file = open(path , 'r')                     # To read all the data from file and display it
            todos = file.readlines()
            file.close()                                # This block of code for removal of \n from file
            """ new_todos = []
            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item) """
            new_todos =[item.strip('\n') for item in todos] # Do the same with List Comprehensioin
            for index , value in enumerate(new_todos):      # The same can be done with direct method using print(row,end='')
            #   value = value.strip('\n')                   # same result can be achived with this
                row = f"{index + 1}-{value.title()}"
                print(row)
        case 'edit':
            number = int(input("Enter number of To Do in list to Edit : "))
            number -= 1                                 # list indexing start from 0
            todos[number] = input("Enter the new To Do : ")
        case 'complete':                                #  Complete Feature using pop method 
            number = int(input("Enter number of To Do in list to Complete : "))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:
            print("Try Again Incorrect option")
    
print("Bye___")
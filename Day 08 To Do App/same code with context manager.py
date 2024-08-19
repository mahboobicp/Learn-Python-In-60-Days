# In this exercise we will work with files to save the user input data
while True:
    print("***"*10)
    uaction = input("Enter add , show , edit , complete or exit : ")
    user_action = uaction.lower()
    user_action = user_action.strip()        # Remove The spaces
    print("***"*10)
    path = r"D:\Learn Python in 60 Days\Day 08 To Do App\todos.txt"
    match user_action:
        case 'add':
            todo = input("Enter To Do : ") + '\n'
            with open(path , 'r') as file:
                todos = file.readlines() 

            todos.append(todo)                          # Add the user input to the list
            
            with open(path , 'w') as file:
                file.writelines(todos)
        case 'show':
            with open(path , 'r') as file:
                todos = file.readlines()
    
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
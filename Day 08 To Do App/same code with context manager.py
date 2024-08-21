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
            new_todos =[item for item in todos]             # Do the same with List Comprehensioin
            for index , value in enumerate(new_todos):      # The same can be done with direct method using print(row,end='')
            #   value = value.strip('\n')                   # same result can be achived with this
                row = f"{index + 1}-{value.title()}"
                print(row, end='')
        case 'edit':
            number = int(input("Enter number of To Do in list to Edit : "))
            number -= 1
            with open(path , 'r') as file:
                todos = file.readlines()
            print(todos)    
            new_todos = input("Enter the new To Do : ")
            todos[number] =  new_todos+'\n'
            print(todos)
            with open(path , 'w') as file:
                file.writelines(todos)
            
        case 'complete':                                #  Complete Feature using pop method 
            number = int(input("Enter number of To Do in list to Complete : "))
            index = number - 1
            with open(path , 'r') as file:
                todos = file.readlines()
            todos.pop(index)
            with open(path , 'w') as file:
                file.writelines(todos)
        case 'exit':
            break
        case _:
            print("Try Again Incorrect option")
    
print("Bye___")
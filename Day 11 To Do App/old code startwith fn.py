while True:    
    uaction = input("\nEnter add, show, edit, complete or exit: ")
    user_action = uaction.lower()
    user_action = user_action.strip()       
    path = r"D:\Python\Learn-Python-In-60-Days\Files\todos.txt"
    if user_action.startswith('add'):
        todo = user_action[4:]
        with open(path , 'r') as file:
            todos = file.readlines() 

        todos.append(todo+'\n')                          
        
        with open(path , 'w') as file:
            file.writelines(todos)
    elif user_action.startswith('show'):
        with open(path , 'r') as file:
            todos = file.readlines()
        new_todos =[item for item in todos] 
        for index , value in enumerate(new_todos):                       
            row = f"{index + 1}-{value.title()}"
            print(row, end='')
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1
            with open(path , 'r') as file:
                todos = file.readlines()
            remove_todo = todos[number]   
            new_todos = input("Enter the new To Do : ")
            todos[number] =  new_todos+'\n'
            print(f"New To Do : {new_todos} Removed : {remove_todo}")
            with open(path , 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Invalid Input Commond")
            continue

    elif user_action.startswith('complete'):   
        try:                             
            number = number = int(user_action[9:])
            index = number - 1
            with open(path , 'r') as file:
                todos = file.readlines()
            todos.pop(index)
            with open(path , 'w') as file:
                file.writelines(todos)
        except IndexError:
            print("Item at index not found")
            continue
        
    elif user_action.startswith('exit'):
        break
    else:
        print("\nInvalid Input")    
    
print("Bye___")
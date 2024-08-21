def get_todo():
    with open(path , 'r') as file:
        todo_local = file.readlines()
    return todo_local


while True:    
    uaction = input("\nEnter add, show, edit, complete or exit: ")
    user_action = uaction.lower()
    user_action = user_action.strip()       
    path = r"D:\Python\Learn-Python-In-60-Days\Files\todos.txt"
    
    if 'add' in user_action or 'new' in user_action:   # Boolean Operator or , and , Not in
        todo = user_action[4:]
        
        todos = get_todo()

        todos.append(todo+'\n')                          
        
        with open(path , 'w') as file:
            file.writelines(todos)
    elif 'show' in user_action:
        todos = get_todo()
        new_todos =[item for item in todos] 
        for index , value in enumerate(new_todos):                       
            row = f"{index + 1}-{value.title()}"
            print(row, end='')
    elif 'edit' in user_action:
        number = int(user_action[5:])
        number -= 1
        todos = get_todo()
        remove_todo = todos[number]   
        new_todos = input("Enter the new To Do : ")
        todos[number] =  new_todos+'\n'
        print(f"New To Do : {new_todos} Removed : {remove_todo}")
        with open(path , 'w') as file:
            file.writelines(todos)
        
    elif 'complete' in user_action:                                
        number = number = int(user_action[9:])
        index = number - 1
        todos = get_todo()
        todos.pop(index)
        with open(path , 'w') as file:
            file.writelines(todos)
    elif 'exit' in user_action:
        break
    else:
        print("\nInvalid Input")    
    
print("Bye___")
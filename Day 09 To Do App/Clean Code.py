while True:    
    uaction = input("Enter add , show , edit , complete or exit : ")
    user_action = uaction.lower()
    user_action = user_action.strip()       
    path = r"D:\Python\Learn-Python-In-60-Days\Day 09 To Do App\todos.txt"
    if 'add' in user_action:
        todo = user_action[4:]
        with open(path , 'r') as file:
            todos = file.readlines() 

        todos.append(todo)                          
        
        with open(path , 'w') as file:
            file.writelines(todos)
    if 'show' in user_action:
        with open(path , 'r') as file:
            todos = file.readlines()
        new_todos =[item for item in todos] 
        for index , value in enumerate(new_todos):                       
            row = f"{index + 1}-{value.title()}"
            print(row, end='')
    if 'edit' in user_action:
        number = int(input("Enter number of To Do in list to Edit : "))
        number -= 1
        remove_todo = todos[number]
        with open(path , 'r') as file:
            todos = file.readlines()
        print(todos)    
        new_todos = input("Enter the new To Do : ")
        todos[number] =  new_todos+'\n'
        print(f"New To Do : {new_todos} Removed : {remove_todo}")
        with open(path , 'w') as file:
            file.writelines(todos)
        
    if 'complete' in user_action:                                
        number = int(input("Enter number of To Do in list to Complete : "))
        index = number - 1
        with open(path , 'r') as file:
            todos = file.readlines()
        todos.pop(index)
        with open(path , 'w') as file:
            file.writelines(todos)
    if 'exit' in user_action:
        break
  
    
print("Bye___")
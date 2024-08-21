# from function import get_todo, write_todos       import methods
import function
while True:    
    uaction = input("\nEnter add, show, edit, complete or exit: ")
    user_action = uaction.lower()
    user_action = user_action.strip()       
    path = r"D:\Learn Python in 60 Days\Files\todos.txt"
    
    if 'add' in user_action or 'new' in user_action:   # Boolean Operator or , and , Not in
        todo = user_action[4:]
        todos = function.get_todo(path)
        todos.append(todo+'\n')                          
        function.write_todos(path_local=path , todo_list=todos)
    
    elif 'show' in user_action:
        todos = function.get_todo(path)
        new_todos =[item for item in todos] 
        for index , value in enumerate(new_todos):                       
            row = f"{index + 1}-{value.title()}"
            print(row, end='')
    
    elif 'edit' in user_action:
        number = int(user_action[5:])
        number -= 1
        todos = function.get_todo(path)
        remove_todo = todos[number]   
        new_todos = input("Enter the new To Do : ")
        todos[number] =  new_todos+'\n'
        print(f"New To Do : {new_todos} Removed : {remove_todo}")
        function.write_todos(path_local=path , todo_list=todos)     
    
    elif 'complete' in user_action:                                
        number = number = int(user_action[9:])
        index = number - 1
        todos = function.get_todo()
        todos.pop(index)
        function.write_todos(path_local=path , todo_list=todos)
    
    elif 'exit' in user_action:
        break
    
    else:
        print("\nInvalid Input")    
    
print("Bye___")
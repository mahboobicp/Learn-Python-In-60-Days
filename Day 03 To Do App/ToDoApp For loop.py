todos = []
while True:
    print("***"*10)
    uaction = input("Enter add , show or exit : ")
    user_action = uaction.lower()
    print("***"*10)
    match user_action:
        case 'add':
            todo = input("Enter To Do : ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break
    
print("Bye___")
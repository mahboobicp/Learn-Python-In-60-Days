todos = []
while True:
    print("***"*10)
    uaction = input("Enter add , show or exit : ")
    user_action = uaction.lower()
    user_action = user_action.strip()
    print("***"*10)
    match user_action:
        case 'add':
            todo = input("Enter To Do : ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break
    
print("Bye___")
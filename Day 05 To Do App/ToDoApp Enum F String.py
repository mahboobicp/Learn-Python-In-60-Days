# Enumeration and String Formating using f string
todos = []
while True:
    print("***"*10)
    uaction = input("Enter add , show , edit or exit : ")
    user_action = uaction.lower()
    user_action = user_action.strip()        # Remove The spaces
    print("***"*10)
    match user_action:
        case 'add':
            todo = input("Enter To Do : ")
            todos.append(todo)
        case 'show':
            for i in todos:
                print(i.title())
        case 'edit':
            number = int(input("Enter number of To Do in list to Edit : "))
            number -= 1                     # list indexing start fro 0
            todos[number] = input("Enter the new To Do : ")
        case 'exit':
            break
    
print("Bye___")
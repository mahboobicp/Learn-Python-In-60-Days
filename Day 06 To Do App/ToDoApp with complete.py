# Enumeration and String Formating using f string
# Enumerate function return index of value in list
# Add Complete feature to list to remove the completed task from the list
todos = []
while True:
    print("***"*10)
    uaction = input("Enter add , show , edit , complete or exit : ")
    user_action = uaction.lower()
    user_action = user_action.strip()        # Remove The spaces
    print("***"*10)
    match user_action:
        case 'add':
            todo = input("Enter To Do : ")
            todos.append(todo)
        case 'show':
            for index , value in enumerate(todos):
                row = f"{index + 1}-{value.title()}"
                print(row)
        case 'edit':
            number = int(input("Enter number of To Do in list to Edit : "))
            number -= 1                        # list indexing start from 0
            todos[number] = input("Enter the new To Do : ")
        case 'complete':                       #  Complete Feature using pop method 
            number = int(input("Enter number of To Do in list to Complete : "))
            todos.pop(number - 1)
        case 'exit':
            break
    
print("Bye___")
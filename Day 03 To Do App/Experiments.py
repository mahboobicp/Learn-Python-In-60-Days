# 1. Experiment with match case with bitwise operator OR |
# 2. Experiment with match case if user input some thing else in match case use _ whatever variable
# 3. Experiment with For loop

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
        case 'show' | 'disply':       # Bitwise operator
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case _:                        # in case of un match inpute this code will be executed
            print("Incorrect Input Try again ...")
print("Bye___")
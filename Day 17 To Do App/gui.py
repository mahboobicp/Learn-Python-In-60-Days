import FreeSimpleGUI as sg
import function
label = sg.Text("To Do Item :")
input_box = sg.InputText(tooltip="Enter To Do", key="todo")
btn = sg.Button("Add")
list_box = sg.Listbox(values=function.get_todo(), key='todos', 
                      enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window("Todo App GUI",[[label],[input_box,btn],
                                   [list_box,edit_button]
                                   ])

while True:
    event,values = window.read()
    match event:
        case "Add":
            new_todo = values['todo'] + '\n'
            todos = function.get_todo()
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'
            todos = function.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            function.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

    
window.close()

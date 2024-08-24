import FreeSimpleGUI as sg
import function
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt",'w') as file:
        pass
label = sg.Text("To Do Item :")
input_box = sg.InputText(tooltip="Enter To Do", key="todo")
btn = sg.Button("Add")
list_box = sg.Listbox(values=function.get_todo(), key='todos', 
                      enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")
completebtn = sg.Button("Complete")
exitbtn = sg.Button("Exit")
aa = sg.Text('',key='msg')
sg.theme("black")
window = sg.Window("Todo App GUI",[[label],[input_box,btn],
                                   [list_box,edit_button,completebtn],
                                   [exitbtn,aa]
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
            try:    
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'
                todos = function.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                function.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                window['msg'].update(value="First Select an Item")

        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Complete":
            try:
                todo_to_remov = values["todos"][0]
                todos = function.get_todo()
                todos.remove(todo_to_remov)
                function.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value=' ')
            except IndexError:
                window['msg'].update(value="First Select an Item")
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

    
window.close()


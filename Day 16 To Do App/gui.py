import FreeSimpleGUI as sg
import function
label = sg.Text("To Do Item :")
input_box = sg.InputText(tooltip="Enter To Do")
btn = sg.Button("Add")
window = sg.Window("Todo App GUI",[[label],[input_box,btn]])
window.read()
window.close()


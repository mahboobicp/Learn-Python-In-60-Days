import FreeSimpleGUI as sg
import function

lable = sg.InputText(tooltip="Enter To Do")
window = sg.Window("Todo App GUI",[[lable]])
window.read()
window.close()


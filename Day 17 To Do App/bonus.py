import FreeSimpleGUI as sg


lable1 = sg.Text("Select Source Files")
input_box = sg.Input()
btn1 = sg.FilesBrowse("Choose")


lable2 = sg.Text("Select  Destination")
input_box1 = sg.Input()
btn2 = sg.FolderBrowse("Choose")

btn = sg.Button("Compress")

window = sg.Window("File Compresser", layout=[[lable1,input_box,btn1],
                                              [lable2,input_box1,btn2],
                                              [btn]])

window.read()
window.close()
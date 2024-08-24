import FreeSimpleGUI as sg
import os
import parser

lable1 = sg.Text("Select Source Files")
input_box = sg.Input()
btn1 = sg.FilesBrowse("Choose", key="files")


lable2 = sg.Text("Select  Destination ")
input_box1 = sg.Input()
btn2 = sg.FolderBrowse("Choose", key="folder")

btn = sg.Button("Compress")
output_lable =sg.Text(key="msg",text_color="blue")

window = sg.Window("File Compresser", layout=[[lable1,input_box,btn1],
                                              [lable2,input_box1,btn2],
                                              [btn,output_lable]])

while True:
    event,values = window.read()
    print(event,values)
    filepaths = values["files"].split(';')
    
    folder = values['folder']
    print(filepaths)
    print(folder)
    parser.make_archive(filepaths,folder)
    window["msg"].update(value="Compression Completet")
window.close()
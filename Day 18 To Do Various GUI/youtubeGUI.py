import tkinter
import customtkinter as ct
from pytube import YouTube
import pytube
from pytubefix import YouTube
from pytubefix.cli import on_progress

def startDownload():
    try:
        ytLink = link.get()
        yt_object = YouTube(ytLink, on_progress_callback = on_progress)
        #video = ytObject.streams.filter(progressive=True,file_extension="mp4")
        event = dropdown.get()
        #video.get_highest_resolution().download()
        match event:
            case "High Resolution":
                video = yt_object.streams.get_highest_resolution()
                video.download()
            case "Audio":
                video = yt_object.streams.get_audio_only()
                video.download()
            case "Low Resolution":
                video = yt_object.streams.get_lowest_resolution()
                video.download()
            case "-":
                video.get_lowest_resolution().download()
        """ video = ytObject.streams.get_highest_resolution()
        video.download() """
    except:
        print("Youtube link is invalid")
    print("Download Completed")

# Set Theme and color
ct.set_appearance_mode("Dark")
ct.set_default_color_theme("dark-blue")

app = ct.CTk()
app.geometry("300x150")
app.title("Youtube Downloader")
app.grid_columnconfigure(0,weight=1)
app.grid_rowconfigure((0, 1,2,3), weight=1)
#frame = ct.CTkFrame(app, width=500, height=600,border_width=1,border_color="red",)
#frame.pack(padx=20,pady=20)

title = ct.CTkLabel(app,text="Insert video link ..",font=("",14),corner_radius=20)
#title.pack(padx=10,pady=10)
title.grid(row=0,column=0,padx=10,pady=10)
url_var = tkinter.StringVar()
link = ct.CTkEntry(app,width=250,height=30,textvariable=url_var,
                   placeholder_text="Enter the video Link",corner_radius=20,font=("",12))
#link.pack()
link.grid(row=1,column=0,padx=0,pady=0)
res_var = tkinter.StringVar()
dropdown = ct.CTkComboBox(app,values=["High Resolution","Low Resolution","Audio"],
                          height=30,width=150,border_width=1,
                          )
#dropdown.pack(padx=10,pady=10)
dropdown.grid(row=2,column=0,padx=10,pady=10)
btn =ct.CTkButton(app,width=150,height=30,text="Download",command=startDownload,border_width=1)
#btn.pack(padx=10,pady=10)
btn.grid(row=3,column=0,padx=10,pady=10)
app.mainloop()


import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from PIL import Image,ImageTk

root = Tk()
root.title("Text to speech")
root.geometry("900x450+100+100")
root.resizable(False,False)
root.configure(bg="#305065")

engine = pyttsx3.init()


# Read function
def read_text():
  text = text_area.get(1.0,END)
  gender = gender_combobox.get()
  speed = speed_combobox.get()
  print({text},{gender},{speed})
  voices = engine.getProperty('voices')
  print(len(voices))
  print(voices[0])
  def setvoice():
    if (gender == 'Male'):
      engine.setProperty('voice',voices[0].id)
      engine.say(text)
      engine.runAndWait()
    else:
      engine.setProperty('voice',voices[1].id)
      engine.say(text)
      engine.runAndWait()

  if(text):
    if(speed=="Fast"):
      engine.setProperty('rate',250)
      setvoice()
    if(speed=="Normal"):
      engine.setProperty('rate',150)
      setvoice()
    if(speed=="Slow"):
      engine.setProperty('rate',75)
      setvoice()

# Save function
def save():
  text = text_area.get(1.0,END)
  gender = gender_combobox.get()
  speed = speed_combobox.get()
  voices = engine.getProperty('voices')
  def setvoice():
    if (gender == 'Male'):
      engine.setProperty('voice',voices[0].id)
      path = filedialog.asksaveasfilename(filetypes=[("MP3","*.mp3"),("WAV","*.wav")],defaultextension=".mp3")
      filename = path.split("/")[-1]
      print(filename)
      path = path.removesuffix(filename)
      print(path)
      os.chdir(path)
      engine.save_to_file(text, filename)
      engine.runAndWait()
    else:
      engine.setProperty('voice',voices[1].id)
      path = filedialog.asksaveasfilename(filetypes=[("MP3","*.mp3"),("WAV","*.wav")],defaultextension=".mp3")
      filename = path.split("/")[-1]
      print(filename)
      path = path.removesuffix(filename)
      os.chdir(path)
      engine.save_to_file(text, filename)
      engine.runAndWait()

  if(text):
    if(speed=="Fast"):
      engine.setProperty('rate',250)
      setvoice()
    if(speed=="Normal"):
      engine.setProperty('rate',150)
      setvoice()
    if(speed=="Slow"):
      engine.setProperty('rate',75)
      setvoice()


# Sizes
new_size_1 = (70,70)
new_size_2 = (30,30)


# Icon
image_icon = Image.open("speak-icon.png")
# image_icon = ImageTk.PhotoImage(image_icon)
# image_icon = PhotoImage(file="speak-icon.png")
# root.iconphoto(False,image_icon)
root.iconphoto(False,ImageTk.PhotoImage(image_icon))


## Top Frame
Top_frame = Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)

# Mic Image
mic = Image.open("mic.png")
resize_mic = mic.resize(new_size_1)
logo = ImageTk.PhotoImage(resize_mic)
# Logo = PhotoImage(file="mic.png")
Label(Top_frame,image=logo,bg="white").place(x=15,y=10)

# Title
Label(Top_frame,text="Text to speech",font="arial 20 bold", bg="white",fg="black").place(x=100,y=30)




# Text area
text_area = Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)


# Voice selector
Label(root,text="VOICE",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)
gender_combobox =Combobox(root,values=['Male','Female'],font="arial 14",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')


# Speed selector
Label(root,text="SPEED",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=160)
speed_combobox =Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')



# Read Button
image_icon_resize = image_icon.resize(new_size_2)
image_button = ImageTk.PhotoImage(image_icon_resize)
btn=Button(root,text=" Speak!",compound="left",image=image_button,width=130,font="arial 14 bold",command=read_text)
btn.place(x=550,y=280)




# Save button
image_download = Image.open("save.png")
image_download_resize = image_download.resize(new_size_2)
image_save = ImageTk.PhotoImage(image_download_resize)
save=Button(root,text=" Save!",compound="left",image=image_save,width=130,font="arial 14 bold",command=save)
save.place(x=730,y=280)






root.mainloop()

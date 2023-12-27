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


# Voice setter
def setvoice():
  text = text_area.get(1.0,END)
  selected_voice = voice_combobox.get()
  speed = speed_combobox.get()
  voices = engine.getProperty('voices')
  for voice in voices:
    if selected_voice == voice.name:
      selected_voice = voice.id
  if(text and selected_voice):
    if(speed=="Fast"):
      engine.setProperty('rate',250)
    if(speed=="Normal"):
      engine.setProperty('rate',150)
    if(speed=="Slow"):
      engine.setProperty('rate',75)
    engine.setProperty('voice',selected_voice)
    engine.say(text)
    return True, text
  else:
    return False


# Read function
def read_text():
  runs, text = setvoice()
  if runs == True:
    engine.runAndWait()



# Save function
def save():
  runs, text = setvoice()
  if runs == True:
    path = filedialog.asksaveasfilename(filetypes=[("MP3","*.mp3"),("WAV","*.wav")],defaultextension=".mp3")
    filename = path.split("/")[-1]
    print(filename)
    path = path.removesuffix(filename)
    print(path)
    os.chdir(path)
    print(text)
    engine.save_to_file(text, filename)
    engine.runAndWait()



# Sizes
new_size_1 = (70,70)
new_size_2 = (30,30)


# Icon
image_icon = Image.open("speak-icon.png")
root.iconphoto(False,ImageTk.PhotoImage(image_icon))


## Top Frame
Top_frame = Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)

# Mic Image
mic = Image.open("mic.png")
resize_mic = mic.resize(new_size_1)
logo = ImageTk.PhotoImage(resize_mic)
Label(Top_frame,image=logo,bg="white").place(x=15,y=10)

# Title
Label(Top_frame,text="Text to speech",font="arial 20 bold", bg="white",fg="black").place(x=100,y=30)




# Text area
text_area = Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)



# # Selectors

# Speed selector
Label(root,text="SPEED",font="arial 12 bold",bg="#305065",fg="white").place(x=545,y=175)
speed_combobox =Combobox(root,values=['Fast','Normal','Slow'],state='r',width=10)
speed_combobox.place(x=550,y=200)
speed_combobox.set('Normal')


# Voice selector
Label(root,text="VOICE",font="arial 12 bold",bg="#305065",fg="white").place(x=545,y=245)
voices = []
sys_voices = engine.getProperty("voices")
for voice in sys_voices:
  voices.append(voice.name)
voice_combobox = Combobox(root,values=voices,state='r',width=50)
voice_combobox.place(x=550,y=270)
voice_combobox.set(voices[0])



# Read Button
image_icon_resize = image_icon.resize(new_size_2)
image_button = ImageTk.PhotoImage(image_icon_resize)
btn=Button(root,text=" Speak!",compound="left",image=image_button,width=130,font="arial 14 bold",command=read_text)
btn.place(x=550,y=320)




# Save button
image_download = Image.open("save.png")
image_download_resize = image_download.resize(new_size_2)
image_save = ImageTk.PhotoImage(image_download_resize)
save=Button(root,text=" Save!",compound="left",image=image_save,width=130,font="arial 14 bold",command=save)
save.place(x=730,y=320)






root.mainloop()

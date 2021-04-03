from tkinter import *
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry("350x300")
root.configure(bg='ghost white')            #set the GUI window
root.title("R-Tech - [Text to Speech]")


Label(root, text = "TEXT TO SPEECH", font = "arial 20 bold", bg='white smoke').pack()
Label(text ="[R-Tech]", font = 'arial 24 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)             #Prepare the GUI to take input and unmodyfiable text
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)

def Text_to_speech():
    Message = entry_field.get()                     #text to speech operation
    speech = gTTS(text = Message)
    speech.save('rishi.mp3')
    playsound('rishi.mp3')

def Exit():
    root.destroy()            # shuts the script

def Reset():                # reset the fill
    Msg.set("")

Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4', bg = 'Green').place(x=25,y=140)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'Red').place(x=100 , y = 140)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset, bg = 'Yellow').place(x=175 , y = 140)

root.mainloop()                    #start the program
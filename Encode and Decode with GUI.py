from tkinter import *
import base64

#window initialization
root = Tk()                #create window using tinkter
root.geometry('500x300')   #set width and height of the window
root.resizable(0,0)          #make window fixed size
root.title("R-Tech - Message Encoding and Decoding service")             #title if the window

#create text in box  which is not modifiable by user
Label(root, text ='***ENCODE <-> DECODE***', font = 'arial 20 bold').pack()
Label(root, text ='[R-Tech]', font = 'arial 24 bold').pack(side =BOTTOM)       #display the fixed lebel on the window

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()                    #variables declearation

#encoding function
def Encode(key,message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#decoding function
def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]                                       #chr() converts integer to charecter
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))      #ord() converts unicode charecter to integer
    return "".join(dec)

#mode selection function
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

#stop the main loop and exit windows
def Exit():
    root.destroy()

#reset the window
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")                    #set all variables to empty string
    Result.set("")

Label(root, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=60)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)                               #takes input
Label(root, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)
Label(root, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=180, y = 150)
Button(root, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='Blue' ,command = Mode).place(x=220, y = 180)                 #creates button
Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=270, y = 220)
Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'Red', padx=2, pady=2).place(x=180, y = 220)

root.mainloop()           #execute when run
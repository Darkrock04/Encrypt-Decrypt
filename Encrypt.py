from tkinter import *
import base64
from tkinter import messagebox
import tkinter.font as font

def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        list_key = key[i % len(key)]
        list_enc = chr((ord(msg[i]) + ord(list_key)) % 256)
        enc.append(list_enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, code):
    dec = []
    enc = base64.urlsafe_b64decode(code).decode()
    for i in range(len(enc)):
        list_key = key[i % len(key)]
        list_dec = chr((256 + ord(enc[i]) - ord(list_key)) % 256)
        dec.append(list_dec)
    return "".join(dec)

wn = Tk()
wn.geometry("600x400")
wn.configure(bg='#34495E')
wn.title("Encrypt and Decrypt")
wn.resizable(False, False)

Message = StringVar()
key = StringVar()
mode = IntVar()
Output = StringVar()

headingFrame1 = Frame(wn, bg="#16A085", bd=5)
headingFrame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

headingLabel = Label(headingFrame1, text="Encryption and Decryption", fg='white', bg='#16A085', font=('Helvetica', 20, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

label1 = Label(wn, text='Enter the Message', font=('Helvetica', 12), bg='#34495E', fg='white')
label1.place(x=50, y=120)

msg = Entry(wn, textvariable=Message, width=40, font=('Helvetica', 12), bg='#ECF0F1', fg='#34495E', bd=2, relief='groove')
msg.place(x=250, y=120)

label2 = Label(wn, text='Enter the Key', bg='#34495E', fg='white', font=('Helvetica', 12))
label2.place(x=50, y=170)

InpKey = Entry(wn, textvariable=key, width=40, font=('Helvetica', 12), bg='#ECF0F1', fg='#34495E', bd=2, relief='groove')
InpKey.place(x=250, y=170)

label3 = Label(wn, text='Choose Encrypt or Decrypt', font=('Helvetica', 12), bg='#34495E', fg='white')
label3.place(x=50, y=220)

Radiobutton(wn, text='Encrypt', variable=mode, value=1, bg='#34495E', fg='white', selectcolor='#16A085', font=('Helvetica', 10)).place(x=250, y=220)
Radiobutton(wn, text='Decrypt', variable=mode, value=2, bg='#34495E', fg='white', selectcolor='#16A085', font=('Helvetica', 10)).place(x=350, y=220)

label4 = Label(wn, text='Result', font=('Helvetica', 12), bg='#34495E', fg='white')
label4.place(x=50, y=270)

res = Entry(wn, textvariable=Output, width=40, font=('Helvetica', 12), bg='#ECF0F1', fg='#34495E', bd=2, relief='groove')
res.place(x=250, y=270)

def Result():
    msg = Message.get()
    k = key.get()
    i = mode.get()
    if i == 1:
        Output.set(encode(k, msg))
    elif i == 2:
        Output.set(decode(k, msg))
    else:
        messagebox.showinfo('ProjectGurukul', 'Please Choose one of Encryption or Decryption. Try again.')

ShowBtn = Button(wn, text="Show Message", bg='#16A085', fg='white', width=15, height=2, command=Result, font=('Helvetica', 12))
ShowBtn.place(x=50, y=320)

ResetBtn = Button(wn, text='Reset', bg='#E74C3C', fg='white', width=15, height=2, command=lambda: [Message.set(""), key.set(""), mode.set(0), Output.set("")], font=('Helvetica', 12))
ResetBtn.place(x=250, y=320)

QuitBtn = Button(wn, text='Exit', bg='#E74C3C', fg='white', width=15, height=2, command=wn.destroy, font=('Helvetica', 12))
QuitBtn.place(x=450, y=320)

wn.mainloop()
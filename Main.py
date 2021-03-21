from GetMail import EmailHook
from gui import gui
import tkinter.font as tkFont
from gui_frame import *  
from tkinter import *
from PIL import ImageTk, Image

font_normal = tkFont.Font(family="Helvetica",size=12)
font_bold = tkFont.Font(family="Helvetica",size=12,weight="bold")

content.grid(column=0, row=0)
loginPrompt = Label(content, text="Please log in to unlock this window.", background="white", font=font_bold)
loginPrompt.grid(column=0, row=1, columnspan=maxCol, rowspan=1, pady=10)

login_root = Tk()
login_root.title("LOGIN: Gmail Spam +")
login_content = Frame(login_root, width=1500, height=1000, background="white")

email_auth=""

pass_auth=""

login_content.grid(column=0, row=0)

emailLabel = Label(login_content, text="Email", font=font_bold, background="white")
emailLabel.grid(column=0, row=1, padx=10, pady=10)

passLabel = Label(login_content, text="Password", font=font_bold, background="white")
passLabel.grid(column=0, row=2, padx=10, pady=10)

emailEntry = Entry(login_content)
emailEntry.grid(column=1, row=1, padx=10, pady=10)

passEntry = Entry(login_content, show="*")
passEntry.grid(column=1, row=2, padx=10, pady=10)
hook = None

def login():
    global hook
    global email_auth
    global pass_auth
    email_auth = emailEntry.get()
    pass_auth = passEntry.get()
    hook = EmailHook(email_auth, pass_auth, 'imap.gmail.com')
    try:
        g = gui(root, hook)
        login_root.destroy()
        loginPrompt.destroy()
        g.startInbox()
    except:
        emailEntry.delete(0, len(email_auth))
        passEntry.delete(0, len(pass_auth))

signin = Button(login_content, text='Login', command=lambda: login(), font=font_normal)
signin.grid(column=0, row=3, padx=10, pady=10)
login_root.mainloop()


from GetMail import EmailHook
from gui import gui
from tkinter import *
from gui_frame import *

login_root = Tk()
login_content = Frame(login_root, width=1500, height=1000, background="white")

login_content.grid(column=0, row=0)
emailLabel = Label(login_content, text="Email", font=tkFont.Font(family="Helvetica",size=12,weight="bold"))
emailLabel.grid(column=0, row=1, padx=10, pady=10)

passLabel = Label(login_content, text="Password", font=tkFont.Font(family="Helvetica",size=12,weight="bold"))
passLabel.grid(column=0, row=2, padx=10, pady=10)

emailEntry = Entry(login_content)
emailEntry.grid(column=1, row=1, padx=10, pady=10)

passEntry = Entry(login_content, show="*")
passEntry.grid(column=1, row=2, padx=10, pady=10)
hook = None

def login():
    global hook
    email_auth = emailEntry.get()
    pass_auth = passEntry.get()
    hook = EmailHook(email_auth, pass_auth, 'imap.gmail.com')
    try:
        hook.connect()
        print("YES")
        login_root.quit()
    except:
        emailEntry.delete(0, len(email_auth))
        passEntry.delete(0, len(pass_auth))
        print("exception")

signin = Button(login_content, text='Login', command=lambda: login(), font=tkFont.Font(family="Helvetica",size=12))
signin.grid(column=0, row=3, padx=10, pady=10)
login_root.mainloop()
print("mainloop done")

hook = EmailHook(emailEntry.get(), passEntry.get(), 'imap.gmail.com')
hook.connect()

g = gui(root, hook)
g.createGUI()
g.startInbox()
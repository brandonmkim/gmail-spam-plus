from GetMail import EmailHook
from gui import gui
from gui_frame import *
from tkinter import *

g = gui(root, EmailHook("emailtestingmoco@gmail.com", open("pwd.txt","r").read(), 'imap.gmail.com'))
g.createGUI()
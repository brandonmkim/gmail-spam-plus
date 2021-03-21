from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image

# stores basic gui frames separately to be accessed by both main and emailClass
root = Tk()
root.title("Gmail Spam + main")
content = Frame(root, width=1500, height=1000, background="white")
maxCol = 4

# renders banner
bannerFrame = Frame(content, borderwidth=0, relief="flat", width=600)

bannerimg = ImageTk.PhotoImage( Image.open("assets/banner.png") )
banner = Label(content, image=bannerimg, background="white")
bannerFrame.image = bannerimg

bannerFrame.grid(column=0, row=0, columnspan=maxCol, rowspan=1)
banner.grid(column=0, row=0, columnspan=maxCol, rowspan=1, pady=10) 

# initializes fonts
font_normal = tkFont.Font(family="Helvetica",size=12)
font_bold = tkFont.Font(family="Helvetica",size=12,weight="bold")

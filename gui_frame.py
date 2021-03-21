from tkinter import *
import tkinter.font as tkFont

# stores basic gui frames separately to be accessed by both main and emailClass
root = Tk()
root.title("gee mail")
content = Frame(root, width=1000, height=600, background="white")

font_normal = tkFont.Font(family="Helvetica",size=12,weight="bold")

maxCol = 4
maxRow = 5
from tkinter import *
import gui_frame

def renderAllEmails(emailList):
    if len(emailList) > 0:
            row = 1
            for e in emailList:
                e.renderEmail(row)
                row += 1
    else:
        Label(gui_frame.content, text="No more emails! Maybe ask a Nigerian prince for more?", background="white", font=gui_frame.font_normal).grid(column=0, columnspan=gui_frame.maxCol, row=1, pady=8)
from tkinter import *
from gui_frame import *
from PIL import ImageTk, Image

class email:
    # list of all instances
    emailList = []
    
    def __init__(self, person, emailID, subj, body, acc):
        self.person = person
        self.emailID = emailID
        self.subj = subj
        self.subj_elem = Label(content, text=subj)
        self.body = body
        self.body_elem = Label(content, text=body)
        self.acc = acc

        trash = ImageTk.PhotoImage( Image.open("assets/trash.png").resize((36, 36), Image.ANTIALIAS) )
        self.trashButton = Button(content, image=trash, command=self.remove)
        self.trashButton.image = trash

        restore = ImageTk.PhotoImage( Image.open("assets/restore.png").resize((36, 36), Image.ANTIALIAS) )
        self.restoreButton = Button(content, image=restore, command=self.remove)
        self.restoreButton.image = restore
        
        self.row = 0

        email.emailList.append(self)
    
    def getAccuracy(self):
        return self.acc

    @staticmethod
    def sort():
        for i in range(len(email.emailList)):
            for x in range(1,i):
                if(email.emailList[i].getAccuracy() > email.emailList[x].getAccuracy()):
                    email.emailList[i],email.emailList[x] = email.emailList[x],email.emailList[i]

    # calls renderEmail on all emails
    @staticmethod
    def renderAllEmails():
        if len(email.emailList) > 0:
            row = 1
            for e in email.emailList:
                e.renderEmail(row)
                row += 1
        else:
            empty = Label(content, text="No more emails! Maybe ask a Nigerian prince for more?").grid(column=0, columnspan=maxCol, row=1, pady=8)
            

    # creates label and button on gui at newRow
    def renderEmail(self, newRow):
        # renders email
        self.subj_elem.grid(        column=0,           columnspan=maxCol-1,    row=newRow, rowspan=1, padx=8, pady=8, sticky=W)
        self.restoreButton.grid(    column=maxCol-1,    columnspan=1,           row=newRow, rowspan=1, padx=8, pady=8, sticky=E)
        self.trashButton.grid(      column=maxCol,      columnspan=1,           row=newRow, rowspan=1, padx=8, pady=8, sticky=W)
        self.row = newRow
    
    def setId(self, i):
        self.id = i

    def remove(self):
        # removes email from list, and fills in empty space
        email.emailList.pop(email.emailList.index(self))
        # removes rendered emails
        self.subj_elem.destroy()
        self.restoreButton.destroy()
        self.trashButton.destroy()
        # re-renders emails without deleted one
        email.renderAllEmails()
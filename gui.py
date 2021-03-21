from GetMail import EmailHook
from gui_frame import *
from emailClass import emails
from renderAllEmails import *
from PIL import ImageTk, Image

# TODO figure out what to do w/ sorting

class gui:
    def __init__(self,root,eh):
        self.root = root
        self.emailhook = eh
        self.emailhook.connect()
        self.emailhook.addDeleted(root)

    def sort(self):
        for i in range(len(self.emailhook.getEmails())):
            for x in range(i,len(self.emailhook.getEmails())):
                if(self.emailhook.getEmails()[i].getAccuracy() > self.emailhook.getEmails()[x].getAccuracy()):
                    self.emailhook.getEmails()[i],self.emailhook.getEmails()[x] = self.emailhook.getEmails()[x],self.emailhook.getEmails()[i]

    def createGUI(self):
        content.grid(column=0, row=0)
    
    def startInbox(self):
        content.grid_columnconfigure(1, weight=1)
        self.emailhook.loop(root)
        
        counter = 0
        while True:
            if(counter == 20000 or counter == 0):
                self.emailhook.loop(root)
                counter = 1
            else:
                print(counter)
                counter += 1
                try:
                    renderAllEmails(self.emailhook.getEmails())
                except:
                    print("exception in render all")
                self.root.update_idletasks()
                self.root.update()
import threading
from GetMail import EmailHook
from gui import gui
from tkinter import *

class SpamDetector:
    def __init__(self, d, email, pwrd, server):
        self.delay = d
        self.e = email
        self.p = pwrd
        self.s = server
        self.t = Tk()

    def runMailCheck(self):
        gm = EmailHook(self.e,self.p,self.s)
        gm.connect()
        t = threading.Thread(target=gm.loop(self.delay,self.t),name='getEmails')
        t.start()
        t.join()
        
sd = SpamDetector(300,"emailtestingmoco@gmail.com",open("pwd.txt","r").read(),'imap.gmail.com')
sd.runMailCheck()

gui = gui()
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

    def runChecker(self):
        gm = EmailHook(self.e,self.p,self.s)
        gm.connect()
        g = gui(self.t,gm)
        t1 = threading.Thread(target=gm.loop(self.delay,self.t),name='getEmails')
        t2 = threading.Thread(target=g.createGUI(), name='rungui')
        #Run Threads
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        
sd = SpamDetector(300,"emailtestingmoco@gmail.com",open("pwd.txt","r").read(),'imap.gmail.com')
sd.runChecker()

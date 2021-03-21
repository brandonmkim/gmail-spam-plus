# import threading
from GetMail import EmailHook
from gui import gui
from gui_frame import *
from tkinter import *
from multiprocessing import Process

class SpamDetector:
    def __init__(self, d, email, pwrd, server):
        self.delay = d
        self.e = email
        self.p = pwrd
        self.s = server
        self.t = root

    def runChecker(self):
        gm = EmailHook(self.e,self.p,self.s)
        gm.connect()
        g = gui(self.t,gm)


        p1 = Process(target=gm.loop(self.delay,self.t))
        p1.start()
        p2 = Process(target=g.createGUI())
        p2.start()
        
sd = SpamDetector(300,"emailtestingmoco@gmail.com",open("pwd.txt","r").read(),'imap.gmail.com')
sd.runChecker()
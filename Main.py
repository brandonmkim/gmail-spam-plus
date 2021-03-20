import threading
from GetMail import EmailHook

class SpamDetector:
    def __init__(self, d, email, pwrd, server):
        self.delay = d
        self.e = email
        self.p = pwrd
        self.s = server

    def runMailCheck(self):
        gm = EmailHook(self.e,self.p,self.s)
        gm.connect()
        t = threading.Thread(target=gm.getEmails,name='getEmails')
        t.start()
        t.join()
        
sd = SpamDetector(300,"emailtestingmoco@gmail.com",open("pwd.txt","r").read(),'imap.gmail.com')
sd.runMailCheck()
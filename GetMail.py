import email
import imaplib as imap
import time
from emailClass import email as em
import SpamClassifier as sc
import threading

class EmailHook:
    def __init__(self, email, pwrd, server):
        self.address = email
        self.p = pwrd
        self.mail = imap.IMAP4_SSL(server)
        self.texts=[]

    def connect(self):
        self.mail.login(self.address,self.p)
        self.mail.select('inbox')
    
    def loop(self,delay,tk):
        while True:
            status, data = self.mail.search(None, 'ALL')
            ids = []
            for i in data:
                ids += i.split()
            for id in ids:
                emailStatus, emailData = self.mail.fetch(id, '(RFC822)')
                for response_part in emailData:
                    if isinstance(response_part, tuple):
                        encodedEmail = email.message_from_bytes(response_part[1])
                        person = encodedEmail['from']
                        headline = encodedEmail['subject']
                        
                        if encodedEmail.is_multipart():
                            content = ''
                            for i in encodedEmail.get_payload():
                                if i.get_content_type() == 'text/plain':
                                    content = i.get_payload()
                        else:
                            content = encodedEmail.get_payload()

                        newstr = ("Subject: " + headline +" "+ content).replace("\n", "").replace("\r", "")
                        
                        #Predict if email is spam.
                        pred,typ = sc.spamDetect(newstr)
                        print(typ)
                        print(pred)
                        if(pred>0.6 and typ[0]=='spam'):
                            self.texts.append(em(tk,person,id,headline,content,pred))
            
            time.sleep(delay)

    def moveToTrash(self, id):
        status, data = self.mail.search(None, 'ALL')
        ids = data[0].split(b' ')
        self.mail.store(id, '+X-GM-LABELS', '\Trash')

    def permDelete(self, id):
        status, search_data = self.mail.search(None, b'2')
        ids = []
        
        for i in search_data:
            ids += i.split()

        self.mail.store(id, '+X-GM-LABELS', '\Trash')
        self.mail.select('[Gmail]/Trash')
        self.mail.store("1:*", '+FLAGS', '\Deleted')
        self.mail.expunge()

    def getEmails(self):
        return self.texts
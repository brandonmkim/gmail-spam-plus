import PySimpleGUI as sg
from emailClass import email

sg.theme('BluePurple')

inbox = [   [sg.Text('No more emails!', key='-empty-')]]

layout = [  [sg.Column(inbox, key='-INBOX-')],
            [sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
            [sg.Input(key='-IN-')],
            [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('spam email detector', layout)



while True:  # Event Loop
    
    (event, values) = window.read()
    # print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        spam = email("i am nigerian prince", "hehe moneey")
        spam.addGUI(inbox)
        window['-INBOX-'].update(inbox)
        window.refresh()
        print("press")
        print(len(inbox));
        

        
        

window.close()
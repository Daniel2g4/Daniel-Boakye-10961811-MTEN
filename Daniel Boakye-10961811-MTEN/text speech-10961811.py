import PySimpleGUI as sg
import pyttsx3

ttsENGINE = pyttsx3.init()
Voice_type = ttsENGINE.getProperty('voices')

layout = [[sg.Text('Select the type of voice:', text_color='black', background_color='green'),
           sg.Radio('Male', 'RADIO1', default=True, key='Male', background_color='red'),
           sg.Radio('Female', 'RADIO1', key='female', background_color='red')],
          [sg.Text('Enter text to speak:', text_color='white', background_color='purple')],
          [sg.InputText(key='input'), sg.Button('speak', button_color='orange')],
          ]

window = sg.Window('TEXT TO SPEECH', layout, background_color='blue')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'speak':
        text = values['input']
        if values['Male']:
            ttsENGINE.setProperty('voice', Voice_type[0].id)
        elif values['female']:
            ttsENGINE.setProperty('voice', Voice_type[1].id)
        ttsENGINE.say(text)
        ttsENGINE.runAndWait()

window.close()
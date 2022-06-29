import converter
import PySimpleGUI as sg


sg.theme('Dark')

layout = [
    [sg.Text('Bitcoin')],
    [sg.Input(key='IN'), []],
    [sg.Button('Converter')],
    [sg.Text('Real')],
    [sg.Output(key='OUT', size=(50,2))]
    
]

window = sg.Window('Converso de bitcoin para real',layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or  event == 'Cancel':
        break
    if event == 'Converter':
        bitcoin = float(values['IN'])
        real = converter.converter_of_coin(bitcoin)
        print(f'{real:2f}R$')

        
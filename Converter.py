import PySimpleGUI as sg
layout = [
    [sg.Input(key='-INPUT-'),
     sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key='-UNITS-'),
     sg.Button('Convert', key='-CONVERTER-')],
    [sg.Text('Output', key='-OUTPUT-')],
]

window = sg.Window('Converter', layout)
output = 0
output_value = 0
while True:
    event, values = window.read() # an event is triggered by a certain action

    if event == sg.WIN_CLOSED: # closing the window triggers this event
        break
    if event == '-CONVERTER-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km to mile':
                    output = round(float(input_value) * 0.06214, 2)
                    output_value = f'{input_value} kms is now equal to {output} miles'
                case 'kg to pound':
                    output = round(float(input_value) * 2.20462, 2)
                    output_value = f'{input_value} kgs is now equal to {output} pounds'
                case 'sec to min':
                    output = round(float(input_value) / 60, 2)
                    output_value = f'{input_value} secs is now equal to {output} minutes'

            window['-OUTPUT-'].update(output_value)
        else:
            window['-OUTPUT-'].update('Please enter a number')

window.close()

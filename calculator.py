import PySimpleGUI as sg


def create_window(theme):
    sg.theme(theme)
    sg.set_options(font='Franklin 14', button_element_size=(6, 3))
    button_size = (6, 3)
    layout = [
        [sg.Push(), sg.Text('Output', key='-OUTPUT-', font='Franklin 26', right_click_menu=theme_menu)],
        [sg.Button('Clear', key='-CLEAR-', expand_x=True), sg.Button('Enter', key='-ENTER-', expand_x=True, pad=(10, 20))],
        [sg.Button('7', key='7', size=button_size), sg.Button('8', key='8', size=button_size), sg.Button('9', key='9', size=button_size), sg.Button('*', size=button_size)],
        [sg.Button('4', key='4', size=button_size), sg.Button('5', key='5', size=button_size), sg.Button('6', key='6', size=button_size), sg.Button('/', size=button_size)],
        [sg.Button('1', key='1', size=button_size), sg.Button('2', key='2', size=button_size), sg.Button('3', key='3', size=button_size), sg.Button('-', size=button_size)],
        [sg.Button('0', key='0', expand_x=True), sg.Button('.', size=button_size), sg.Button('+', size=button_size)]
              ]
    return sg.Window('Calculator', layout)


theme_menu = ['menu', ['LightGrey1', 'Dark', 'DarkGrey8', 'random']]
window = create_window('Dark')

current_num = []
full_operation = []
while True:
    event, values = window.read() # an event is triggered by a certain action
    if event == sg.WIN_CLOSED: # closing the window triggers this event
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-OUTPUT-'].update(num_string)

    if event in ['+', '/', '-', '*']:
        full_operation.append(''.join(current_num))
        current_num = []
        full_operation.append(event)
        window['-OUTPUT-'].update('')

    if event == '-ENTER-':
        full_operation.append(''.join(current_num))
        result = eval(' '.join(full_operation))
        window['-OUTPUT-'].update(result)
        full_operation = []

    if event == '-CLEAR-':
        current_num = []
        full_operation = []
        window['-OUTPUT-'].update('')

window.close()
import PySimpleGUI as sg
from time import time


def create_window(theme):
    sg.theme(theme)
    button_size = (2, 1)
    point = 0
    layout = [
        [sg.Text(f'Points = {point}', key='-POINT-'), sg.Push(), sg.Button('x', size=button_size, key='-CLOSE-',
                                                                           enable_events=True)],
        [sg.Text('Press Start to Start the Quiz', font='Calibri 12', expand_x=True, pad=(10, 20), key='-QUIZ-')],
        [sg.Text('0.0', font='Calibri 50', key='-TIME-')],
        [sg.Button('Start', button_color=('#FFFFFF', '#FF0000'), border_width=0, key='-STARTSTOP-', size=(5, 1)),
         sg.Button('Theme', button_color=('#FFFFFF', '#FF0000'), border_width=0, key='-THEME-', size=(5, 1),
                   right_click_menu=theme_menu)],
        [sg.Input(key='-INPUT-', visible=False), sg.Button('Enter', button_color=('#FFFFFF', '#FF0000'), border_width=0, key='-ENTER-',
                                            size=(5, 1), visible= False)],
        [sg.Column([[]], key='-COLUMN-')],
        [sg.VPush()]
    ]
    return sg.Window('Quiz', layout,
                     size=(600, 300),
                     no_titlebar=True,
                     element_justification='centre')


theme_menu = ['menu', ['LightGrey1', 'Dark', 'DarkGrey8', 'random']]
window = create_window('Black')

start_time = 0
point = 0
active = False
Questions = ['Who built the first computer?', 'What is the full form of IDE?', 'How many states of matter are there?',
             'Who invented the light bulb?', 'Electricity is measured in?', 'Resistance is measured in?',
             'What is the capital of Pakistan?', 'What is the molecular formula of water?',
             'How many houses in Hogwarts?', '']
p = 0
while True:

    event, values = window.read(timeout=10)

    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

    if event == '-STARTSTOP-':
        window['-QUIZ-'].update('Who is the President of Pakistan?')
        if active:
            #from active to stop
            active = False
            window['-STARTSTOP-'].update('Reset')

        else:
            #from stop to reset
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
                point = 0
                window['-INPUT-'].update(visible=False)
                window['-ENTER-'].update(visible=False)


            else:
                start_time = time()
                active = True
                window['-STARTSTOP-'].update('Stop')

    if active:
        elapsed_time = round(time() - start_time, 1)
        window['-TIME-'].update(elapsed_time)
        window['-INPUT-'].update(visible=True)
        window['-ENTER-'].update(visible=True)

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event == '-ENTER-':
        window['-INPUT-'].update('')
        if values['-INPUT-'] == 'arif alvi':
            point += 1
            window['-POINT-'].update(f'Points = {point}')

        if p <= 9:
            if event == '-ENTER-':
                window['-QUIZ-'].update(Questions[p])
                p += 1
        if p == 10:
            sg.popup(f'Your score is {point}, Your time taken = {elapsed_time}')
            elapsed_time = 0

        if values['-INPUT-'] == 'charles babbage':
            point += 1
            window['-POINT-'].update(f'Points = {point}')

        if values['-INPUT-'] == 'integrated development environment':
            point += 1
            window['-POINT-'].update(f'Points = {point}')

        if values['-INPUT-'] == '3':
            point += 1
            window['-POINT-'].update(f'Points = {point}')

        if values['-INPUT-'] == 'thomas edison':
            point += 1
            window['-POINT-'].update(f'Points = {point}')

        if values['-INPUT-'] == 'watts':
            point += 1
            window['-POINT-'].update(f'Points = {point}')

        if values['-INPUT-'] == 'ohms':
            point += 1
            window['-POINT-'].update(f'Points = {point}')

        if values['-INPUT-'] == 'islamabad':
            point += 1
            window['-POINT-'].update(f'Points = {point}')

        if values['-INPUT-'] == 'h2o':
            point += 1
            window['-POINT-'].update(f'Points = {point}')

        if values['-INPUT-'] == '4':
            point += 1
            window['-POINT-'].update(f'Points = {point}')

window.close()
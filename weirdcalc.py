import PySimpleGUI as sg


def create_window(theme):
    sg.theme(theme)
    sg.set_options(font='Calibri 14', button_element_size=(6, 3))
    button_size = (6, 3)
    layout = [
        [sg.Text('Enter a button', key='-TEXT-', font='Calibri 18', right_click_menu=theme_menu)],
        [sg.Button('Whats This', key='-What-', expand_x=True), sg.Button('Your weird', key='-WEIRD-', expand_x=True)],
        [sg.Button('1', size=button_size), sg.Button('2', size=button_size), sg.Button('3', size=button_size), sg.Button('4', size=button_size)],
        [sg.Button('5', size=button_size), sg.Button('6', size=button_size), sg.Button('7', size=button_size), sg.Button('8', size=button_size)],
        [sg.Button('9', size=button_size), sg.Button('10', size=button_size), sg.Button('11', size=button_size), sg.Button('12', size=button_size)],
        [sg.Button('-Calculate my Weirdness-', expand_x=True, key='-CALCULATOR-')]
        ]
    return sg.Window('Weird Calculator', layout)


theme_menu = ['menu', ['Dark', 'DarkGrey8', 'BlueMono', 'random']]
window = create_window('BlueMono')

while True:
    event , values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event == '1':
        output_value = "Think about these Weird things"
        window['-TEXT-'].update(output_value)
    if event == '2':
        output_value = "Do fish have a thirst for water?"
        window['-TEXT-'].update(output_value)
    if event == '3':
        output_value = "If man developed from monkeys \nwhy do we still have monkeys?"
        window['-TEXT-'].update(output_value)
    if event == '4':
        output_value = "If you punch yourself in the \nface and it hurts are you \nweak or strong?"
        window['-TEXT-'].update(output_value)
    if event == '5':
        output_value = "To kill an elephant how many \nchickens would be required"
        window['-TEXT-'].update(output_value)
    if event == '6':
        output_value = "Is your time truly wasted if \nyou enjoy wasting it?"
        window['-TEXT-'].update(output_value)
    if event == '7':
        output_value = "What’s the color of the mirror?"
        window['-TEXT-'].update(output_value)
    if event == '8':
        output_value = "Have you ever been tempted to \nsleep inside the fridge?\nI know I have"
        window['-TEXT-'].update(output_value)
    if event == '9':
        output_value = "What have you forgotten today?"
        window['-TEXT-'].update(output_value)
    if event == '10':
        output_value = "meow meow \nYes I'm a cat mOve On"
        window['-TEXT-'].update(output_value)
    if event == '11':
        output_value = "Why do you think 11 \nisn’t pronounced onety-one?"
        window['-TEXT-'].update(output_value)
    if event == '12':
        output_value = "Are we really living \nor just slowly dying?"
        window['-TEXT-'].update(output_value)
    if event == '-What-':
        output_value = "A weird calculator :)"
        window['-TEXT-'].update(output_value)
    if event == '-WEIRD-':
        output_value = "Why yes thank you!"
        window['-TEXT-'].update(output_value)
    if event == '-CALCULATOR-':
        output_value = "Congrats! \nYou are 100% weird"
        window['-TEXT-'].update(output_value)

window.close()
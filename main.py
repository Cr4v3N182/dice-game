import PySimpleGUI as sg

sg.theme("DarkBlue15")

label = sg.Text("Press roll to get a result")
p1_roll_button = sg.Button("Player One Roll", key='user1b')
p1_dice_result = sg.Text("Click roll to get a result", key='p1dice')
p2_roll_button = sg.Button("Player Two Roll", key='user2b')
p2_dice_result = sg.Text("Click roll to get a result", key='p2dice')
exit_button = sg.Button("Exit", key="exit", pad=40)

layout = [[label],
          [p1_roll_button, p2_roll_button],
          [p1_dice_result, p2_dice_result],
          [exit_button]]

window = sg.Window("Dice Game", layout=layout, size=(400,200), element_justification='c', font=("Havetica", 10))

while True:
    event, values = window.read()
    match event:
        case "exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
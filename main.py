import PySimpleGUI as sg
from functions import *

sg.theme("DarkBlue15")


label = sg.Text("Press roll to get a result")
p1_roll_button = sg.Button("Player One Roll", key='user1b')
p1_info = sg.Text("", key='p1info')
p1_dice_result = sg.Text("Click roll to get a result", key='p1dice')
p2_roll_button = sg.Button("Player Two Roll", key='user2b')
p2_info = sg.Text("", key='p2info')
p2_dice_result = sg.Text("Click roll to get a result", key='p2dice')
check_result_button = sg.Button("Check", key='check')
output = sg.Text("", key='output')
exit_button = sg.Button("Exit", key="exit")

layout = [[label],
          [p1_roll_button, p2_roll_button],
          [p1_dice_result, p2_dice_result],
          [check_result_button],
          [p1_info, p2_info],
          [output],
          [exit_button]]

window = sg.Window("Dice Game", layout=layout, size=(400,250), element_justification='c', font=("Havetica", 10))

while True:
    event, values = window.read()
    match event:
        case "exit":
            break
        case sg.WIN_CLOSED:
            break
        case "user1b":
            roll_dice1()
            p1_dice_result.update(value=p1_list)
        case "user2b":
            roll_dice2()
            p2_dice_result.update(value=p2_list,text_color="red")


window.close()
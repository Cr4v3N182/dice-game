import PySimpleGUI as sg
from functions import *

sg.theme("DarkBlue15")

label = sg.Text("Press roll to get a result")
p1_roll_button = sg.Button("Player One Roll", key='user1b')
p1_info = sg.Text("", key='p1info')
p1_dice_result = sg.Text("Click roll to get a result", key='p1dice')
p1_score = sg.Text((f"player one score: {s1}").title(), key='p1score')
p2_roll_button = sg.Button("Player Two Roll", key='user2b')
p2_info = sg.Text("", key='p2info')
p2_dice_result = sg.Text("Click roll to get a result", key='p2dice')
p2_score = sg.Text((f"player two score: {s2}").title(), key='p2score')
check_result_button = sg.Button("Check", key='check')
output = sg.Text("", key='output')
exit_button = sg.Button("Exit", key="exit")
clear_button = sg.Button("CE", key='clear')

layout = [[label],
          [p1_roll_button, p2_roll_button],
          [p1_dice_result, p2_dice_result],
          [p1_info, p2_info],
          [check_result_button, clear_button],
          [output],
          [p1_score, exit_button, p2_score]]

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
            p1_info.update(value=f"Player one score: {sum(p1_list)}")
        case "user2b":
            roll_dice2()
            p2_dice_result.update(value=p2_list,text_color="red")
            p2_info.update(value=f"Player two score: {sum(p2_list)}")
        case "check":
            if (sum(p1_list) > sum(p2_list)):
                p1_score
                s1 += 1
                p1_score.update(value=(f"player one score: {s1}").title())
                output.update(value=("player one wins").title())
            elif (sum(p1_list) < sum(p2_list)):
                s2 += 1
                p2_score.update(value=(f"player one score: {s2}").title())
                output.update(value=("player two wins").title())
            else:
                output.update(value=("draw").title())
        case 'clear':
            p1_list = []
            p2_list = []
            p1_dice_result.update(value="")
            p2_dice_result.update(value="")
            continue

window.close()
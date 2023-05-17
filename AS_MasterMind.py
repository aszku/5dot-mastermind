#-------------------------------------------------------------------------------
# Name:        MasterMind
# Author:      anias
# Copyright:   (c) annaszaniawska 2022
#-------------------------------------------------------------------------------

#importy
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from functools import partial
from idlelib.tooltip import Hovertip

password_list = [1,2,3,4,5]
rows_checked = 0

#definitions
def check_action(c,g,x):
    global color_num, color_dict, rows_checked
    white_dots_check_A = []
    white_dots_check_B = []
    for y in password_list_Strings:
        white_dots_check_B.append(y)
##    print("white_dots_check_B = ",white_dots_check_B)

    pass_check = [ GridList[x-5].cget('bg'), GridList[x-4].cget('bg'), GridList[x-3].cget('bg'), GridList[x-2].cget('bg'), GridList[x-1].cget('bg') ]
##    print("pass_check = ",pass_check)
    black_dots = 0
    white_dots = 0
    #
    i=0
    for y in pass_check:
##        print("y = ",y," i = ",i,"password_list_Strings[i] = ",password_list_Strings[i])
        if y == password_list_Strings[i]:
##            print("if")
            black_dots += 1
            white_dots_check_B.remove(y)
##            print("white_dots_check_B = ",white_dots_check_B)
        else:
##            print("else")
            white_dots_check_A.append(y)
        i += 1
    #
    for y in white_dots_check_A:
        if y in white_dots_check_B:
            white_dots += 1
            white_dots_check_B.remove(y)
    #
##    print("black_dots = ",black_dots,"   white_dots = ",white_dots,"  - white_dots_check_A = ",white_dots_check_A)
    if black_dots+white_dots == 0:
        display_check = "No hits!"
    else:
        display_check = black_dots*"⚫" + white_dots*"⚪"
    GridList[x].config(text=display_check, state= DISABLED)
    if x<67:
        GridList[x+6].config(state= NORMAL)
    rows_checked = rows_checked+1
    if black_dots == 5:
        show_Win()

    if rows_checked == 12 and black_dots != 5:
        show_Lose()




def click_color_panel(x):
    global color_num, color_dict
    color_num = x
##    print("Active color is ",color_num)
    active_button.config(bg=color_dict[color_num])
##    active_button.config(text=color_dict[color_num], bg=color_dict[color_num])

def click_color_grid(c,g,x):
    global color_num, color_dict, rows_checked
    if g > 12-rows_checked:
        color_num = (GridList[x].cget('bg'))
        color_num = (list(color_dict.keys())[list(color_dict.values()).index(color_num)])
##        print("Active color is ",color_num)
        active_button.config(bg=color_dict[color_num])
##        active_button.config(text=color_dict[color_num], bg=color_dict[color_num])
    else:
##        print("else; color_num = ",color_num," - color_dict[color_num] = ",color_dict[color_num])
        GridList[x].config(bg=color_dict[color_num])
##        print("else; g = ",g," c = ",c)

def show_Win():
   labelPassword5.config( text="!", bg=color_dict[password_list[0]])
   labelPassword4.config( text="!", bg=color_dict[password_list[1]])
   labelPassword3.config( text="!", bg=color_dict[password_list[2]])
   labelPassword2.config( text="!", bg=color_dict[password_list[3]])
   labelPassword.config( text="!", bg=color_dict[password_list[4]])
   messagebox.showinfo("Win",("Congrats, you have won in " + str(rows_checked) + " turns!"))

def show_Lose():
   labelPassword5.config( text="!", bg=color_dict[password_list[0]])
   labelPassword4.config( text="!", bg=color_dict[password_list[1]])
   labelPassword3.config( text="!", bg=color_dict[password_list[2]])
   labelPassword2.config( text="!", bg=color_dict[password_list[3]])
   labelPassword.config( text="!", bg=color_dict[password_list[4]])
   messagebox.showinfo("Lose","Boo, you haven't made it in 12 turns!")

#how_it_looks
root = Tk()
root.title('MasterMind')
root.geometry("500x800")
root.resizable(0, 0)

frame0 = Frame(root)
frame0.pack()

labelEnter0 = Label(frame0, text="\n How to play?", font=5)

HooverHowToPlay = Hovertip(labelEnter0,'Break the 5-digit password by trial-and-error in max 12 turns. \nSet the code, click "Check" and you will find out how many \nthere are correctly placed pegs (black marks), and how many \nincorrectly placed but still present in password (white marks).')
labelEnter0.grid(row=0,columnspan=2)

frame = Frame(frame0)
frame.grid(row=1,column=0, sticky="", padx=15)

rightframe = Frame(frame0)
rightframe.grid(row=1,column=1, sticky="", padx=15)

color_num = 0

color_dict = { 0 : "White", 1 : "Red", 2 : "Blue", 3 : "Green", 4 : "Yellow", 5 : "Pink", 6 : "Brown", 7 : "Grey", 8: "Violet"}

GridList = list(range(12*6))
##print("Len GridList ",len(GridList))
g = 12
c = 1

for i in range(5):
    frame.columnconfigure(i, weight=1)
frame.columnconfigure(5, weight=5)

for x in GridList:
    if c > 5:
        GridList[x] = Button(frame, text="<- Check!", width=12, font=("Arial",10), command=partial(check_action,c,g,x), state= DISABLED)
        GridList[x].grid(column=6, row=g, sticky=E)
        g = g - 1
        c = 1
    elif c <= 5:
        GridList[x] = Button(frame, text="⚫", width=2, height=1, font=1, bg=color_dict[0])
        GridList[x].grid(column=c, row=g, sticky=W)
        GridList[x].config(command= partial(click_color_grid,c,g,x))
        c = c + 1

GridList[5].config(state= NORMAL)

color_num = 0

labelAct = Label(rightframe, text="Active color: \n", height=5, font=("Arial",10), fg="gray22")
labelAct.pack( side = TOP )

active_button = Button(rightframe, width=2, height=1, font=1, bg=color_dict[color_num], fg="black", state= DISABLED)
##active_button = Button(rightframe, text=color_dict[color_num], width=2, height=1, font=1, bg=color_dict[color_num], fg="black", state= DISABLED)
active_button.pack()

labelEnter = Label(rightframe, text="\n", font=30)
labelEnter.pack()

#possible colors palette
labelAct2_list = list(range(9))
##print("labelAct2_list = ",labelAct2_list)
for x in labelAct2_list:
    labelAct2_list[x] = Button(rightframe, text=color_dict[x], width=10, font=20, bg=color_dict[x], command=partial(click_color_panel, x))
    labelAct2_list[x].pack()

##password shown

label = Label(rightframe, text="\n Password:", font=30, fg="gray22")
label.pack( )

labelPassword = Button(rightframe, text="?", width=2, height=1, font=1, state= DISABLED)
labelPassword.pack( side = RIGHT )

labelPassword2 = Button(rightframe, text="?", width=2, height=1, font=1, state= DISABLED)
labelPassword2.pack( side = RIGHT )

labelPassword3 = Button(rightframe, text="?", width=2, height=1, font=1, state= DISABLED)
labelPassword3.pack( side = RIGHT )

labelPassword4 = Button(rightframe, text="?", width=2, height=1, font=1, state= DISABLED)
labelPassword4.pack( side = RIGHT )

labelPassword5 = Button(rightframe, text="?", width=2, height=1, font=1, state= DISABLED)
labelPassword5.pack( side = RIGHT )

labelEnter2 = Label(rightframe, text="\n \n", font=30)
labelEnter2.pack()


password_list = [1,2,3,4,5]
for x in range(len(password_list)):
    password_list[x] = random.randint(0, 8)

##print("password_list = ",password_list)

password_list_Strings = []
for x in range(len(password_list)):
    password_list_Strings.append(color_dict[password_list[x]])

##print("password_list_Strings = ",password_list_Strings)

rows_checked = 0


root.mainloop()

from turtle import *
from tkinter import *
from shutil import *
from time import *
import os
from functools import partial

screen = Screen()
screen.title("Minecraft Mod Swapper by RealTaCo201")
screen.setup(width=600, height=430)
screen.bgcolor("black")
canvas = screen.getcanvas()

unused_mods_dir = os.environ["USERPROFILE"] + "\\AppData\\Roaming\\.minecraft\\unusedmods\\"
if not os.path.exists(unused_mods_dir):
    os.makedirs(unused_mods_dir)

mods_dir = os.environ["USERPROFILE"] + "\\AppData\\Roaming\\.minecraft\\mods\\"
if os.path.exists(mods_dir):
    rmtree(mods_dir)
os.makedirs(mods_dir)

replaced = False
prev_screen_height = screen.window_height()
prev_unused_mods_dir = os.listdir(unused_mods_dir)
buttons = []


def replace_mods(from_folder):
    rmtree(mods_dir)
    os.makedirs(mods_dir)
    for file in os.listdir(from_folder):
        copy(from_folder + "\\" + file, mods_dir)
        print(file)
    print(from_folder)
    print("Replaced mods in mod folder!")
    global replaced
    hideturtle()
    color("white")
    goto(0, 143)
    write("Replaced used mods!", align="center", font=("Calibri", 20, "normal"))
    replaced = True


def refresh_folder():
    global buttons
    for button in buttons:
        button.destroy()
    buttons = []
    for folder in os.listdir(unused_mods_dir):
        action_with_arg = partial(replace_mods, unused_mods_dir + folder)
        buttons.append(Button(canvas.master, text=folder, bg="black", fg="white", command=action_with_arg))
        buttons[len(buttons) - 1].config(height=2, width=14)
    refresh()


def refresh():
    y = 0
    x = 0
    for button in buttons:
        button.pack()
        if y * 50 + 35.5 > screen.window_height():
            x += 1
            y = 0
        button.place(x=x * 110 + 10, y=y * 44 + 35.5)
        y += 1


refresh_folder()

while True:
    try:
        screen.update()
        if prev_unused_mods_dir != os.listdir(unused_mods_dir):
            sleep(5)
            refresh_folder()
        prev_unused_mods_dir = os.listdir(unused_mods_dir)
        if prev_screen_height != screen.window_height():
            sleep(5)
            refresh()
        prev_screen_height = screen.window_height()
        if replaced:
            sleep(2)
            color("black")
            write("Replaced used mods!", align="center", font=("Calibri", 20, "normal"))
            replaced = False
    except:
        exit()

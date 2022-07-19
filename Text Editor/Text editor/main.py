from ctypes import resize, sizeof
from itertools import count
from math import fabs
from secrets import choice
import tkinter as tk
from tkinter import Image, image_names, ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

main_application=tk.Tk()
main_application.geometry("1200x800")
main_application.title("TEXT EDITOR")

#=============Main Menu===============#

main_menu=tk.Menu()

#file icons

#new_icon=tk.PhotoImage(file="icons/new1.png")
#open_icon=tk.PhotoImage(file="icons/open.png")
#save_icon=tk.PhotoImage(file="icons/save.png")
#saveas_icon=tk.PhotoImage(file="icons/saveas.png")
#exit_icon=tk.PhotoImage(file="icons/exit.png")


file=tk.Menu(main_menu,tearoff=False)

#file icon command

file.add_command(label="New" ,accelerator="CTRL+N" )
file.add_command(label="Open" ,compound=tk.LEFT ,accelerator="CTRL+O" )
file.add_command(label="Save" ,compound=tk.LEFT ,accelerator="CTRL+S" )
file.add_command(label="Save As" ,compound=tk.LEFT ,accelerator="CTRL+Alt+S" )
file.add_command(label="Exit" ,compound=tk.LEFT ,accelerator="CTRL+Q" )

edit=tk.Menu(main_menu,tearoff=False)

edit.add_command(label="Copy" ,compound=tk.LEFT ,accelerator="CTRL+C" )
edit.add_command(label="Paste" ,compound=tk.LEFT ,accelerator="CTRL+V" )
edit.add_command(label="Cut" ,compound=tk.LEFT ,accelerator="CTRL+X" )
edit.add_command(label="Clear All" ,compound=tk.LEFT ,accelerator="CTRL+Alt+X" )
edit.add_command(label="Find" ,compound=tk.LEFT ,accelerator="CTRL+F" )

view=tk.Menu(main_menu,tearoff=False)

view.add_checkbutton(label="Tool Bar" ,compound=tk.LEFT  )
view.add_checkbutton(label="Status Bar" ,compound=tk.LEFT )


theme=tk.Menu(main_menu,tearoff=False)

theme_choice=tk.StringVar()

color_dict={
      'Light Default':("#000000","ffffff"),
      'Light Plus':("#474747","e0e0e0"),
      'Dark':("#c4c4c4","2d2d2d"),
      'Red':("#2d2d2d","ffe8e8"),
      'Monokai':("#d3b774","474747"),
      'Night Blue':("#ededed","6b9dc2"),

}
count=0
for i in color_dict:
    theme.add_radiobutton(label=i,variable=theme_choice,compound=tk.LEFT)
    count+=1

#cascade
main_menu.add_cascade(label="File",menu=file)
main_menu.add_cascade(label="Edit",menu=edit)
main_menu.add_cascade(label="View",menu=view)
main_menu.add_cascade(label="Theme",menu=theme)
#=============End Main Menu================#


#=============Tool Bar===============#
#=============End Tool Bar================#


#=============Text Editor===============#
#=============End Text Editor================#


#=============Status Bar===============#
#=============End Status Bar================#


#=============Main Menu Functionality===============#
#=============End Main Menu Functionality================#

main_application.config(menu=main_menu)
main_application.mainloop()


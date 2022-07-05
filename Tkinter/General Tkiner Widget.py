from ast import Pass
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory

#global variables for files

inpath_string = ""
outpath_string = ""
file_extention = ""
tab_text_string = ""
tab2_text_string = ""
tab3_text_string = ""
tab4_text_string = ""


#global variables for copy and parsing data


#print_on_gui lets you display text onto text window. 

def print_on_gui(*args, sep=" ", end="\n"):
    text = sep.join(args) + end
    # Set the Text widget's state to normal so that we can edit its text
    text_widget.config(state="normal")
    # Insert the text at the end
    text_widget.insert("end", text)
    # Set the Text widget's state to disabled to disallow the user changing the text
    text_widget.config(state="disabled")

#input directory link
def InputDirectory():
    global inpath_string
    inpath =  askdirectory(title='Select your folder')
    if len(inpath) == 0:
        inpath_string = str(inpath)
        print_on_gui("No input path selected", inpath)
        print_on_gui()
    else:
        inpath_string = str(inpath)
        print_on_gui("This is out in path:", inpath)
        print_on_gui()

#output directory link
def OutPutDirectory():
    global outpath_string
    outpath  = askdirectory(title='Select your folder')
    if len(outpath) == 0:
        outpath_string = str(outpath)
        print_on_gui("No ouput path selected", outpath)
        print_on_gui()
        
    else:
        outpath_string = str(outpath)
        print_on_gui("This is outpath:", outpath)
        print_on_gui()

def file1_file():
    global file_extension
    file_extension = "file1"
    print_on_gui("File extension is file1")
    print_on_gui()

def file2_file():
    global file_extension
    file_extension = "file2"
    print_on_gui("File extension is file2")
    print_on_gui()

#Function for button press. Parses tab information for worksheet
def Tabclick():
    tab_text = tabEntry.get()
    global tab_text_string
    if len(tab_text) == 0:
        tab_text_string = str(tab_text)
        print_on_gui("This is the excel tab is blank")
        print_on_gui()
    else:    
        tab_text_string = str(tab_text)
        print_on_gui("This is the excel tab to record:", tab_text)
        print_on_gui()

#Function for button press. Parses how many rows to skip from worksheet
def Tabclick2():
    global tab2_text_string
    tab_text2 = tabEntry2.get()
    if len(tab_text2) == 0:
        tab2_text_string = str(tab_text2)
        print_on_gui ("How many Roles to skip is blank")
        print_on_gui()
    else:
        tab2_text_string = str(tab_text2)
        print_on_gui("This is how many rows to skip:", tab_text2)
        print_on_gui()

#Function for button press. Parses how many columns to record from worksheet
def tabClick3():
    global tab3_text_string
    tab_text3 = tabEntry3.get()
    if len(tab_text3) == 0:
        tab3_text_string = str(tab_text3)
        print_on_gui ("How many columns to record is blank")
        print_on_gui()
    else:
        tab3_text_string = str(tab_text3)
        print_on_gui("This is the columns to record:", tab_text3)
        print_on_gui()

#Function for button press. Parses how many rows to record from worksheet
def tabClick4():
    global tab4_text_string
    tab4_text_string = tabEntry4.get()
    if len(tab4_text_string)  == 0:
        tab4_text_string = str(tab4_text_string)
        print_on_gui ("How many rows to record is blank")
        print_on_gui()
    else:
        tab4_text_string = str(tab4_text_string)
        print_on_gui("This is how many rows to record:", tab4_text_string)
        print_on_gui()

#Function to copy files..
def copy_files():
    global inpath_string
    global outpath_string

    if len(inpath_string) and len(outpath_string) != 0:
        print_on_gui ("Copying Files")
        copy_files_function(inpath_string, outpath_string)
        print_on_gui()
    elif (len(inpath_string) == 0) and (len(outpath_string) != 0):
        print_on_gui ("Input Directory Missing")
        print_on_gui()
    elif (len(inpath_string) != 0) and (len(outpath_string) == 0):
        print_on_gui ("Output Directory Missing")
        print_on_gui()
    else:
        print_on_gui ("Both Directories are Missing")
        print_on_gui()

#function to parse files
def parse_files():

    global tab_text_string
    global tab2_text_string
    global tab3_text_string
    global tab4_text_string

    if len(tab_text_string) and len(tab2_text_string) and len(tab3_text_string) and len(tab4_text_string) != 0:
        print_on_gui ("All Files Defined")
        print_on_gui()
        parse_file_function(outpath_string, tab_text_string, tab2_text_string, tab3_text_string, tab4_text_string)
    else:
        print_on_gui ("One OR more fields is missing. Please check below")
        print_on_gui()
        print_on_gui ("Tab1:", tab_text_string)
        print_on_gui()
        print_on_gui ("Tab2:", tab2_text_string)
        print_on_gui()
        print_on_gui ("Tab3:", tab3_text_string)
        print_on_gui()
        print_on_gui ("Tab4:", tab4_text_string)
        print_on_gui()
    
#Intiate window
window = Tk()
window.geometry("700x1000")

Program_label = Label(window, text = "File parser", font = (300)).grid(row = 0, columnspan = 3, pady = 50)

Input_label = Label(window, text = "Please select input folder", font = (80)).grid(row= 1, column = 0, pady = 15)

input_button = Button(text="Input",command=InputDirectory).grid(row= 1, column = 1, pady= 15)

Output_label = Label(window, text = "Please select output folder", font = (80)).grid(row= 2, column = 0,pady = 15)

output_button = Button(text="Ouput",command=OutPutDirectory).grid(row= 2, column = 1,  pady = 15)

last_label = Label(window, text = "Which file type?", font = (80)).grid(row= 3, column = 0,pady = 15)

rad2 = Radiobutton(window, text = ".file2", value = 1, command = file2_file).grid(row= 3, column = 1)
rad1 = Radiobutton(window, text = ".file1", value = 2, command= file1_file).grid(row= 3, column = 2)

copy_files_label = Label(window, text = "Copy Files", font = (80)).grid(row= 4, column = 0, pady= 25)
copy_files_button = Button(text="Copy Files",command= copy_files).grid(row= 4, column = 1)

tab_label = Label(window, text = "What is the first tab?", font = (80)).grid(row = 5, column = 0)
tabEntry = Entry(window)
tabEntry.grid(row = 5 , column= 1)
tab_button = Button(text="Enter",command= Tabclick).grid(row = 5, column = 2)

skip_rows_label = Label(window, text = "What is the second tab?", font = (80)).grid(row = 6, column = 0)
tabEntry2 = Entry(window)
tabEntry2.grid(row = 6, column = 1)
skip_rows_button = Button(text="Enter",command= Tabclick2).grid(row = 6, column = 2)

columns_label = Label(window, text = "What is the third tab?", font = (80)).grid(row = 7, column = 0)
tabEntry3 = Entry(window)
tabEntry3.grid(row = 7, column = 1)
columns_label_button = Button(text="Enter",command= tabClick3).grid(row = 7, column = 2)

rows_label = Label(window, text = "What is the forth tab?", font = (80)).grid(row = 8, column = 0)
tabEntry4 = Entry(window)
tabEntry4.grid(row= 8, column = 1)
row_label_button = Button(text="Enter",command= tabClick4).grid(row = 8, column = 2)

parse_files_label = Label(window, text = "Parse Files", font = (80)).grid(row = 9, column = 0, pady = 25)
parse_files_button = Button(text="Parse Files",command= parse_files).grid(row = 9, column = 1)

# Create a new `Text` widget
text_widget = tk.Text(window, state="disabled")
# Show the widget on the screen
text_widget.grid(row = 12, columnspan = 3 )  #fill="both", expand=True)

# #last statement to close window
window.mainloop()

#Linked stuff
#https://poopcode.com/how-to-show-dialog-box-to-select-a-folder-in-python/
#https://stackoverflow.com/questions/67653912/how-do-you-make-tkinter-gui-output-text-from-print_on_gui-statement
# https://stackoverflow.com/questions/59754049/tkinter-gui-field-not-updating-when-user-is-pressing-a-button
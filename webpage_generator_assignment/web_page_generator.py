



##Python: 3.11.7
##
##Date: 7/19/24
##
##Author: Kevin Montano
##
##Purpose:    This python program is part of The Tech Academy Python Course -
##            WEB PAGE GENERATOR ASSIGNMENT
##  
##
##Tested OS:  This code was written and tested to work with macOS Ventura 13.6.4



# module import
import tkinter as tk
from tkinter import *
# module to create and display web docs in browser
import webbrowser
import os


# custom child class for Frame
# this is the ui for the app
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # App title displayed on the top bar of ui window
        self.master.title("Web Page Generator")

        # Label: providing instructions on how to use app ui
        self.instr_lbl = Label(self.master, text = "Enter custom text or click the Default HTML page button")
        # position lbl with grid
        self.instr_lbl.grid(row = 0, padx = (10, 10), pady = (30, 10))

        # Entry: user input field to provide custom text
        # for a simple HTML page
        self.custom_entry = Entry(self.master, width = 110)
        # postion custom_entry with grid
        self.custom_entry.grid(row = 1, columnspan = 3, padx = (10, 10), pady = (8, 20), sticky = W)

        # Button: provides a default webpage upon user click
        # without any custom text
        self.default_btn = Button(self.master, text = "Default HTML Page", width = 30, height = 2, command = self.defaultHTML)
        # Placement of button using grid geo manager
        self.default_btn.grid(row = 2, column = 1, padx = (20, 0), pady = (0, 20))

        # Button: provides a custom webpade upon user click
        # that includes any text in the Entry field
        # a user has provided
        self.custom_btn = Button(self.master, text = 'Submit Custom Text', width = 30, height = 2, command = self.customHTML)
        # position custom_btn in window with grid
        self.custom_btn.grid(row = 2, column = 2, padx = (10, 10), pady = (0, 20), sticky = E)


    # creates and launches a simple html webpage
    # in a new tab for the user's default web browser
    def defaultHTML(self):
        # text to write to html doc
        htmlText = "Stay tuned for our amazing summer sale!"
        # opens file to write into it, creates it if not exist
        htmlFile = open("index.html", "w")
        # html content to add into html doc
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        # 'w' overites all content in opened file
        # write executes the task of adding content into file
        htmlFile.write(htmlContent)
        # close opened file
        htmlFile.close()
        # open html webpage in a new tab in user's default web browser
        webbrowser.open_new_tab("file://" + os.path.realpath("index.html"))

    # creates a custom html webpage
    # from the user's input in custom_entry
    # then opens it in a new tab in user's
    # default web browser
    def customHTML(self):
        # retrieve user input in the entry widget
        usrInput = self.custom_entry.get()

        # create webpage html doc
        htmlDoc = open("customIndex.html", "w")
        
        # insert html markup inclusing user text input into html doc
        htmlDoc.write("<html>\n<body>\n<h1>" + usrInput + "</h1>\n</body>\n</html>")

        # close opened html doc
        htmlDoc.close()

        # open new html doc with custom user input text in a new tab in web browser
        webbrowser.open_new_tab("file://" + os.path.realpath("customIndex.html"))
    

        











if __name__ == "__main__":

    root = tk.Tk()
    app = ParentWindow(root)
    root.mainloop()

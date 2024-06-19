

##Python: 3.11.7
##
##Date: 7/18/24
##
##Author: Kevin Montano
##
##Purpose:    This python program is part of The Tech Academy Python Course -
##            FILE TRANSFER Assignment
##  
##
##Tested OS:  This code was written and tested to work with macOS Ventura 13.6.4


# modules import
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import datetime
import time
import os
import shutil


# class of application tkinter user-uinterface
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")

        # Button to select files from source directory
        self.sourceDir_btn = Button(self.master, text="Select Source", width = 20, command = self.sourceDir)
        # Positions source button in the Frame
        self.sourceDir_btn.grid(row = 0, column = 0, padx = (20, 10), pady = (30, 0))

        # Entry for source directory selection
        self.sourceDir_entry = Entry(width = 75)
        # Postion Entry with same padx and pady to line with button
        self.sourceDir_entry.grid(row = 0, column = 1, padx = (20, 10), pady = (30, 0))

        # Button to select destination for files from the destination directory
        self.destDir_btn = Button(self.master, text="Select Destination", width = 20, command = self.destDir)
        # Positions destination button next row under source button
        self.destDir_btn.grid(row = 1, column = 0, padx = (20, 10), pady = (15, 10))

        # Entry for destrination directory selection
        self.destDir_entry = Entry(width = 75)
        # Positions destination Entry right beside its button to line up
        self.destDir_entry.grid(row = 1, column = 1, columnspan = 2, padx = (20, 10), pady = (15, 10))

        # Button to transfer files
        self.transfer_btn = Button(text = "Transfer Files", width = 20, command = self.transferFiles)
        # Position in the frame
        self.transfer_btn.grid(row = 2, column = 1, padx = (20, 60), pady = (0, 15))

        # Button to exit program
        self.exit_btn = Button(text = "Exit", width = 20, command = self.exit_program)
        # Postion exit btn in the Frame
        self.exit_btn.grid(row = 2, column = 1, padx = (60, 40), pady = (0, 15), sticky = N + E)


    # select source directory
    def sourceDir(self):
        # popup ask user to select a directory 
        selectSrcDir = tkinter.filedialog.askdirectory()

        # .delete() will deletes whatever is in the Entry widget
        self.sourceDir_entry.delete(0, END)
        # insert the user selection to the source Entry
        self.sourceDir_entry.insert(0, selectSrcDir)

    # select destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.destDir_entry.delete(0, END)
        self.destDir_entry.insert(0, selectDestDir)

    # Only transfer files from source dir
    # that have been modified in the last 24 hours
    # into the destination dir
    def transferFiles(self):

        # Gets source directory
        srcDir = self.sourceDir_entry.get()

        # Gets destination directory
        destDir = self.destDir_entry.get()

        # Retrieves a list of files in the source diresctory
        sourceFiles = os.listdir(srcDir)

        # Iterates through the list of each file in the source directory
        for file in sourceFiles:
            
            # Gets the timestamp of the file from its filepath
            try:
                lastModified = os.path.getmtime(srcDir + '/' + file)
            # print error
            except OSError:
                print('The file does not exist or is inaccessible.')

            # The difference bewteen the current time and the file's timestamp
            diff = time.time() - lastModified

            # Check if time modified was less than 1 day = 24 hours = 86400 seconds
            # If so, transfer file to folder
            if diff < 86400.0:
                # move each file from the source to the destination directory
                shutil.move(os.path.join(srcDir, file), os.path.join(destDir, file))
                print(file + ' was successfully transferred.')
            # show file that was not transferred
            else:
                print("'{}'  was not transferred because it was modified over 24 hrs ago.".format(file))
            

    # Once a user clicks on the 'Exit' button
    # this method will execute to terminate main Tkinter Frame and all widgets
    def exit_program(self):
        frame.destroy()
        

        





        


if __name__ == "__main__":

    frame = tk.Tk()
    App = ParentWindow(frame)
    frame.mainloop()




    

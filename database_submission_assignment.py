
# Python: 3.11.7
#
# Author: Kevin Montano
#
# Purpose:  This python program is part of The Tech Academy Python Course -
#           DATABASE SUBMISSION ASSIGNMENT
#           It is a script that creates a SQL database and adds records from
#           a given record all within Python



import sqlite3

#Create database
connect = sqlite3.connect('db_files.db')

# given tuple of fileNames to insert into db table
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#Create table 'fileNames'
def createTableFileNames():
    # with intelligently frees up resources after this code block is done
    with connect:
        # instantiate cursor to perform SQL commands on the database
        cur = connect.cursor()
        #create table via cur.execute()CREATE TABLE command
        cur.execute('CREATE TABLE IF NOT EXISTS tbl_fileNames( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_fileName TEXT \
                    )')
        # must commit the the CREATE TABLE cmd
        connect.commit()
        insertFileNames(fileList)
        
        
# This f() adds file names from a given list (tuple) into the db table 'fileNames'
def insertFileNames(fileList):
    # instantiate cursor obj to perform SQL commands on the database
    cur = connect.cursor()
    # iterate through list and only add filenames whose extensions are .txt
    for fileName in fileList:
        # conditional statement check
        if fileName.endswith('.txt'):
            # Adds a new record with the fileName in the col_fileName of tbl_fileName
            cur.execute('INSERT INTO tbl_fileNames(col_fileName) VALUES (?)', (fileName,))
            # outputs to user the filename after adding it
            print('Added: {} to tbl_fileNames'.format(fileName))


            

# Only runs if this is the main program i.e. not run as a script
if __name__ == '__main__':
    createTableFileNames()
    

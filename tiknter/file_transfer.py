#python 3.10.6
#Author Alexis


#======import section====
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
#======end import=========

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Sets titile of GUI window
        self.master.title("File Transfer")

        #Creates button to sleect files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir) 
        #postitions source button in GUI usinf Tkinker grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        #creates entry for source directory selsecton
        self.source_dir = Entry(width=75)
        #Positions entry id GUI using thkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30,0))


        #Creates button to selesct destination of files from destination directory
        self.destDir_btn = Button( text="Select Destination", width=20, command=self.destDir)
        #Postiions destination button in GUI using tkinter grid()
        #on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        #Creates entry for destination direcroy selection
        self.destination_dir = Entry(width=75)
        #Postions entry in GUI using tkinkter grid() padx and pady are the sames as
        #the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15,10))
 
        #Creates button to transfer file
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #Postions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))
 

        #creates an exit button
        self.exit_btn = (Button(text="Exit", width=20, command=self.exit_program))
        #Position the Exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0,15))                 
        
    #Creates function to select source directory.
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clear the conten that is inserted in teh Entry widget,
        #this allows the path to b inserted into the Entry widget properly.
        self.source_dir.delete(0, END)
        #THhe .instert methond will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)
        

    #Creates funton to select destination directory.
    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        #The .delete(0, End) will clear the the content that is inserted int he Entry widget,
        #this allows the path to e inserted into the Entry widget properly.
        self.destination_dir.delete(0, END)
        #The .insert methon will inser the user selection to the destinatio_dir Entry widget
        self.destination_dir.insert(0, selectDestDir)
 
    #Creates function to transfer files from on dirctory to another         
    def transferFiles(self):
        #Gets source, directiory
        source = self.source_dir.get()
        #Gets destination directory
        destination = self.destination_dir.get()
        #Gets a list of files int he sources directory
        source_files = os.listdir(source)
        #runs throught each files in the source directory
        for i in source_files:
            #moves each file from the source to the destination
            shutil.move(source +'/' + i, destination) 
            print(i + ' was succesfully transfered.')
 
    #Creates function to exit program
    def exit_program(self):
        #root is the main GUI window, the Tkinter destoy method
        #tells python to termite root.mainloop and all widgets inside the GUI window
        root.destroy()

        
if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

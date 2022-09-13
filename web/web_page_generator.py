import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("What does your pet does not need")
        self.btn = Button(self.master, text="101 things your pet DOES NOT need", width=30, height=2, command=self.defaultHTML)
        self.btn.grid( padx=(10,10) , pady=(10,10))
        self.Submit_btn = Button(self.master,text="Submit Custom Text",width=30, height=2, command=self.CustText)
        self.Submit_btn.grid(padx=10,pady=10,sticky="w")
        

        self.displayText = StringVar()
        
        
        self.lblTextEntry = Label(self.master,text='What type of pet do you have?')
        self.lblTextEntry.grid(row=1,column=1,columnspan=3,padx=(10,10),pady=(10,0),sticky='w')

        self.txtEntry = Entry(self.master,text=self.displayText)
        self.txtEntry.grid(row=2,column=1,columnspan=3,padx=(10,10),pady=(5,10),sticky='w')


        

        
    def defaultHTML(self):
        htmlText = "This is a saitire page for people like myself that spoils therr pets a little too much.<br> I do plan on linking all the product on here also, just icase your pet needs one!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" +htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        

    def CustText(self):
        htmlText = self.displayText.get()
        htmlFile = open("index.html","w")
        htmlContent = "<html>\n<body>\n<h1>101 things you "+ htmlText +" DOES NOT NEED</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    

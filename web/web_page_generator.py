import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("What does your pet not need ")
        self.btn = Button(self.master, text="101 things your pet DOES NOT need", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10) , pady=(10,10))


    def defaultHTML(self):
        htmlText = "This is a saitire page for people like myself that spoils therr pets a little too much.<br> I do plan on linking all the product on here also, just icase your pet needs one!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" +htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        


if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    

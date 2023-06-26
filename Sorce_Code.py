import tkinter as tk
import webbrowser

class LinkOpener:
    def __init__(self, master):
        self.master = master
        master.title("DOptimizer")

        
        self.button = tk.Button(master, text="Run", bg="Green", fg="Blue", font=("Helvetica", 24), command=self.open_links)
        self.button.pack(expand=True)

        
        self.footer = tk.Label(master, text="Created by [DanielMGX on Github]", font=("Helvetica", 10))
        self.footer.pack(side="bottom")

    def open_links(self):
       
        links = [
            "https://github.com/hellzerg/optimizer",
            "https://github.com/ChrisTitusTech/winutil",
            "https://pegasun.com/system-utilities"
        ]

        
        for link in links:
            webbrowser.open_new_tab(link)


root = tk.Tk()


root.geometry("300x200")
root.configure(bg="Purple")


link_opener = LinkOpener(root)


root.mainloop()
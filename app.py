import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()




        # self.create_widgets()

    # def create_widgets(self):
    #     self.hi_there = tk.Button(self)
    #     self.hi_there["text"] = "Hello World\nClick Me"
    #     self.hi_there["command"] = self.say_hi
    #     self.hi_there.pack(side="top")

    #     self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
    #     self.quit.pack(side="bottom")

    # def say_hi(self):
    #     print("Hiya, didn't see you there!")


root = tk.Tk()
root.geometry("800x500")
app = Application(master=root)
app.mainloop()
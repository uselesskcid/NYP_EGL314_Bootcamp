import tkinter as tk
import yamaha
import MA3

class GUIApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("OSC Demo")

        self.main_page()

    def main_page(self):
        self.clear_widgets()

        title = tk.Label(self, text="Main Page", font="20")
        title.grid(row=0, column=0, columnspan=3)

        ql1_button = tk.Button(self, text="QL1", font="20", command=self.ql1_page)
        ql1_button.grid(row=1, column=1)

        ma3_button = tk.Button(self, text="MA3", font="20", command=self.ma3_page)
        ma3_button.grid(row=2, column=1)

    def ql1_page(self):
        self.clear_widgets()

        title = tk.Label(self, text="QL1 Page", font="20")
        title.grid(row=0, column=0, columnspan=3)

        functions = ["run_command('set MIXER:Current/InCh/Fader/Level 0 0 1000')",
                     "run_command('set MIXER:Current/InCh/Fader/Level 1 0 1000')",
                     "run_command('set MIXER:Current/InCh/Fader/Level 2 0 1000')"]

        row = 1
        col = 0
        for func in functions:
            button = tk.Button(self, text=func, font="12", command=lambda f=func: eval(f))
            button.grid(row=row, column=col)
            row += 1
            if row > 3:
                row = 1
                col += 1

        back_button = tk.Button(self, text="Back", font="20", command=self.main_page)
        back_button.grid(row=4, column=1)

    def ma3_page(self):
        self.clear_widgets()

        title = tk.Label(self, text="MA3 Page", font="20")
        title.grid(row=0, column=0, columnspan=3)

        functions = ["grandma.send_message(LAPTOP_IP, PORT, '/gma3/cmd', 'Go Sequence 1')"]

        row = 1
        col = 0
        for func in functions:
            button = tk.Button(self, text=func, font="12", command=lambda f=func: eval(f))
            button.grid(row=row, column=col)
            row += 1

        back_button = tk.Button(self, text="Back", font="20", command=self.main_page)
        back_button.grid(row=2, column=1)

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = GUIApp()
    app.mainloop()

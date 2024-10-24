import tkinter as tk
from tkinter import font
from math import sin, cos, tan, log, sqrt, radians

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")

        # Make the window non-resizable
        self.root.resizable(False, False)

        # Custom font for buttons and entry
        self.custom_font = font.Font(family="Helvetica", size=14)

        # Entry field for input and results
        self.entry = tk.Entry(root, width=35, borderwidth=5,
                              font=self.custom_font, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons and place them using grid
        self.create_buttons()

    def create_buttons(self):
        # Number and operator buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3),
            ('sqrt', 6, 0), ('^', 6, 1), ('C', 6, 2), ('DEL', 6, 3)
        ]

        for (text, row, column) in buttons:
            self.create_button(text, row, column)

    def create_button(self, text, row, column):
        btn = tk.Button(self.root, text=text, width=5, height=2,
                        font=self.custom_font,
                        command=lambda: self.click_button(text),
                        bg='lightblue' if text != "C" else 'red',
                        activebackground='lightgreen')
        btn.grid(row=row, column=column, padx=5, pady=5)

    def click_button(self, button):
        if button == '=':
            try:
                result = eval(self.entry.get().replace('^', '**'))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button in ["sin", "cos", "tan", "log", "sqrt"]:
            try:
                value = eval(self.entry.get())
                if button == "sin":
                    result = sin(radians(value))  
                elif button == "cos":
                    result = cos(radians(value))  
                elif button == "tan":
                    result = tan(radians(value)) 
                elif button == "log":
                    result = log(value) if value > 0 else "Error" 
                elif button == "sqrt":
                    result = sqrt(value) if value >= 0 else "Error" 

                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == "C":
            self.clear_entry()
        elif button == "DEL":
            self.delete_char()
        else:
            self.entry.insert(tk.END, button)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def delete_char(self):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current[:-1])

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()

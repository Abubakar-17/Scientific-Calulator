import tkinter as tk
from src.calculator import ScientificCalculator

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("360x600")

        self.calc = ScientificCalculator()
        self.expression = ""

        # Display
        self.entry = tk.Entry(
            root,
            font=("Consolas", 18),
            justify="right"
        )
        self.entry.pack(fill="x", padx=10, pady=10)

        # Buttons
        buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "0",".","=","+",
            "sin","cos","tan","log",
            "sqrt","(",")","C"
        ]

        frame = tk.Frame(root)
        frame.pack()

        row = col = 0
        for btn in buttons:
            tk.Button(
                frame,
                text=btn,
                width=6,
                height=2,
                command=lambda b=btn: self.on_click(b)
            ).grid(row=row, column=col, padx=4, pady=4)

            col += 1
            if col == 4:
                col = 0
                row += 1

    def on_click(self, value):
        if value == "=":
            result = self.calc.evaluate(self.expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
            self.expression = ""
        elif value == "C":
            self.expression = ""
            self.entry.delete(0, tk.END)
        else:
            if value in ["sin", "cos", "tan", "log", "sqrt"]:
                self.expression += value + "("
            else:
                self.expression += value

            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

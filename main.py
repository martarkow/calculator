import tkinter as tk
from tkinter import ttk, messagebox
import math

class KalkulatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalkulator")
        self.master.geometry("400x500")

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.entry_var, font=('Helvetica', 16), bd=10, insertwidth=4, width=14,
                              justify='right')
        self.entry.grid(row=0, column=0, columnspan=5, sticky="nsew")

        buttons = [
            '(', ')', 'C', 'sqrt',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'x^y', '+',
            '='
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            ttk.Button(master, text=button, style="TButton", command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        self.configure_grid()

    def configure_grid(self):
        for i in range(7):
            self.master.grid_columnconfigure(i, weight=1)
            self.master.grid_rowconfigure(i, weight=1)

    def button_click(self, value):
        current_entry = self.entry_var.get()

        if value == '=':
            try:
                result = self.eval_expr(current_entry)
                self.entry_var.set(result)
            except Exception as e:
                messagebox.showerror("Błąd", "Błędne wyrażenie matematyczne")
                self.entry_var.set('')
        elif value == 'x^y':
            self.entry_var.set(current_entry + '**')
        elif value == 'sqrt':
            try:
                result = math.sqrt(float(current_entry))
                self.entry_var.set(result)
            except ValueError:
                messagebox.showerror("Błąd", "Nie można pierwiastkować liczby ujemnej")
                self.entry_var.set('')
        elif value == 'C':
            self.entry_var.set('')
        else:
            self.entry_var.set(current_entry + str(value))

    def eval_expr(self, expr):
        try:
            return eval(expr)
        except (ValueError, SyntaxError):
            raise Exception("Błędne wyrażenie matematyczne")

def main():
    root = tk.Tk()
    style = ttk.Style()
    style.configure("TButton", font=('Helvetica', 12))
    kalkulator_gui = KalkulatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

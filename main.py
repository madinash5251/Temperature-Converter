# main.py

import tkinter as tk
from tkinter import ttk
from app.functions import celsius_conversion, fahrenheit_conversion, clear_entry

def main():
    app = tk.Tk()
    app.title("Temperature Converter")

    celsius_label = ttk.Label(app, text="Celsius:")
    celsius_label.grid(row=0, column=0, padx=10, pady=5)

    celsius_entry = ttk.Entry(app)
    celsius_entry.grid(row=0, column=1, padx=10, pady=5)

    fahrenheit_label = ttk.Label(app, text="Fahrenheit:")
    fahrenheit_label.grid(row=1, column=0, padx=10, pady=5)

    fahrenheit_entry = ttk.Entry(app)
    fahrenheit_entry.grid(row=1, column=1, padx=10, pady=5)

    result_label = ttk.Label(app, text="")
    result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    convert_button = ttk.Button(app, text="Convert", command=lambda: convert_temperature(celsius_entry, fahrenheit_entry, result_label))
    convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    app.bind('<FocusIn>', lambda event: enable_input(event, celsius_entry, fahrenheit_entry))

    app.mainloop()

def convert_temperature(celsius_entry, fahrenheit_entry, result_label):
    if celsius_entry.get():
        celsius_value = float(celsius_entry.get())
        fahrenheit_value = (celsius_value * 9/5) + 32
        result_label.config(text=f"{celsius_value:.2f} degrees Celsius is {fahrenheit_value:.2f} degrees Fahrenheit")
    elif fahrenheit_entry.get():
        fahrenheit_value = float(fahrenheit_entry.get())
        celsius_value = (fahrenheit_value - 32) * 5/9
        result_label.config(text=f"{fahrenheit_value:.2f} degrees Fahrenheit is {celsius_value:.2f} degrees Celsius")

def enable_input(event, celsius_entry, fahrenheit_entry):
    if event.widget == celsius_entry:
        fahrenheit_entry.delete(0, "end")
    elif event.widget == fahrenheit_entry:
        celsius_entry.delete(0, "end")

if __name__ == "__main__":
    main()
#call main
# functions.py

import math

def clear_entry(entry):
    entry.delete(0, "end")
    result_label.config(text="")

def enable_celsius(celsius_entry, fahrenheit_entry):
    fahrenheit_entry.delete(0, "end")
    fahrenheit_entry.config(state="disabled")
    celsius_entry.config(state="normal")

def enable_fahrenheit(celsius_entry, fahrenheit_entry):
    celsius_entry.delete(0, "end")
    celsius_entry.config(state="disabled")
    fahrenheit_entry.config(state="normal")

def celsius_conversion(celsius_entry, result_label):
    celsius_value = celsius_entry.get()
    result = celsius_to_fahrenheit(celsius_value)
    result_label.config(text=result)

def fahrenheit_conversion(fahrenheit_entry, result_label):
    fahrenheit_value = fahrenheit_entry.get()
    result = fahrenheit_to_celsius(fahrenheit_value)
    result_label.config(text=result)

def celsius_to_fahrenheit(celsius_value):
    try:
        celsius_value = float(celsius_value)
        fahrenheit_value = (celsius_value * 9/5) + 32
        return round(fahrenheit_value, 2)
    except ValueError:
        return "Invalid Input"

def fahrenheit_to_celsius(fahrenheit_value):
    try:
        fahrenheit_value = float(fahrenheit_value)
        celsius_value = (fahrenheit_value - 32) * 5/9
        return round(celsius_value, 2)
    except ValueError:
        return "Invalid Input"
#functions
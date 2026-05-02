import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        # Get value from entry and convert to float
        inches = float(entry_inches.get())
        # Calculation: 1 inch = 2.54 cm
        cm = inches * 2.54
        # Update the result label
        label_result.config(text=f"{cm:.2f} cm")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Length Converter")
root.geometry("300x150")

# Input Label and Entry
tk.Label(root, text="Enter Inches:").pack(pady=5)
entry_inches = tk.Entry(root)
entry_inches.pack(pady=5)

# Convert Button (This is where the 'event' is triggered)
btn_convert = tk.Button(root, text="Convert", command=convert)
btn_convert.pack(pady=10)

# Result Label
label_result = tk.Label(root, text="0 cm", font=("Arial", 12, "bold"))
label_result.pack()

# Run the application
root.mainloop()

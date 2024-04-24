import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            result = "Error! Division by zero"
        else:
            result = num1 / num2

    result_label.config(text="Result: " + str(result))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create widgets
label_num1 = tk.Label(root, text="Enter first number:")
entry_num1 = tk.Entry(root)

label_num2 = tk.Label(root, text="Enter second number:")
entry_num2 = tk.Entry(root)

label_operation = tk.Label(root, text="Choose operation:")
operation_var = tk.StringVar(root)
operation_var.set("Addition")
option_menu = tk.OptionMenu(root, operation_var, "Addition", "Subtraction", "Multiplication", "Division")

calculate_button = tk.Button(root, text="Calculate", command=calculate)
result_label = tk.Label(root, text="Result: ")

# Grid layout
label_num1.grid(row=0, column=0, sticky="w")
entry_num1.grid(row=0, column=1)

label_num2.grid(row=1, column=0, sticky="w")
entry_num2.grid(row=1, column=1)

label_operation.grid(row=2, column=0, sticky="w")
option_menu.grid(row=2, column=1)

calculate_button.grid(row=3, column=0, columnspan=2, pady=10)
result_label.grid(row=4, column=0, columnspan=2)

# Run the main event loop
root.mainloop()

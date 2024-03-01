import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = var_operation.get()

    if operation == 'Add':
        result = num1 + num2
    elif operation == 'Subtract':
        result = num1 - num2
    elif operation == 'Multiply':
        result = num1 * num2
    elif operation == 'Divide':
        if num2 == 0:
            result = "Error! Division by zero is not allowed."
        else:
            result = num1 / num2

    label_result.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Simple Calculator")

label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

label_operation = tk.Label(root, text="Select operation:")
label_operation.grid(row=2, column=0, padx=5, pady=5)
var_operation = tk.StringVar(root)
var_operation.set("Add")
optionmenu_operation = tk.OptionMenu(root, var_operation, "Add", "Subtract", "Multiply", "Divide")
optionmenu_operation.grid(row=2, column=1, padx=5, pady=5)

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

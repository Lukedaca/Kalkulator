import tkinter as tk

def press(num):
    entry_var.set(entry_var.get() + str(num))

def clear():
    entry_var.set("")

def evaluate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except:
        entry_var.set("error")

root = tk.Tk()
root.title("Kalkulačka")
root.geometry("400x500")
root.configure(bg="black")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 16), bg="black", fg="white")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("0", 4, 1),
    ("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3),
    ("C", 4, 0), ("=", 4, 2)
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, command=evaluate, bg="green", fg="white", font=("Arial", 16))
    elif text == "C":
        btn = tk.Button(root, text=text, command=clear, bg="green", fg="white", font=("Arial", 16))
    else:
        btn = tk.Button(root, text=text, command=lambda t=text: press(t), bg="green", fg="white", font=("Arial", 16))
    btn.grid(row=row, column=col, sticky="nsew")

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    if i < 4:
        root.grid_columnconfigure(i, weight=1)

root.mainloop()

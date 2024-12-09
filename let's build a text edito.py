import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt",
                                      filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        with open(file, "r") as f:
            txt.delete(1.0, tk.END)
            txt.insert(tk.END, f.read())

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        with open(file, "w") as f:
            f.write(txt.get(1.0, tk.END))
        messagebox.showinfo("Saved", "File saved successfully!")

def clear_text():
    txt.delete(1.0, tk.END)


win = tk.Tk()
win.title("Text Editor")
win.geometry("600x400")

txt = tk.Text(win, wrap="word", font=("Arial", 12))
txt.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

menu = tk.Menu(win)
win.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=win.quit)

edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Clear", command=clear_text)

win.mainloop()

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def saving_file():
    file_location = asksaveasfilename(defaultextension="txt", filetypes=[("Text files", "*.txt"), ["All files","*.*"]])
    if not file_location:
        return 
    with open(file_location,"w") as file_output:
        text = text_edit.get(1.0, tk.END)
        file_output.write(text)
    root.title(f"MY OWN NOTEPAD - {file_location}")

def opening_file():
    file_location = askopenfilename(filetypes=[("Text files", "*.txt"),("All files","*.*")])
    if not file_location:
        return
    text_edit.delete(1.0, tk.END)
    with open(file_location, "r") as file_input:
        text = file_input.read()
        text_edit.insert(tk.END, text)
    root.title(f"MY OWN NOTEPAD - {file_location}")

root = tk.Tk()
root.title("MY OWN NOTEPAD")
root.rowconfigure(0, minsize=800)
root.columnconfigure(1, minsize=800)

text_edit = tk.Text(root)
text_edit.grid(row = 0, column=1, sticky="nsew")

frame_button = tk.Frame(root, relief = tk.RAISED, bd=3)
frame_button.grid(row = 0, column = 0, sticky="ns")

button_open = tk.Button(frame_button, text="OPEN FILE", command=opening_file)
button_open.grid(row=0, column=0, padx=5, pady=5)

button_save = tk.Button(frame_button, text="SAVE AS", command=saving_file)
button_save.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()
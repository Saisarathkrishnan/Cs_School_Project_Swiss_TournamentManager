import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Create a Listbox without a border color
listbox = tk.Listbox(root, highlightthickness=0, selectbackground="blue", selectmode=tk.SINGLE)
listbox.pack(pady=20)

# Insert some items into the Listbox
for item in ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]:
    listbox.insert(tk.END, item)

root.mainloop()


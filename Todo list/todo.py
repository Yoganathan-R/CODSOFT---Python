import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.tasks = []

        self.label = tk.Label(master, text="Add Task:", font=("Arial", 12))
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.task_entry = tk.Entry(master, width=50, font=("Arial", 12))
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.add_button.grid(row=0, column=2, padx=5, pady=5)

        self.task_listbox = tk.Listbox(master, width=50, font=("Arial", 12))
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.update_button = tk.Button(master, text="Update Task", command=self.update_task, bg="#FFA500", fg="white", font=("Arial", 12))
        self.update_button.grid(row=2, column=0, padx=5, pady=5)

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task, bg="#f44336", fg="white", font=("Arial", 12))
        self.remove_button.grid(row=2, column=1, padx=5, pady=5)

        self.save_button = tk.Button(master, text="Save List", command=self.save_list, bg="#009688", fg="white", font=("Arial", 12))
        self.save_button.grid(row=2, column=2, padx=5, pady=5)

        self.load_button = tk.Button(master, text="Load List", command=self.load_list, bg="#2196F3", fg="white", font=("Arial", 12))
        self.load_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        self.task_listbox.bind("<Double-Button-1>", self.update_task_status)  # Bind double click to update task status

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "status": "Pending"})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def remove_task(self, event=None):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "No task selected.")

    def update_task(self, event=None):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            current_task = self.tasks[index]["task"]
            updated_task = simpledialog.askstring("Update Task", f"Update task: '{current_task}'")
            if updated_task:
                self.tasks[index]["task"] = updated_task
                self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "No task selected.")

    def update_task_status(self, event=None):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            status = self.tasks[index]["status"]
            if status == "Pending":
                self.tasks[index]["status"] = "Completed"
            else:
                self.tasks[index]["status"] = "Pending"
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "No task selected.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"{task['task']} - {task['status']}")

    def save_list(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, "w") as file:
                for task in self.tasks:
                    file.write(task["task"] + "," + task["status"] + "\n")
            messagebox.showinfo("Save", "List saved successfully.")

    def load_list(self):
        filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filename:
            self.tasks.clear()
            self.task_listbox.delete(0, tk.END)
            with open(filename, "r") as file:
                for line in file:
                    task, status = line.strip().split(",")
                    self.tasks.append({"task": task, "status": status})
                    self.task_listbox.insert(tk.END, f"{task} - {status}")
            messagebox.showinfo("Load", "List loaded successfully.")

def main():
    root = tk.Tk()
    root.configure(bg="#E0E0E0") 
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

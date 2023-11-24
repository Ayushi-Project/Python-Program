import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        # Task List
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, height=10, width=40)
        self.task_listbox.pack(pady=10)

        # Entry for adding a new task
        self.new_task_entry = tk.Entry(self.root, width=30)
        self.new_task_entry.pack(pady=5)

        # Buttons
        tk.Button(self.root, text="Add Task", command=self.add_task).pack(pady=5)
        tk.Button(self.root, text="Delete Task", command=self.delete_task).pack(pady=5)
        tk.Button(self.root, text="Update Task", command=self.update_task).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.destroy).pack(pady=5)

        # Display tasks
        self.display_tasks()

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        task = self.new_task_entry.get()
        if task:
            self.tasks.append(task)
            self.display_tasks()
            self.new_task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.display_tasks()
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to delete.")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        new_task = self.new_task_entry.get()
        if selected_index and new_task:
            self.tasks[selected_index[0]] = new_task
            self.display_tasks()
            self.new_task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Invalid Update", "Please select a task and enter a new task description.")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
import os


class AdminPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Page")

        self.label_admin = tk.Label(root, text="Admin", font=("Arial", 16))
        self.label_admin.pack(pady=10)

        self.label_emp_num = tk.Label(root, text="Enter Employee Number:")
        self.label_emp_num.pack(pady=5)

        self.entry_emp_num = tk.Entry(root)
        self.entry_emp_num.pack(pady=5)

        self.button_payroll = tk.Button(root, text="Payroll", command=self.open_payroll)
        self.button_payroll.pack(pady=10)

        self.button_emp_info = tk.Button(root, text="Employee Info", command=self.open_employee_info)
        self.button_emp_info.pack(pady=10)

    def open_payroll(self):
        os.system('python ACCOUNTING.py')

    def open_employee_info(self):
        os.system('python HR.py')


if __name__ == "__main__":
    root = tk.Tk()
    app = AdminPage(root)
    root.mainloop()

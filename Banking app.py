import self
import tkinter as tk


class BankApp(tk.Tk):
    def init(self):
        (super().init())
        self.title("Bank App")

# Configure font
    self.font_style = ("Arial", 16)

    # Account type selection
    self.account_type = tk.StringVar()
    self.account_type.set("Savings")
    account_label = tk.Label(self, text="Select Account Type:", font=self.font_style)
    account_label.pack()
    savings_radio = tk.Radiobutton(self, text="Savings", variable=self.account_type, value="Savings", font=self.font_style)
    savings_radio.pack()
    current_radio = tk.Radiobutton(self, text="Current", variable=self.account_type, value="Current", font=self.font_style)
    current_radio.pack()

    # Deposit and Withdraw entry fields
    deposit_label = tk.Label(self, text="Deposit Amount:", font=self.font_style)
    deposit_label.pack()
    self.deposit_entry = tk.Entry(self, font=self.font_style)
    self.deposit_entry.pack()

    withdraw_label = tk.Label(self, text="Withdraw Amount:", font=self.font_style)
    withdraw_label.pack()
    self.withdraw_entry = tk.Entry(self, font=self.font_style)
    self.withdraw_entry.pack()

    # Buttons
    deposit_button = tk.Button(self, text="Deposit", command=self.deposit, font=self.font_style)
    deposit_button.pack()
    withdraw_button = tk.Button(self, text="Withdraw", command=self.withdraw, font=self.font_style)
    withdraw_button.pack()
    balance_button = tk.Button(self, text="Check Balance", command=self.check_balance, font=self.font_style)
    balance_button.pack()

    # Balance display
    self.balance_label = tk.Label(self, text="Current Balance: $0.00", font=self.font_style)
    self.balance_label.pack()

def deposit(self):
    amount = float(self.deposit_entry.get())
    current_balance = float(self.balance_label["text"].split("$")[1])
    new_balance = current_balance + amount
    self.balance_label["text"] = f"Current Balance: ${new_balance:.2f}"

def withdraw(self):
    amount = float(self.withdraw_entry.get())
    current_balance = float(self.balance_label["text"].split("$")[1])
    new_balance = current_balance - amount
    self.balance_label["text"] = f"Current Balance: ${new_balance:.2f}"

def check_balance(self):
    current_balance = float(self.balance_label["text"].split("$")[1])
    tk.messagebox.showinfo("Balance", f"Your current balance is ${current_balance:.2f}")
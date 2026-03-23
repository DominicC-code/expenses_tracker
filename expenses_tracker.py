import time
import json
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit


class Expenses(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 400, 500)
        self.amount = QLineEdit()
        self.category = QLineEdit()
        self.description = QLineEdit()
        self.add_expense = QPushButton("Add Expense")
        self.all_expenses = QLabel("")
        self.total_spent = QLabel("")
        self.expenses = []
        try:
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)
        except:
            self.expenses = []
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        vbox.addWidget(self.amount)
        vbox.addWidget(self.category)
        vbox.addWidget(self.description)
        vbox.addWidget(self.all_expenses)
        vbox.addWidget(self.total_spent)
        vbox.addWidget(self.add_expense)
        self.setLayout(vbox)

        self.amount.setPlaceholderText("Enter amount here (how much money it costs): ")
        self.category.setPlaceholderText("What category is this? (food, games, etc.): ")
        self.description.setPlaceholderText("Give an optional note for this expense ('for birthday, etc.')")

        self.add_expense.setObjectName("Add")

        display_text = ""
        for expense in self.expenses:
            display_text += f"${expense['amount']:.2f} - {expense['category']} - {expense['description']}\n"

        total = 0
        for expense in self.expenses:
            total += expense['amount']

        self.all_expenses.setText(display_text)
        self.total_spent.setText(f"Total: ${total:.2f}")

        self.setStyleSheet("""
            QLabel{
                background-color: rgb(200, 200, 200);
                font-size: 100px
            }
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }
            QPushButton#Add{
                background-color: rgb(111, 196, 87)
            }
            QLineEdit{
                font-size: 30px;
            }
            """)

        self.add_expense.clicked.connect(self.add_expense1)

    def add_expense1(self):
        try:
            amount = float(self.amount.text())
            category = self.category.text().strip()
            description = self.description.text().strip()

            expense = {
                "amount": amount,
                "category": category,
                "description": description
            }

            self.expenses.append(expense)

            display_text = ""
            for expense in self.expenses:
                display_text += f"${expense['amount']:.2f} - {expense['category']} - {expense['description']}\n"

            total = 0
            for expense in self.expenses:
                total += expense['amount']

            self.all_expenses.setText(display_text)
            self.total_spent.setText(f"Total: ${total:.2f}")

            self.category.clear()
            self.description.clear()

            with open("expenses.json", "w") as file:
                json.dump(self.expenses, file)

        except:
            self.amount.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    expenses = Expenses()
    expenses.show()
    sys.exit(app.exec())
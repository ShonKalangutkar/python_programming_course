import matplotlib.pyplot as plt

def main():
    expenses = {} 
    while True:
        expense_name = input("Enter the name of the expense(or 'done' to finish): ")
        if expense_name == 'done':
            break
        expense_amount = float(input(f"enter the amout for {expense_name } : "))
        expenses[expense_name]=expense_amount
        
    plot_expenses(expenses)
        
def plot_expenses(expenses):
    labels = list(expenses.keys())
    values = list(expenses.values())
    
    plt.figure(figsize=(10,7))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.axis('equal')
    plt.title("Expense Breakdown")
    plt.show()
    
if __name__ == "__main__":
    main()
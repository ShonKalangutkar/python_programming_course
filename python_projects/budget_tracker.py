def main():
    income = float(input("Enter your total income: "))
    expenses = {}
    while True:
        expense_name = input("Enter where you've spent your money or enter 'done' to finish: ")
        if expense_name.lower() == 'done':
            break
        expense_amount = float(input("Enter your spenditure: "))
        expenses[expense_name]=expense_amount
        
    total_expenses = sum(expenses.values())
    surplus_or_deficit = income - total_expenses
    
    print("\n Budget summary")
    print(f"Total Income: Rs {round(income,2)}")
    print(f"Total expenses: Rs {round(total_expenses,2)}")
    print(f"Total expenses breakdown:")
    for name, amount in expenses.items():
        print(f"{name}: Rs {round(amount,2)}") 
    print(f"surplus/deficit: Rs{round(surplus_or_deficit,2)}")

if __name__ == "__main__":
    main()   
        
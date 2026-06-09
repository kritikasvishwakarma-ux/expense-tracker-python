#expense tracker.py

expenses = []

# Save all expenses to CSV file
def save_expenses():
    with open("expenses.csv", "w", newline="") as file:
        file.write("Date,category,amount,description\n")

        for expense in expenses:
            file.write(f"{expense['Date']},{expense['category']},{expense['amount']},{expense['description']}\n")

# Show category-wise spending summary
def category_summary():
    if not expenses:
          print("No data available")
          return
    summary={}
    
    for exp in expenses:
        category = exp["category"]
        amount =  exp["amount"]

        if category in summary:
             summary[category] += amount
        else:
            summary[category] = amount
    print("\n----- Category Wise Spending ---")
    for cat, total in summary.items():
         print(f"{cat} -> {total:.2f}")

# Display expenses for a specific month
def monthly_expenses():
    month = input("Enter month (YYYY-MM): ")

    found = []

    for exp in expenses:
        if exp["Date"].startswith(month):
            found.append(exp)

    if not found:
        print("No expenses found for this month.")
        return

    total = 0

    print("\n--- Monthly Expenses ---")
    for exp in found:
        print(f"{exp['Date']} | {exp['category']} | {exp['amount']:.2f}")
        total += exp["amount"]

    print(f"\nTotal for {month}: {total:.2f}")

# Find and display the highest expense
def highest_expense():
    if not expenses:
        print("No data available.")
        return

    highest = expenses[0]

    for exp in expenses:
        if exp["amount"] > highest["amount"]:
            highest = exp

    print("\n--- Highest Expense ---")
    print(f"Date: {highest['Date']}")
    print(f"Category: {highest['category']}")
    print(f"Amount: {highest['amount']:.2f}")
    print(f"Description: {highest['description']}")

# Display overall spending insights
def show_insights():
    if not expenses:
        print("No data available.")
        return

    total = 0
    count = len(expenses)
    highest = expenses[0]

    category_count = {}

    for exp in expenses:
        amount = exp["amount"]
        total += amount

        # highest
        if amount > highest["amount"]:
            highest = exp

        # category grouping
        cat = exp["category"]
        if cat in category_count:
            category_count[cat] += amount
        else:
            category_count[cat] = amount

    avg = total / count

    print("\n===== EXPENSE INSIGHTS =====")
    print(f"Total spent: {total:.2f}")
    print(f"Number of transactions: {count}")
    print(f"Average expense: {avg:.2f}")

    print("\nTop Category:")
    top_cat = max(category_count, key=category_count.get)
    print(f"{top_cat} → {category_count[top_cat]:.2f}")

    print("\nHighest single expense:")
    print(f"{highest['category']} → {highest['amount']:.2f}")

# Add a new expense record
def add_expense():
    try:
        Date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category (e.g., Food, Transport): ")
        amount = float(input("Enter the amount: "))
        description = input("Enter a description (optional): ")
        expense={
            "Date": Date,
            "category": category,
            "amount": amount,
            "description": description
        }
        expenses.append(expense)
        print("expense added successfully!\n")
        save_expenses()
    except ValueError:
            print("Invalid input. Please enter a valid amount.")


# Display all recorded expenses
def view_expenses():
    if not expenses :
        print("no expense in record.")
    else:
        print("\n Recorded Expenses.")
        for idx, expense in enumerate(expenses, start=1):
            print(
                f"{idx}. Date: {expense['Date']}\n"
                f"   Category: {expense['category']}\n"
                f"   Amount: ${expense['amount']:.2f}\n"
                f"   Description: {expense['description']}"
            )

# Calculate and display total expenses
def total_expenses():
    total=0
    for expense in expenses:
        total+=expense["amount"]
    print(f"Number of expenses: {len(expenses)}")
    print(f"total expenses: ${total:.2f}")

# Search expenses by category
def search_expense():
    if not expenses:
        print("No expenses to search.")
    else :
        search_term= input("Enter a search term(category):").lower()
        found_expense= [
            expense for expense in expenses
            if search_term in expense["category"].lower()
        ]
        if found_expense:
            print("\n Search result:")
            
            for idx, expense in enumerate(found_expense, start = 1):
                print(f"\n{idx} Date: {expense['Date']}")
                print(f"Category: {expense['category']}")
                print(f"Amount: ${expense['amount']:.2f}")
                print(f"Description: {expense['description']}")
        else:
            print("No matching expenss found.")

            
# Delete an expense by selecting a matching record
def delete_expense():

    if not expenses:
        print("No expense to delete.")
    else :
        matches=[]
        delete_term= input("Enter the category to delete expense:").lower()
        for expense in expenses:
            if delete_term in expense["category"].lower():
                matches.append(expense)
        if not matches:
            print("no expenses found in given category")
            return
        for idx,expense in enumerate(matches, start = 1):
                print(
                    f"{idx}. Date: {expense['Date']} | "
                    f"Category: {expense['category']} | "
                    f"Amount: ${expense['amount']:.2f}"
                    )
        try:
             choice = int(input("Enter the idx no. for removing specific expense "))
        except ValueError:
            print("please enter a valid number:")
            return
        if 1 <= choice <= len(matches):
                        user_choice= matches[choice-1]
                        expenses.remove(user_choice)
                        save_expenses()
                        print(f"Expense deleted succesfully.")
                        return
        else:
            print("Invalid choice")


def exit_program():
    print("exited program.")

# Load expenses from CSV file when program starts
def load_expense():
    try:
        with open("expenses.csv", "r") as file:
            next(file)

            for line in file:
                line = line.strip()
                parts = line.split(",")

                expense = {
                    "Date": parts[0],
                    "category": parts[1],
                    "amount": float(parts[2]),
                    "description": parts[3]
                }
                expenses.append(expense)
    except (FileNotFoundError, StopIteration):
       pass

# Main menu and program flow
def main():
    print("\n\n----Expense Tracker-----")
    print("\n1. Add expense")
    print("2. View expense")
    print("3. Total expense")
    print("4. Search expense")
    print("5. Delete expense")
    print("6. Category-wise summary")
    print("7. Monthly report")
    print("8. Highest expense")
    print("9. Insight dashboard")
    print("10. Exit ")


    while True :
            try:
                select = int(input("\nenter your choice no. from menu: "))
            except ValueError:
                print("enter valid choice.")
                continue
            if select == 1:
                add_expense()
            elif select == 2:
                view_expenses()
            elif select == 3:
                total_expenses()
            elif select == 4:
                search_expense()
            elif select == 5:
                delete_expense()
            elif select ==6:
                category_summary()
            elif select == 7:
                monthly_expenses()
            elif select == 8:
                highest_expense()
            elif select == 9:
                show_insights()
            elif select == 10:
                exit_program()
                break
            else :
                 print("please enter choice from above option.")

load_expense()
main()

            
             

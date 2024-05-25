# Define empty lists to store expenses
expence_name = []
price = []
day = []
month = []
year = []

# Function to read user input
def read_input():
    while True:
        try:
            n = int(input("How many expenses would you like to enter? "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    for i in range(n):
        expence_name.append(input("Enter expense name: "))
        while True:
            try:
                price.append(float(input("Enter the price: ")))
                break
            except ValueError:
                print("Please enter a valid price.")
        while True:
            try:
                day.append(int(input("Enter the day: ")))
                break
            except ValueError:
                print("Please enter a valid day.")
        while True:
            try:
                month.append(int(input("Enter the month: ")))
                break
            except ValueError:
                print("Please enter a valid month.")
        while True:
            try:
                year.append(int(input("Enter the year: ")))
                break
            except ValueError:
                print("Please enter a valid year.")

# Function to display expenses based on user choice
def display_expenses():
    while True:
        try:
            n = int(input("1. Display year-wise\n2. Display month-wise\n3. Display daily\nEnter your choice: "))
            break
        except ValueError:
            print("Please enter a valid choice.")
    
    if n == 1:
        display(year)
    elif n == 2:
        display(month)
    elif n == 3:
        display(day)
    else:
        print("Please enter a correct choice.")

# Function to display expenses
def display(time_frame):
    for i in range(len(expence_name)):
        print(f"Expense: {expence_name[i]}, Price: {price[i]}, Date: {day[i]}-{month[i]}-{year[i]}")

# Main function to handle user choices
def main():
    while True:
        try:
            choice = int(input("1. Read input\n2. Display\n3. Exit\nEnter your choice: "))
        except ValueError:
            print("Please enter a valid choice.")
            continue
        
        if choice == 1:
            read_input()
        elif choice == 2:
            display_expenses()
        elif choice == 3:
            break
        else:
            print("Please enter a correct choice.")

# Run the main function
if __name__ == "__main__":
    main()

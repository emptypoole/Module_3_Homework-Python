import os
import csv

# Set path to budget_data csv
budget_csv = os.path.join("Resources", "budget_data.csv")

# Create lists for holding profit/loss data
profit_loss = []
month_to_month_profit_loss = []

# Create variables
number_of_months = 0
total_profit_losses = 0
greatest_profit_increase = 0
greatest_profit_month = ""
greatest_profit_decrease = 0
greatest_profit_decrease_month = ""
average_change = 0

# Import the budget_data
with open(budget_csv, 'r', newline='') as csvfile:
    budget_data_reader = csv.reader(csvfile, delimiter=",")

    # Skip header
    csv_header = next(budget_data_reader)

    # Cycle through the rows, count the number of months and tally the profits/losses
    for row in budget_data_reader:
        # Count the number of months
        number_of_months += 1
        # Count the total profit/loss
        total_profit_losses += int(row[1])
        # Find the greatest increase and decrease months
        if int(row[1]) > greatest_profit_increase:
            # Column 0 is month
            greatest_profit_month = (row[0])
            # Column 1 is profit/loss
            greatest_profit_increase = int(row[1])
        elif int(row[1]) < greatest_profit_decrease:
            greatest_profit_decrease_month = (row[0])
            greatest_profit_decrease = int(row[1])
        profit_loss.append(int(row[1]))

# Find the average change
for value in range(len(profit_loss)-1):
    monthly_change = (profit_loss[value + 1]) - profit_loss[value]
    month_to_month_profit_loss.append(monthly_change)
average_change = round((sum(month_to_month_profit_loss) / number_of_months), 2)

# Set the file output
financial_analysis_output_file = os.path.join("Analysis", "Financial Analysis.txt")

# Print to terminal
print("Financial Analysis")
print("-" * 35)
print("Total Number of Months: " + str(number_of_months))
print("The Total Profit/Loss is: $" + str(total_profit_losses))
print("The Average Change is: " + str(average_change))
print("The Greatest Increase in Profits was in " + str(greatest_profit_month) + " with $" + str(greatest_profit_increase))
print("The Greatest Decrease in Profits was in " + str(greatest_profit_decrease_month) + " with $" + str(greatest_profit_decrease))


# Write the required data to file
with open(financial_analysis_output_file, "w", encoding="utf-8") as f:
    f.write("Financial Analysis \n")
    f.write("_____________________\n")
    f.write("Total Number of Months: " + str(number_of_months) + "\n")
    f.write("The Total Profit/Loss is: $" + str(total_profit_losses) + "\n")
    f.write("The Average Change is: " + str(average_change) + "\n")
    f.write("The Greatest Increase in Profits was in " + str(greatest_profit_month) + " with $" + str(greatest_profit_increase) + "\n")
    f.write("The Greatest Decrease in Profits was in " + str(greatest_profit_decrease_month) + " with $" + str(greatest_profit_decrease))
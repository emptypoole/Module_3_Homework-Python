import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")


profit_loss = []
month_to_month_profit_loss = []

number_of_months = 0
total_profit_losses = 0
greatest_profit_increase = 0
greatest_profit_month = ""
greatest_profit_decrease = 0
greatest_profit_decrease_month = ""
average_change = 0

with open(budget_csv, newline='') as csvfile:
    budget_data_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(budget_data_reader)

    for row in budget_data_reader:
        number_of_months += 1
        total_profit_losses += int(row[1])
        if int(row[1]) > greatest_profit_increase:
            # Column 0 is month
            greatest_profit_month = (row[0])
            # Column 1 is profit/loss
            greatest_profit_increase = int(row[1])
        elif int(row[1]) < greatest_profit_decrease:
            greatest_profit_decrease_month = (row[0])
            greatest_profit_decrease = int(row[1])
        profit_loss.append(int(row[1]))

for value in range(len(profit_loss)-1):
    monthly_change = (profit_loss[value + 1]) - profit_loss[value]
    month_to_month_profit_loss.append(monthly_change)

average_change = round((sum(month_to_month_profit_loss) / number_of_months), 2)

financial_analysis_output_file = os.path.join("Analysis", "Financial Analysis.txt")

with open(financial_analysis_output_file, "w", encoding="utf-8") as f:
    f.write("Financial Analysis \n")
    f.write("_____________________\n")
    f.write(" Total Number of Months: " + str(number_of_months) + "\n")
    f.write("The Total Profit/Loss is: $" + str(total_profit_losses) + "\n")
    f.write("The Average Change is: " + str(average_change) + "\n")
    f.write("The Greatest Increase in Profits was in " + str(greatest_profit_month) + " with $" + str(greatest_profit_increase) + "\n")
    f.write("The Greatest Decrease in Profits was in " + str(greatest_profit_decrease_month) + " with $" + str(greatest_profit_decrease))
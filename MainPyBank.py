#!/usr/bin/env python
# coding: utf-8

# In[8]:


import csv

DataFile = "budget_data.csv"
OutputFile = "output_file.txt"

TotalMonths = 0
GreatestIncrease = ["", 0]
GreatestDecrease = ["", 9999999999999999999]
TotalRevenue = 0
PreviousRevenue = 0
MonthChange = []
RevenueChangeList = []

with open(DataFile) as BudgetData:
    csvreader = csv.DictReader(BudgetData)

    for row in csvreader:

        TotalMonths = TotalMonths + 1
        TotalRevenue = TotalRevenue + int(row["Profit/Losses"])

        RevenueChange = int(row["Profit/Losses"]) - PreviousRevenue
        PreviousRrevenue = int(row["Profit/Losses"])
        RevenueChangeList = RevenueChangeList + [RevenueChange]
        MonthChange = MonthChange + [row["Date"]]

        if (RevenueChange > GreatestIncrease[1]):
            GreatestIncrease[0] = row["Date"]
            GreatestIncrease[1] = RevenueChange

        if (RevenueChange < GreatestDecrease[1]):
            GreatestDecrease[0] = row["Date"]
            GreatestDecrease[1] = RevenueChange

RevenueAverageChange = sum(RevenueChangeList) / len(RevenueChangeList)

output = (
    f"Total Months: {TotalMonths}\n"
    f"Total Revenue: ${TotalRevenue}\n"
    f"Average Revenue Change: ${RevenueAverageChange}\n"
    f"Greatest Increase in Revenue: {GreatestIncrease[0]} (${GreatestIncrease[1]})\n"
    f"Greatest Decrease in Revenue: {GreatestDecrease[0]} (${GreatestDecrease[1]})\n"
)

print(output)

with open(OutputFile, "w") as txt_file:
   txt_file.write(output)


# In[ ]:





{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Months: 86\n",
      "Total Revenue: $38382578\n",
      "Average Revenue Change: $446309.0465116279\n",
      "Greatest Increase in Revenue: Feb-2012 ($1170593)\n",
      "Greatest Decrease in Revenue: Sep-2013 ($-1196225)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "\n",
    "DataFile = \"budget_data.csv\"\n",
    "OutputFile = \"output_file.txt\"\n",
    "\n",
    "TotalMonths = 0\n",
    "GreatestIncrease = [\"\", 0]\n",
    "GreatestDecrease = [\"\", 9999999999999999999]\n",
    "TotalRevenue = 0\n",
    "PreviousRevenue = 0\n",
    "MonthChange = []\n",
    "RevenueChangeList = []\n",
    "\n",
    "with open(DataFile) as BudgetData:\n",
    "    csvreader = csv.DictReader(BudgetData)\n",
    "\n",
    "    for row in csvreader:\n",
    "\n",
    "        TotalMonths = TotalMonths + 1\n",
    "        TotalRevenue = TotalRevenue + int(row[\"Profit/Losses\"])\n",
    "\n",
    "        RevenueChange = int(row[\"Profit/Losses\"]) - PreviousRevenue\n",
    "        PreviousRrevenue = int(row[\"Profit/Losses\"])\n",
    "        RevenueChangeList = RevenueChangeList + [RevenueChange]\n",
    "        MonthChange = MonthChange + [row[\"Date\"]]\n",
    "\n",
    "        if (RevenueChange > GreatestIncrease[1]):\n",
    "            GreatestIncrease[0] = row[\"Date\"]\n",
    "            GreatestIncrease[1] = RevenueChange\n",
    "\n",
    "        if (RevenueChange < GreatestDecrease[1]):\n",
    "            GreatestDecrease[0] = row[\"Date\"]\n",
    "            GreatestDecrease[1] = RevenueChange\n",
    "\n",
    "RevenueAverageChange = sum(RevenueChangeList) / len(RevenueChangeList)\n",
    "\n",
    "output = (\n",
    "    f\"Total Months: {TotalMonths}\\n\"\n",
    "    f\"Total Revenue: ${TotalRevenue}\\n\"\n",
    "    f\"Average Revenue Change: ${RevenueAverageChange}\\n\"\n",
    "    f\"Greatest Increase in Revenue: {GreatestIncrease[0]} (${GreatestIncrease[1]})\\n\"\n",
    "    f\"Greatest Decrease in Revenue: {GreatestDecrease[0]} (${GreatestDecrease[1]})\\n\"\n",
    ")\n",
    "\n",
    "print(output)\n",
    "\n",
    "with open(OutputFile, \"w\") as txt_file:\n",
    "   txt_file.write(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

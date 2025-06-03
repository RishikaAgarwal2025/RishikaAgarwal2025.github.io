# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 13:44:56 2025

@author: Group 6
"""

# Importing essential libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyomo.environ import *

# Load the dataset
df = pd.read_excel('BuildMax_Rentals_Dataset_Updated.xlsx')

# Typecasting -  Ensuring 'Date - Week ending with' column is in appropriate datetime format
df["Date - Week ending with"] = pd.to_datetime(df["Date - Week ending with"], errors="coerce")

# Defining indexes or keys for our variables
e = ["Excavator", "Crane", "Bulldozer"]  # Type of eqipment
d = [1, 4, 8, 16]  # Duration in weeks
w = list(df.iloc[:-3, 0])  # Total Number of weeks
for i in range(len(w)):
    w[i] = int(w[i])  # Type casting float to integer

#############################
# Extracting Important data #
#############################

# Starting of week inventory for each equipment, storing in a dictionary

Start_Inventory = {}
for i in range(len(w)):
    Start_Inventory[w[i]] = {
        "Excavator": df.iloc[i, 62],
        "Crane": df.iloc[i, 63],
        "Bulldozer": df.iloc[i, 64]
    }

# Starting of week 1 inventory for all equipments, storing in a dictionary

Week1_Inventory = {}
Week1_Inventory[1] = {
    "Excavator": df.iloc[0, 62],
    "Crane": df.iloc[0, 63],
    "Bulldozer": df.iloc[0, 64]
}

# Returns for that week for each equipment, storing in a dictionary
Returns = {}
for i in range(len(w)):
    Returns[w[i]] = {
        "Excavator": {d[0]: df.iloc[i, 5], d[1]: df.iloc[i, 10], d[2]: df.iloc[i, 15], d[3]: df.iloc[i, 20]},
        "Crane": {d[0]: df.iloc[i, 25], d[1]: df.iloc[i, 30], d[2]: df.iloc[i, 35], d[3]: df.iloc[i, 40]},
        "Bulldozer": {d[0]: df.iloc[i, 45], d[1]: df.iloc[i, 50], d[2]: df.iloc[i, 55], d[3]: df.iloc[i, 60]}
    }

# Demand for that week for each equipment, storing in a dictionary
Demand = {}
for i in range(len(w)):
    Demand[w[i]] = {
        "Excavator": {d[0]: df.iloc[i, 2], d[1]: df.iloc[i, 7], d[2]: df.iloc[i, 12], d[3]: df.iloc[i, 17]},
        "Crane": {d[0]: df.iloc[i, 22], d[1]: df.iloc[i, 27], d[2]: df.iloc[i, 32], d[3]: df.iloc[i, 37]},
        "Bulldozer": {d[0]: df.iloc[i, 42], d[1]: df.iloc[i, 47], d[2]: df.iloc[i, 52], d[3]: df.iloc[i, 57]}
    }

# Price for that week for each equipment, storing in a dictionary
Price = {}
for i in range(len(w)):
    Price[w[i]] = {
        "Excavator": {d[0]: df.iloc[i, 6], d[1]: df.iloc[i, 11], d[2]: df.iloc[i, 16], d[3]: df.iloc[i, 21]},
        "Crane": {d[0]: df.iloc[i, 26], d[1]: df.iloc[i, 31], d[2]: df.iloc[i, 36], d[3]: df.iloc[i, 41]},
        "Bulldozer": {d[0]: df.iloc[i, 46], d[1]: df.iloc[i, 51], d[2]: df.iloc[i, 56], d[3]: df.iloc[i, 61]}
    }

# Defining equipment purchase prices
purchase_price = {
    "Excavator": df.iloc[6, 67],
    "Crane": df.iloc[7, 67],
    "Bulldozer": df.iloc[8, 67]
}

#################
# Create Model  #
#################
model = ConcreteModel()

########################
# Decision Variables   #
########################
model.X = Var(w, e, d,
              domain=NonNegativeIntegers)  # total rental request we accept for each equipment type and their duration for each week
model.R = Var(w, e, domain=NonNegativeIntegers)  # Dynamic returns for each week
model.I = Var(w, e, domain=NonNegativeIntegers)  # Available inventory for each week

########################
# Objective Function   #
########################
model.revenue = Objective(expr=sum(model.X[i, j, k] * Price[i][j][k] * (k * 7) for i in w for j in e for k in d),
                          sense=maximize)

########################
# Constraints          #
########################

# 1. Demand Constraint: Rentals cannot exceed demand
model.demand_constraint = ConstraintList()
for i in w:
    for j in e:
        for k in d:
            model.demand_constraint.add(model.X[i, j, k] <= Demand[i][j][k])

# 2. Returns Constraint: Evaluating Returns of past rentals
model.returns_constraint = ConstraintList()
for i in w:
    for j in e:
        if i - min(d) in w:  # Ensures return period exists in the dataframe
            model.returns_constraint.add(
                model.R[i, j] == sum(model.X[i - k, j, k] for k in d if i - k in w)
            )
        else:
            # model.returns_constraint.add(model.R[i, j] == model.X[1,j,1])
            model.returns_constraint.add(model.R[i, j] == 0)

# 3. Inventory update constraint
model.inventory_constraint = ConstraintList()
for i in w:
    for j in e:
        if i == min(w):  # First week uses initial inventory
            model.inventory_constraint.add(model.I[i, j] == Week1_Inventory[1][j])
        else:
            prev_week = w[w.index(i) - 1]
            model.inventory_constraint.add(
                model.I[i, j] == model.I[prev_week, j] + model.R[i, j] - sum(model.X[prev_week, j, k] for k in d)
            )

# 4. Allocation based on inventory constraint
model.allocation_constraint = ConstraintList()

for i in w:
    for j in e:
        if i == min(w):  # First week uses initial inventory
            model.allocation_constraint.add(
                sum(model.X[i, j, k] for k in d) <= Week1_Inventory[1][j]
            )
        else:  # Subsequent weeks uses rolling inventory (prev_week_balance_inv + returns_recieved_for_prev_week)
            model.allocation_constraint.add(
                sum(model.X[i, j, k] for k in d) <= model.I[i, j]
            )

####################
#   Solving Mode   #
####################

solver = SolverFactory('glpk')
solution = solver.solve(model, tee=False)

########################
# Save Optimized Results#
########################
output = []
for i in w:
    for j in e:
        for k in d:
            output.append([i, j, k, model.X[i, j, k](), model.I[i, j](), model.R[i, j]()])

output = pd.DataFrame(output,
                      columns=["Week", "Equipment", "Duration", "Approved Rentals Count", "Available Inventory Count",
                               "Equipments Returned"])

# Saving output to csv
output.to_csv("approved_rentals_output.csv", index=False)
print("=====================================================================")
print(f"Maximum Revenue: GBP {model.revenue():.2f}")
print("Optimised allocation plan generated as approved_rentals_output.csv in current working directory.")
print("=====================================================================")

###################################
# Extracting Actual Approved Data #
###################################

approved = {}
for i in range(len(w)):
    approved[w[i]] = {
        "Excavator": {d[0]: df.iloc[i, 3], d[1]: df.iloc[i, 8], d[2]: df.iloc[i, 13], d[3]: df.iloc[i, 18],
                      "Inventory": df.iloc[i, 62],
                      "Returns": (df.iloc[i, 5] + df.iloc[i, 10] + df.iloc[i, 15] + df.iloc[i, 20])},
        "Crane": {d[0]: df.iloc[i, 23], d[1]: df.iloc[i, 28], d[2]: df.iloc[i, 33], d[3]: df.iloc[i, 38],
                  "Inventory": df.iloc[i, 63],
                  "Returns": (df.iloc[i, 25] + df.iloc[i, 30] + df.iloc[i, 35] + df.iloc[i, 40])},
        "Bulldozer": {d[0]: df.iloc[i, 43], d[1]: df.iloc[i, 48], d[2]: df.iloc[i, 53], d[3]: df.iloc[i, 58],
                      "Inventory": df.iloc[i, 64],
                      "Returns": (df.iloc[i, 45] + df.iloc[i, 50] + df.iloc[i, 55] + df.iloc[i, 60])}
    }

actual = []
for i in w:
    for j in e:
        for k in d:
            actual.append([i, j, k, approved[i][j][k], approved[i][j]["Inventory"], approved[i][j]["Returns"]])

actual = pd.DataFrame(actual,
                      columns=["Week", "Equipment", "Duration", "Approved Rentals Count", "Available Inventory Count",
                               "Equipments Returned"])

# Save actual approved values to CSV
actual.to_csv("actual_rentals_output.csv", index=False)

print("Actual approved values saved to actual_rentals_output.csv")
("=====================================================================")

# merging actual and optimised action plan for plotting

merged = output.merge(actual, on=["Week", "Equipment", "Duration"], suffixes=("_Optimized", "_Actual"))

###############################################
# Plotting: Optimised Vs Actual Approval Plan #
###############################################

# Creating subplots
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 12), sharex=True)

# Ploting approvals for actual and optimised action plan for each Equipment type
for z, j in enumerate(e):
    ax = axes[z]

    j_data = merged[merged["Equipment"] == j]

    ax.plot(j_data["Week"], j_data["Approved Rentals Count_Optimized"], linestyle='-', marker='o',
            label=f"{j} - Optimized", color='b')
    ax.plot(j_data["Week"], j_data["Approved Rentals Count_Actual"], linestyle='--', marker='s', label=f"{j} - Actual",
            color='r')

    ax.set_ylabel("Approved Rentals Count")
    ax.set_title(f"Optimized vs Actual Approved Rentals - {j}")
    ax.legend()
    ax.grid(True)

# Setting common x-axis label
plt.xlabel("Week")
plt.show()

################################################
# Plotting: Optimised Vs Actual weekly revenue #
################################################

# weekly revenue from both optimized and actual allocations
weekly_revenue = []

for i in w:
    for z in e:
        revenue_optimized = sum(output[(output["Week"] == i) & (output["Equipment"] == z) & (output["Duration"] == k)][
                                    "Approved Rentals Count"].values[0] * Price[i][z][k] * (k * 7) for k in d)
        revenue_actual = sum(approved[i][z][k] * Price[i][z][k] * (k * 7) for k in d)

        weekly_revenue.append([i, z, revenue_optimized, revenue_actual])

# typecasting to dataframe
revenue_df = pd.DataFrame(weekly_revenue, columns=["Week", "Equipment", "Optimized Revenue", "Actual Revenue"])

# Creating subplots for each Equipment type
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 12), sharex=True)

# Plotting weekly revenue(actual vs optimised) for each Equipment type
for z, j in enumerate(e):
    ax = axes[z]

    j_data = revenue_df[revenue_df["Equipment"] == j]

    ax.plot(j_data["Week"], j_data["Optimized Revenue"], linestyle='-', marker='o', label=f"{j} - Optimized Revenue",
            color='g')
    ax.plot(j_data["Week"], j_data["Actual Revenue"], linestyle='--', marker='s', label=f"{j} - Actual Revenue",
            color='r')

    ax.set_ylabel("Revenue (GBP)")
    ax.set_title(f"Weekly Revenue Comparison - {j}")
    ax.legend()
    ax.grid(True)

# Setting common x-axis label
plt.xlabel("Week")
plt.tight_layout()
plt.show()

##############################################################
# Evaluating and Plotting: Optimised Vs Actual total revenue #
##############################################################

# total revenue for each Equipment type
total_revenue = revenue_df.groupby("Equipment")[["Optimized Revenue", "Actual Revenue"]].sum()

# overall total revenue across all Equipment types
total_actual_revenue = total_revenue["Actual Revenue"].sum()
total_optimized_revenue = total_revenue["Optimized Revenue"].sum()

# Printing total revenue values
print("=======================================================")
print("Total Revenue Summary (GBP):")
print(total_revenue)
print("\nOverall Total Revenue (GBP):")
print(f"Optimized Revenue: GBP {total_optimized_revenue:,.2f}")
print(f"Actual Revenue: GBP {total_actual_revenue:,.2f}")
print("=======================================================")

# Plotting bar chart
plt.figure(figsize=(8, 6))
bar_width = 0.4
Equipments = total_revenue.index

# Bar positioning
x = np.arange(len(Equipments) + 1)  # +1 for total revenue

# Adding total revenue as the last row
total_revenue.loc["Total"] = [total_optimized_revenue, total_actual_revenue]

# Plotting the bars
plt.bar(x - bar_width / 2, total_revenue["Optimized Revenue"], bar_width, label="Optimized Revenue", color="blue")
plt.bar(x + bar_width / 2, total_revenue["Actual Revenue"], bar_width, label="Actual Revenue", color="red")

# Labelling and formatting
plt.xlabel("Equipment Type")
plt.ylabel("Total Revenue (GBP)")
plt.title("Total Revenue Comparison (Optimized vs Actual)")
plt.xticks(x, total_revenue.index)  # Set x-axis labels (including 'Total')
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()

#################################################
# Evaluating: Optimised Vs Actual total ROI     #
#################################################

# Calculating total cost for each Equipment using initial inventory
total_Equipment_cost_optimized = sum(Week1_Inventory[1][j] * purchase_price[j] for j in e)
total_Equipment_cost_actual = sum(Week1_Inventory[1][j] * purchase_price[j] for j in e)

# Calculating ROI
roi_optimized = (total_optimized_revenue - total_Equipment_cost_optimized) / total_Equipment_cost_optimized
roi_actual = (total_actual_revenue - total_Equipment_cost_actual) / total_Equipment_cost_actual

# ROI change rate
roi_change = ((roi_optimized - roi_actual) / roi_actual)

# Results
print("=======================================================")
print("Total ROI Summary:")
print(f"Total Equipment Cost (GBP):")
print(f"  - Optimized Plan: GBP {total_Equipment_cost_optimized:,.2f}")
print(f"  - Actual Plan: GBP {total_Equipment_cost_actual:,.2f}")
print(f"\nTotal ROI:")
print(f"  - Optimized ROI: {roi_optimized:.2%}")
print(f"  - Actual ROI: {roi_actual:.2%}")
print(f"  - ROI Change: {roi_change:.2%}")
print("=======================================================")

###################################
# Equipment-wise ROI Calculation  #
###################################

equipment_roi_optimized = {}
equipment_roi_actual = {}

for j in e:
    # Calculate cost using initial inventory
    equipment_cost = Week1_Inventory[1][j] * purchase_price[j]

    # ROI for each equipment type
    equipment_roi_optimized[j] = (total_revenue.loc[j, "Optimized Revenue"] - equipment_cost) / equipment_cost
    equipment_roi_actual[j] = (total_revenue.loc[j, "Actual Revenue"] - equipment_cost) / equipment_cost

# Equipment-wise ROI
print("=======================================================")
print("Equipment-wise ROI (Optimized vs Actual):")
for j in e:
    print(f"{j}:")
    print(f"  - Optimized ROI: {equipment_roi_optimized[j]:.2%}")
    print(f"  - Actual ROI: {equipment_roi_actual[j]:.2%}")
    print(
        f"  - The optimized approval plan changes ROI by {(equipment_roi_optimized[j] - equipment_roi_actual[j]) / equipment_roi_actual[j]:.2%} compared to actual ROI.")
print("=======================================================")
print(
    "Note: Positive changes imply the model has increased profit by said percent against the actual approval plan, while negative values indicate that the model has reduced loss by the given percent compared to actual ROI.")
print("=======================================================")

#######################################
# Plotting: Optimized Vs Actual ROI  #
#######################################

# Converting ROI data to a DataFrame for plotting
roi = pd.DataFrame({
    "Equipment": e,
    "Optimized ROI": [equipment_roi_optimized[j] for j in e],
    "Actual ROI": [equipment_roi_actual[j] for j in e]
})

# Creating subplots for ROI comparison
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 12), sharex=True)

# Plotting ROI for each equipment type
for z, j in enumerate(e):
    ax = axes[z]

    j_data = roi[roi["Equipment"] == j]

    # Plotting bars for ROI
    ax.bar(["Optimized ROI", "Actual ROI"],
           [equipment_roi_optimized[j] * 100, equipment_roi_actual[j] * 100],
           color=["blue", "red"], width=0.4)

    # Formatting
    ax.set_ylabel("ROI (%)")
    ax.set_title(f"Optimized vs Actual ROI - {j}")
    ax.grid(axis="y", linestyle="--", alpha=0.7)

# Setting common x-axis label
plt.xlabel("ROI Type")
plt.tight_layout()
plt.show()
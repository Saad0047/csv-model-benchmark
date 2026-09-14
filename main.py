# Now this is me making the CSV Analyzer by myself, Objective: Make Dataset (whatever) ready for a Model to be trained on it.  
from dataset_loader import csv_finder
import pandas as pd
import os
from dataset_inspection import column_info, pencil_box_list, crayon_box_list
from data_cleaning import dataset_cleaner

# Phase 1:

print("CSV dataset Analyzer")
csv_path = csv_finder() # Get the File Path. 

# Read the csv. 
if csv_path:
    file_name = os.path.basename(csv_path)
    print(f"Selected File: {file_name}")
    df = pd.read_csv(csv_path) 
else:
    print("No File Selected!")

# First 5 enteries. 
print(df.head())
print("-" * 30)

# Count Rows, Columns
rows, columns = df.shape # .shape tells you Rows and Columns. Its an attribute not a Function.
print("Number of Rows and Columns: ")
print()
print(f"Rows: {rows}")
print(f"Columns: {columns}")
print()
print("-" * 30)

# Display the Names of Columns
print()
print("Name of the Columns are as: ")
print()
print(df.columns) # An attribute to find out the names of the Columns.
print("-" * 30)

# Phase 2:

print()
print("Missing Data Report!")
print("-" * 30)

# Missing Values Per Column. 
print(df.isnull().sum()) # isnull() tells Null fields per column, sum() sums values of each object
print("-" * 30)

# Data Type Detection.
print(df.dtypes) # Tells the Data-type of the Columns. 
print("-" * 30)

# Unique Values Per Column. 
print("Number of unique values per column: ")
print()
print(df.nunique())
print("-" * 30)

# Function for Unique Values Detailed
column_info(df)

# Phase 3: Dataset Cleaning Strategies (Later: Add code so its Optional.)

dataset_cleaner(df)

# Phase 4: Data-set Analysis 

# 1. Record Highest and Lowest Value
for i in pencil_box_list: # idxmax and idxmin
    print(f"Column: {i}")

    max_value = df.loc[df[i].idxmax()] 
    print("Max Values: ")
    print(max_value)

    min_value = df.loc[df[i].idxmin()]
    print("Min Values: ")
    print(min_value)

# 2. Corelation Matrix: Tells the trend!
matrix = df[pencil_box_list].corr() # For Consistency it would only be plotted on Specific Categories.
print(matrix)

# 3. Outlier Detector. From the cor-relation, either keep the outliers or Delete the outliers. AI Logic.
def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    print(f"Column: {column}")
    print(f"Normal Range: {lower_bound:.2f} to {upper_bound:.2f}")
    print(f"Number of Outliers Found: {len(outliers)}")
    if len(outliers) > 0:
        print(outliers)
    print()
    return outliers

# Run across every Pencil Box column
for i in pencil_box_list:
    detect_outliers(df, i)

# 4. For Num Values, Record Top 10 and Bottom 10 values. (Only for Pencil-Box Classifiers)
for i in pencil_box_list: # (nlargest and nsmallest)
    top_10 = df.nlargest(10, i)
    bottom_10 = df.nsmallest(10, i)
    print(f"Column Name: {i} ")
    print("Top 10")
    print(top_10)

    print("Bottom 10")
    print(bottom_10)
# Data Cleaning 
import pandas as pd
from dataset_inspection import crayon_box_list, pencil_box_list # Filtered Lists for Data Cleaning 

def remove_duplicates(df): # Remove all of the Duplicates
    print("Remove Duplicates: ")
    print()
    df.drop_duplicates(inplace=True)
    print()

def Apply_Mode(df, column):
    column_mode = df[column].mode()[0] # This takes the very First value of the Mode. MODE means "The Most Frequent".
    print(f"The Mode from this {column} is: {column_mode} ")
    df[column] = df[column].fillna(column_mode) # Missing Data Filled Here!
    print(f"The Missing Data for {column} has been Filled!")

def replace_missing_values(df, column): # Entirely AI Logic
    if df[column].dtypes == "int64":
        skew_value = df[column].skew()
        if abs(skew_value) > 1: # abs() means an Absolute Value. like |-5| to 5 or |3| to 3
            fill_value = df[column].median()
            method = "Median"
        else:
            fill_value = df[column].mean()
            method = "Mean"
        df[column] = df[column].fillna(fill_value)
        print(f"{method} for {column} is {fill_value}. Missing values filled.")
    elif df[column].dtypes == "object":
        Apply_Mode(df, column)
        
def dataset_cleaner(df):
    print("-" * 30)
    print("Data Cleaning: ")
    print()
    while True:
        print("1. Remove Duplicate Values")
        print("2. Replace Missing Values")
        print("3. Fill columns with a Custom Value")
        print()
        choice = input("Choose from the Above: ")
        if choice == "q" or choice == "Q":
            break
        elif choice == "1": # 1. Remove Duplicate Rows: 
            number_of_duplicates = df.duplicated().sum()
            print(f"The Number of Duplicates are: {number_of_duplicates}")
            if number_of_duplicates > 0:
                print()
                print("1. Remove those Duplicates. ")
                print("Leave them be. (Press B or b to quit)")
                print()
                option = input("Your choice is: ")
                if option == "b" or option == "B":
                    break
                elif option == "1":
                    remove_duplicates(df) # Remove Duplicates Function.
                    print("Duplicates have been Removed!")

        elif choice == "2": # 2. Replace Missing Values 
            print()
            for column in crayon_box_list: # For all of the Crayon Box
                while True:
                    print(f"Name of the column: {column}")
                    print()
                    print("1. Apply Mode. ")
                    print("Let it be. (q or Q to quit)")
                    print()
                    choice_crayon = input("Choose one of the Above: ") 
                    if choice_crayon == "q" or choice_crayon == "Q":
                        break
                    if choice_crayon == "1":
                        Apply_Mode(df, column) 

            for column in pencil_box_list: # For all of the Pencil Box 
                while True:
                    print(f"Name of the column: {column}")
                    print()
                    print("1. Replace the Missing Values.")
                    print("let it be. (q or Q to quit)")
                    print()
                    choice_pencil_box = input("Choose one of the Above: ")
                    if choice_pencil_box == "Q" or choice_pencil_box == "q":
                        break
                    if choice_pencil_box == "1":
                        replace_missing_values(df, column)

        elif choice == "3": # 3. Replace with some custom values.
            for column in crayon_box_list:
                while True:
                    print(f"For {column}, Do you want to put a custom values: ")
                    print()
                    print("1. Yes!")
                    print("Q or q to quit.")
                    print()
                    choice_for_custom = input("Choose one of the following: ")
                    if choice_for_custom == "1":
                        custom_value = input("Custom Value: ")
                        df[column] = df[column].fillna(custom_value) 
                        print(f"This column has been filled with {custom_value}")
                    if choice_for_custom == "q" or choice_for_custom == "Q":
                        break
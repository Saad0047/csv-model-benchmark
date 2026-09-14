import pandas as pd 

# Lists 
crayon_box_list = []
pencil_box_list = []
id_classifier_list = []

def crayon_box(df, column): # --> If ratio be less than 0.05, it would mean 2-3 or something of unique values, Hence show it i.e Crayon Box
    counts = df[column].value_counts()
    percentage = df[column].value_counts(normalize = True, dropna = False) * 100
    # This Displays the Percentage along with counts for each of the identified column.
    print(f"Column: {column}")
    print(pd.DataFrame({"Count": counts, "Percentage": percentage.round(2)}))

def pencil_box(df, column): # --> If ratio >= 0.05 or ratio < 0.95, It means more unique values, Perform operations like min,max and avg etc.
    print(f"Lowest value: {df[column].min()}") 
    print(f"Highest value: {df[column].max()}") 
    print(f"Average value: {df[column].mean()}")
    print(f"Missing value: {df[column].isnull().sum()}")
    print(f"Median value: {df[column].median()}")
    print(f"Standard Deviation: {df[column].std():.2f}")
    print(f"Missing values: {df[column].isnull().sum()}")

def ID_classifier(column): # --> If by divison percentage is 1, then it means as many unique values as enteries so some sort of ID. Note: Adds Column, GPT Logic.
    print(f"'{column}' is a highly unique text column.")
    print("It may be an identifier or another unique field.")

def column_info(df):
    # Make a List. 
    col_list = df.columns.to_list() # This will Return all of the Columns to a List.
    print(col_list)
    for column in col_list:
        ratio = df[column].nunique()/len(df) # Explaination: Check all the columns --> Formula = unique_values(column)/total_values 
        print(f"\nColumn: {column}")
        print(f"Ratio: {ratio:.2f}")
        
        # For Datatype object
        if ratio >= 0.95:
            ID_classifier(column)
            id_classifier_list.append(column)

        elif df[column].dtype == "object":
            crayon_box(df, column)
            crayon_box_list.append(column)

        # Numeric column
        else:
            if df[column].nunique() <= 10:
                crayon_box(df, column)
            else:
                pencil_box(df, column)
                pencil_box_list.append(column)
import os
import pandas as pd
from extraction import series_type
folder_path = '../formatted_data'

column_name_1 = "formation"
#column_name_2 = "quels enseignements vous semblent les plus utiles pour l'exercice de votre metier et votre insertion professionnelle ?"
column_name_2= "quels enseignements, absents de votre formation, vous auraient ete utiles ?"
column_list = [column_name_1, column_name_2]

# Initialize an empty DataFrame to store the concatenated data
all_data = pd.DataFrame()

# Loop through all Excel files in the folder
for file_name in os.listdir(folder_path):
    if (file_name.endswith('.xlsx') or file_name.endswith('.xls')) :
        excel_file_path = os.path.join(folder_path, file_name)
        print(f'Processing {excel_file_path}...')
        
        # Load data from the current Excel file
        df = pd.read_excel(excel_file_path)

        # Select two columns from the data frame
        selected_columns = df[column_list]
        
        # Remove rows with missing values
        selected_columns = selected_columns.dropna(subset=column_list)

        # Concatenate the current data with the existing data
        all_data = pd.concat([all_data, selected_columns], ignore_index=True)



# Save the concatenated data to a single CSV file
csv_file_path = 'output_file1.csv'
all_data.to_csv(csv_file_path, index=False)

print(f'Data from all Excel files have been extracted and saved to {csv_file_path}.')

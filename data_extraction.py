import pandas as pd

def read_and_store_data():
    try:
        # Read the CSV file
        df = pd.read_csv('Kaggle_Test_Dataset_v2.csv')

        # Print the top 5 rows
        print(df.head(5))

        # Print success message
        print("Data extraction successful")

        # Store the dataframe to a CSV file
        df.to_csv('data.csv', index=False)

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
read_and_store_data()
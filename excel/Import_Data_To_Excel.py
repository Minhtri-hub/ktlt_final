import pandas as pd
import os
import json

json_file_path = os.path.abspath("../dataset/reservation_data.json")

try:
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)  # Load JSON data


    df = pd.DataFrame(data)


    file_path = os.path.abspath("../excel/reservations.csv")

    try:

        df.to_csv(file_path, index=False, encoding="utf-8-sig", sep=',')
        print(f"Data has been successfully exported to '{file_path}' as individual cells in Excel.")
    except PermissionError:
        print(f"Cannot write to file. Ensure '{file_path}' is not open or locked!")
    except Exception as e:
        print(f"An error occurred while writing to CSV: {e}")

except FileNotFoundError:
    print(f"JSON file not found at '{json_file_path}'. Please check the file path.")
except json.JSONDecodeError as e:
    print(f"Error loading JSON data: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

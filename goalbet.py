import pandas as pd
import requests
from io import StringIO
from sqlalchemy import create_engine
from util import get_database_conn
con = get_database_conn
def extract_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        df = pd.read_csv(StringIO(content))
        return df
    else:
        print(f"Failed to extract data from {url}")
        return None

url1 = "https://www.football-data.co.uk/mmz4281/1920/E0.csv"
url2 = "https://www.football-data.co.uk/mmz4281/1920/E2.csv"
url3 = "https://www.football-data.co.uk/mmz4281/1920/E1.csv"  

data1 = extract_data(url1)
data2 = extract_data(url2)
data3 = extract_data(url3)  

if all(data is not None for data in [data1, data2, data3]):
    if 'time' in data1.columns and 'time' in data2.columns:
        concatenated_data = pd.concat([data1, data2, data3], ignore_index=True)
    else:  
        data3['time'] = None 
        concatenated_data = pd.concat([data1, data2, data3], ignore_index=True)
        concatenated_data.to_csv("C:/Users/HP/OneDrive/Documents/vs code etl projects/goalbet_etl/E0_E1_E2_combined_data.csv", index=False)
    print('E0_E1_E2_combined_data written to csv successfully')
else:
    print("Data extraction failed.")

from goalbet import extract_data, transformed_data, load_to_db

def main():
    url1 = "https://www.football-data.co.uk/mmz4281/1920/E0.csv"
    url2 = "https://www.football-data.co.uk/mmz4281/1920/E2.csv"
    url3 = "https://www.football-data.co.uk/mmz4281/1920/E1.csv"
    
    data1 = extract_data(url1)
    data2 = extract_data(url2)
    data3 = extract_data(url3)
    if all(data is not None for data in [data1, data2, data3]):
        transformed_data()
        load_to_db()
    else:
        print("Data extraction failed.")
main()
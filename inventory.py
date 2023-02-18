import requests, json, csv

class Company:
    ...

class ThirdParty:
    ...

def main():
    # Request data from site API and store response
    url = ""
    response = requests.get(url).json()

    # Set placeholder data to demonstrate program functionality
    response = "data.csv"
    read_data(response)


def read_data(response):
    """Read data into memory and store relevant information in lists"""
    warehouses, capacity_available = [], []
    with open(response) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            warehouses.append(row[0])
            capacity_available.append(row[5])


if __name__ == "__main__":
    main()
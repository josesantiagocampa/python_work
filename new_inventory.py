import requests, json, csv
from datetime import datetime


class Company:
    """A class representing a company seeking storage solutions"""
    def __init__(self,inventory_requirement,temperature_control="N"):
        self.inventory_requirement = inventory_requirement
        self.temperature_control = temperature_control

class ThirdParty:
    "A class representing a third party warehouse"
    ...

def main():
    # Request data from site API and store response
    # url = ""
    # response = requests.get(url).json()

    # Set placeholder data to demonstrate program functionality
    response = "data.csv"

    # Instantiate a company seeking storage for 400 units requiring refrigeration
    company = Company(200,temperature_control="Y")

    # Determine which warehouses have capacity to accomodate company and store in list
    warehouse_options = check_warehouses(company,response)

    # TODO: Check through warehouse options for closest in distance
    # TODO: Update available storage at selected warehouse


def check_warehouses(company, response):
    """Read data into memory and check for warehouses with available storage to accomodate company need"""
    warehouse_options = []
    with open(response) as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (int(row["capacity_available"]) >= company.inventory_requirement) and row["temperature_control"] == company.temperature_control:
                warehouse_options.append(row["warehouse"])
    return warehouse_options


if __name__ == "__main__":
    main()
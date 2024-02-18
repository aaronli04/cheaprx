import csv

# Search CostPlusDrugs for relevant drugs
def search_costplusdrugs(file_path, name):
    matching_rows = []
    name_lower = name.lower()

    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if name_lower in row['Name'].lower() or name_lower in row['Generic'].lower():
                matching_rows.append(row)

    return matching_rows

# Scrape GoodRx
def search_goodrx(name):
    url = 'https://www.goodrx.com/'
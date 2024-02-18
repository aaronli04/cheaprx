import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from helpers import extract_soup_with_selenium, extract_primary_data, extract_secondary_data

def scrape_costplusdrugs():
    # Link to scrape
    url = 'https://costplusdrugs.com/medications/'

    # Data
    data = {
        'Name': [], 'Generic': [], 'Link': [], 'Form': [],
        'Price': [], 'Prescription Needed': [], 'Strength': [], 'Count': []
    }

    soup = extract_soup_with_selenium(url)

    medications = soup.find_all('div', class_='w-auto tablet:w-full tablet:border-2 tablet:border-cap-gray-100 inline-flex')

    for medication in medications:
        name, generic, link, type, price = extract_primary_data(medication)
        print(name)

        prescription_needed = False
        strength = ''
        count = ''

        if link:
            print(link)
            prescription_needed, strength, count = extract_secondary_data(link)


        data['Name'].append(name)
        data['Generic'].append(generic)
        data['Link'].append(link)
        data['Form'].append(type)
        data['Price'].append(price)    
        data['Prescription Needed'].append(prescription_needed)
        data['Strength'].append(strength)
        data['Count'].append(count)

    df = pd.DataFrame(data)
    df.to_csv('prescription_data.csv', index=False)


if __name__ == "__main__":
    scrape_costplusdrugs()
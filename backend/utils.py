import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
    
def extract_soup_with_selenium(link):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    time.sleep(0.1)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    return soup

# Search CostPlusDrugs for relevant drugs
def search_costplusdrugs(file_path, name):
    matching_rows = []
    medications = []
    name_lower = name.lower()

    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if name_lower in row['Name'].lower() or name_lower in row['Generic'].lower():
                matching_rows.append(row)

    for row in matching_rows:
        processed_medication = {
            'name': row['Name'],
            'generic': row['Generic'],
            'link': row['Link'],
            'price': row['Price'],
            'prescription_needed': bool(row['Prescription Needed'].lower() == 'true'),
            'strength': row['Strength'],
            'count': row['Count']
        }
        medications.append(processed_medication)

    return medications

# Scrape Blink Health
def search_blink_health(name):
    link = 'https://www.blinkhealth.com/' + name
    soup = extract_soup_with_selenium(link)

    price_elem = soup.find('div', class_="text_Text_title4-blinkui__5v9KW text_interstate-regular__6jvdM text_interstate-regular__6jvdM text_Text_align-right__YLNqY")
    size_elem = soup.find('div', class_="input_input__fT6hC px-sm-16 py-sm-12")
    prescription_elem = soup.find_all('span', class_='text_Text_headline-blinkui__XtU_c text_interstate-regular__6jvdM text_interstate-regular__6jvdM')

    if (price_elem and size_elem and prescription_elem):
        price = ''
        prescription_needed = False
        strength = ''
        count = ''

        price = price_elem.text.strip().replace('$', '').replace(',', '')

        parts = [part.strip() for part in size_elem.text.split(',')]
        for part in parts:
            if "mg" in part:
                strength = part.lower()
            elif any(char.isdigit() for char in part):
                count = part.lower()

        for elem in prescription_elem:
            prescription_status = elem.text.strip().lower()
            if prescription_status == 'prescription required':
                prescription_needed = True

        medication = {
            'name': name,
            'generic': '',
            'link': link,
            'price': price,
            'prescription_needed': prescription_needed,
            'strength': strength,
            'count': count
        }

        return medication
    
    return None

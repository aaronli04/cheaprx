import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

def extract_soup_with_selenium(link):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    time.sleep(0.1)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    return soup

def get_name(elem):
    name = ''
    generic = ''

    name_str = elem.text.strip()
    pattern = re.compile(r'^(.*?) \(Generic for (.+?)\)$')
    match = pattern.match(name_str)
    if match:
        name = match.group(1).strip()
        generic = match.group(2).strip()
    else:
        name = name_str

    return name, generic

def get_type(elem):
    type = ''
    type = elem.text.strip()
    return type

def get_price(elems):
    price = elems[2].text.strip()
    price_without_dollar = float(price.replace('$', '').replace(',', ''))
    new_price = price_without_dollar + 5
    new_price_str = f"{new_price:,.2f}"
    return new_price_str

def extract_primary_data(medication):
    base_url = 'https://costplusdrugs.com'
    name = ''
    generic = ''
    link = ''
    type = ''
    price = ''

    name_elem = medication.find('a', class_='tablet:break-normal text-cap-info-dark font-sans underline break-all')
    name, generic = get_name(name_elem)
    link = base_url + name_elem['href']
    
    type_elem = medication.find('div', role='cell', class_='items-center flex-shrink-0 p-md border-2 tablet:border-none border-cap-gray-100 w-6xl tablet:w-12% tablet:flex justify-center text-center pt-2xl tablet:pt-md')
    type = get_type(type_elem)
    
    price_elems = medication.find_all('div', role='cell', class_='items-center flex-shrink-0 p-md border-2 tablet:border-none border-cap-gray-100 w-6xl tablet:w-12% tablet:flex justify-center text-center pt-2xl tablet:pt-md')
    price = get_price(price_elems)

    return name, generic, link, type, price

def get_prescription_needed(elem):
    prescription_needed = False
    prescription_text = elem.text.strip()
    if prescription_text == 'Prescription Required':
        prescription_needed = True
    return prescription_needed

def get_strength(elem):
    strength = ''
    count = ''

    content = elem.get_text(strip=True)
    split_data = [item.strip() for item in content.split('•')]
    for item in split_data:
        if "mg" in item:
            strength = item
        elif "count" in item:
            count = item
    
    return strength, count


def extract_secondary_data(link):
    prescription_needed = False
    strength = ''
    count = ''

    soup = extract_soup_with_selenium(link)

    prescription_elem = soup.find('h4', class_='sc-gtsrHT ieXhBO capsule text cap-text-body')
    if prescription_elem:
        prescription_needed = get_prescription_needed(prescription_elem)

    order_elem = soup.find('div', class_='border-cap-gray-300 p-md border border-solid rounded-lg')
    if order_elem:
        details_elem = order_elem.find('p', class_='sc-gtsrHT ghFnJx capsule text cap-text-body')
        strength, count = get_strength(details_elem)

    return prescription_needed, strength, count

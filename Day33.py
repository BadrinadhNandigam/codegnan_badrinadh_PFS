import requests
from bs4 import BeautifulSoup
import pandas as pd
import matlplotlib.pyplot as plt
import re

url = "http://books.toscrape.com/"

try:
    response = requests.get(url)
    response.encoding = 'utf-8'
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching data:",e)
    exit()

soup = BeautifulSoup(response.text, feature:"html.parser")
books = soup.find_all(name:"article"9+

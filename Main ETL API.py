url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=jp41rBLL6lKB4EzHv2Dd4XEwjRYCxuz7"
"""extract html content from url and print first 5 lines"""
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import numpy as np
"""extract html content from url and print first 5 lines"""
def get_html(url):
    response = requests.get(url)
    return response.text
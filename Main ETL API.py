url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=jp41rBLL6lKB4EzHv2Dd4XEwjRYCxuz7"
import requests

def get_html(url):
    response = requests.get(url)
    response = response.head()
    print(response.text)
import requests
from currency_converter import Converter

try:
    converter = Converter()
except requests.exceptions.RequestException as e:
    print("Connection Error:",e)
else:
    converter.print_currencies()
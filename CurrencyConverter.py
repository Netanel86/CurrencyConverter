import requests
import xmltodict
import datetime

today = datetime.datetime.now();

endpoint = "http://www.boi.org.il/currency.xml?rdate={year}{month}{day}"

url = endpoint.format(
    year = today.strftime("%Y"), 
    month = today.strftime("%m"), 
    day = today.strftime("%d"))

try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print("Connection Error:",e)
else:
    data = xmltodict.parse(response.content)

    if 'CURRENCY' not in data['CURRENCIES']:
        print(data['CURRENCIES']['ERROR2'])
    else:
        mydict = {}

        for currency in data['CURRENCIES']['CURRENCY']:
            mydict[currency['CURRENCYCODE']] = {
                'country' : currency['COUNTRY'], 
                'name' : currency['NAME'], 
                'rate' : currency['RATE']}


        print(mydict)
        

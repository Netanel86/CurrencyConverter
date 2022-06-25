import requests
import datetime
import xmltodict

class Currency:
    def __init__(self, code, country, name, rate):
        self.code = code
        self.country = country
        self.name = name
        self.rate = rate

class Converter: 
    def __init__(self):
        self.endpoint = "http://www.boi.org.il/currency.xml?rdate={year}{month}{day}"
        self.currency_dict = {}

        response = requests.get(self.__formatUrl())

        self.__init_currencies(response)
    
    def __formatUrl(self):
        today = datetime.datetime.now()
        
        return self.endpoint.format(
            year = today.strftime("%Y"), 
            month = today.strftime("%m"), 
            day = self.__get_last_business_day(today))

    def __get_last_business_day(self, today):
        
        # Lambda function to check the weekday and retrun the days past since last business day
        get_delta = lambda date : 1 if int(date.strftime('%w')) == 5 else 2 if int(date.strftime('%w')) == 6 else 0
        
        # fix_day = lambda date : int(date.strftime("%d")) - get_delta(date) if get_delta(date) != 0 else 0
        # return fix_day(today)
        return int(today.strftime("%d")) - get_delta(today)

    def __init_currencies(self, xml_response):
        data = xmltodict.parse(xml_response.content)

        for currency in data['CURRENCIES']['CURRENCY']:
            newCurrency = Currency(currency['CURRENCYCODE'],currency['COUNTRY'], currency['NAME'], currency['RATE'])

            self.currency_dict[newCurrency.code] = newCurrency

    def print_currencies(self):
        print(self.currency_dict)

    


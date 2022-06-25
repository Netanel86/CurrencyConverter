import requests
import datetime
import xmltodict

class Currency:
    def __init__(self, code, country, name, rate):
        self.code = code
        self.country = country
        self.name = name
        self.rate = float(rate)
    
    def __str__(self):
        return "[{0}]: Name: {1}, Code: {2}, Rate: {3}".format(self.country, self.name, self.code, self.rate)

class Converter: 
    def __init__(self):
        self.__endpoint = "http://www.boi.org.il/currency.xml?rdate={year}{month}{day}"
        self.__currency_dict = {}

        response = requests.get(self.__formatUrl())

        self.__init_currencies(response)
    
    def __formatUrl(self):
        today = datetime.datetime.now()
        
        return self.__endpoint.format(
            year = today.strftime("%Y"), 
            month = today.strftime("%m"), 
            day = self.__get_last_business_day(today))

    def __get_last_business_day(self, today):
       
        # Lambda function to check the weekday and retrun the days past since last business day
        get_delta = lambda date : 1 if int(date.strftime('%w')) == 5 else 2 if int(date.strftime('%w')) == 6 else 0

        return int(today.strftime("%d")) - get_delta(today)

    def __init_currencies(self, xml_response):
        data = xmltodict.parse(xml_response.content)

        for currency in data['CURRENCIES']['CURRENCY']:
            new_currency = Currency(currency['CURRENCYCODE'], currency['COUNTRY'], currency['NAME'], currency['RATE'])

            self.__currency_dict[new_currency.code] = new_currency

        self.__currency_dict['ILS'] = Currency('ILS', 'Israel', 'New Shekels', 1)

    def __check_currency(self, currency, code):
        if currency == 0:
            raise ConversionError("Conversion Error: '{0}' is not a knowen currency code".format(code))    
    
    def convert(self, sum, from_code, to_code):
        src_currency = self.__currency_dict.get(from_code, 0)
        target_currency = self.__currency_dict.get(to_code, 0)
        
        self.__check_currency(src_currency, from_code)
        self.__check_currency(target_currency, to_code)

        if from_code == to_code:
            converted = sum
        else: 
            converted = (sum * src_currency.rate) / target_currency.rate
        
        return {'converted_sum': converted, 
            'src_currency': src_currency, 
            'target_currency': target_currency}

    def print_currencies(self):
        for currency in self.__currency_dict.values():
            print(currency)
    
class ConversionError(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)

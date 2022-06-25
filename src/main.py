import requests
from currency_converter import ConversionError, Converter

try:
    converter = Converter()
    print("My console currency conversion app:")
    from_str = input("Enter Source Currency:")
    to_str = input("Enter Target Currency:")
    sum = input("Enter Amount:")
    # from_str = 'ILS'
    # to_str = 'ILS'
    # sum = 120
    converted = converter.convert(sum, from_str, to_str)

    print("Converted {0} {1} {2} to {3} {4} {5}".format(sum, 
        converted['src_currency'].country, 
        converted['src_currency'].name, 
        converted['converted_sum'],
        converted['target_currency'].country,
        converted['target_currency'].name))

#Catch exception in case of a connection error    
except requests.exceptions.RequestException as e:
    print("Connection Error:",e)

#Catch exception in case of a conversion error
except ConversionError as e:
    print(e)
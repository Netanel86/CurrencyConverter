import requests
from currency_converter import ConversionError, Converter

try:
    converter = Converter()
    print("My console currency conversion app:")
    
    from_str = input("Enter Source Currency: ").upper()
    to_str = input("Enter Target Currency: ").upper()
    sum = float(input("Enter Amount: "))

    converted = converter.convert(sum, from_str, to_str)

    print("Converted {0:.2f} {1} {2} to {3:.2f} {4} {5}".format(sum, 
        converted['src_currency'].country, 
        converted['src_currency'].name,
        converted['converted_sum'],
        converted['target_currency'].country,
        converted['target_currency'].name))

#Catch exception in case of a input error
except ValueError as e:
    print(e)

#Catch exception in case of a connection error    
except requests.exceptions.RequestException as e:
    print("Connection Error:",e)

#Catch exception in case of a conversion error
except ConversionError as e:
    print(e)
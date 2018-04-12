import requests
from main.models import Currency


def currency_converter():
    currencies = ['KWD', 'OMR', 'BHD', 'JOD', 'SAR', 'LBP', 'QAR']
    for c in currencies:
        r = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=' + 'AED_' + c + '&compact=ultra')
        json = r.json()
        rate = json['AED_' + c]
        Currency.objects.filter(to_currency=c).update(rate=rate)

from django import template
import requests
from main.models import Currency

register = template.Library()


@register.filter(name='spacetodash')
def spacetodash(value):
    return value.replace(' ', '-')


@register.filter(name='dashtospace')
def dashtospace(value):
    return value.replace('-', ' ')


@register.filter(name='multiply')
def multiply(value, arg):
    return float(value) * float(arg)


@register.filter(name='formatprice')
def formatprice(value):
    return float("{0:.2f}".format(value))


@register.simple_tag
def currency_converter(value, code):
    if code == "KWD":
        currency = Currency.objects.get(to_currency=code)
        rate = currency.rate
        converted = float(rate) * float(value)
        return float("{0:.2f}".format(converted))
    elif code == 'OMR':
        currency = Currency.objects.get(to_currency=code)
        rate = currency.rate
        converted = float(rate * value)
        return float("{0:.2f}".format(converted))
    elif code == 'BHD':
        currency = Currency.objects.get(to_currency=code)
        rate = currency.rate
        converted = float(rate * value)
        return float("{0:.2f}".format(converted))
    elif code == 'AED':
        tax = float(value) * (5 / 100)
        final = float(value + tax)
        return float("{0:.2f}".format(final))
    elif code == 'JOD':
        currency = Currency.objects.get(to_currency=code)
        rate = currency.rate
        converted = float(rate * value)
        price_with_tax = float(converted + (converted * (16 / 100)))
        return float("{0:.2f}".format(price_with_tax))
    elif code == 'SAR':
        currency = Currency.objects.get(to_currency=code)
        rate = currency.rate
        converted = float(rate * value)
        price_with_tax = float(converted + (converted * (5 / 100)))
        return float("{0:.2f}".format(price_with_tax))
    elif code == 'QAR':
        currency = Currency.objects.get(to_currency=code)
        rate = currency.rate
        final = float(rate * value)
        return float("{0:.2f}".format(final))
    elif code == 'LBP':
        currency = Currency.objects.get(to_currency=code)
        rate = currency.rate
        converted = float(rate * value)
        price_with_tax = float(converted + (converted * (11 / 100)))
        return float("{0:.2f}".format(price_with_tax))

import requests

def valuta(from_currency,to_currency,amount):
    """

    :param from_currecny:
    :param to_currency:
    :param amount:
    :return:
    """
    to_amount = amount * 2

    return "{amount} {from_currency} is {to_amount} {to_currency}"

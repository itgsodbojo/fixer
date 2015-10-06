#!/usr/bin/env python

import requests
import sys

def valuta(from_currency,to_currency,amount):
    """

    :param from_currecny:
    :param to_currency:
    :param amount:
    :return:
    """
    to_amount = amount * 2

    return "{amount} {from_currency} is {to_amount} {to_currency}"


# for this to work change the flag for your file to executable
# in a terminal do
# chmod +x fixer.py

# run the program with ./fixer [args]
if __name__ == "__main__":


      from_currency=  sys.argv[2]
      to_currency=  sys.argv[4]
      amount=  sys.argv[1]

      print valuta(from_currency,to_currency ,amount )

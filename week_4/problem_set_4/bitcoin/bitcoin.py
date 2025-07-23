# Week 4: Problem 5
# check the current price of bitcoin using coincap_api_key
# take cmd-line arg for how many bitcoin they want to buy. if input not a num, sys.exit,
# give output with float type upto 4 decimals with (,) sep
import requests
import json
import os
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        coin = float(sys.argv[1])
        if coin <= 0:
            sys.exit("Number of Bitcoins must be positive")
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        price = float(get_bitcoin_price())
    except (KeyError, ValueError, requests.RequestException):
        sys.exit("Error fetching Bitcoin Price")

    total_price = price * coin
    print(f"${total_price:,.4f}")


def get_bitcoin_price():
    api_key = os.getenv("COINCAP_API_KEY")

    url = "https://rest.coincap.io/v3/assets/bitcoin"
    headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}

    # get the data in json response
    response = requests.get(url, headers=headers)

    # check for correct response of api
    response.raise_for_status()

    bitcoin = response.json()
    bitcoin_price = bitcoin["data"]["priceUsd"]
    return bitcoin_price


main()

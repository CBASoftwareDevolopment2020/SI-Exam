import webscraper

import requests
import secrets


class CurrencyConverter:
    @staticmethod
    def convert(in_cur: str, out_cur: str, amt: int) -> int:
        return int(round(webscraper.get_exchange_rate(in_cur, out_cur) * amt))

    @staticmethod
    def convert_old(in_cur: str, out_cur: str, amt: int) -> int:
        return int(round(CurrencyConverter.exchange_rate(in_cur, out_cur) * amt))

    @staticmethod
    def exchange_rate(in_cur: str, out_cur: str) -> float:
        url = f'https://currency-converter13.p.rapidapi.com/convert'
        querystring = {"from": in_cur, "to": out_cur, "amount": "1"}
        headers = {
            'x-rapidapi-key': secrets.rapidapi_key,
            'x-rapidapi-host': 'currency-converter13.p.rapidapi.com'
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.json()['amount'])
        return response.json()['amount']


if __name__ == '__main__':
    print(CurrencyConverter.convert('USD', 'EUR', 100))

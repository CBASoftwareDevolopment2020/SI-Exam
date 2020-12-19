from bs4 import BeautifulSoup
import requests


def get_exchange_rate(in_cur: str, out_cur: str) -> float:
    url = f'https://www.google.com/search?q=exchange+rate+{in_cur}+to+{out_cur}'
    html = requests.request("GET", url).text
    soup = BeautifulSoup(html, 'html.parser').find('div', id='main').text
    res = soup.split(':')[1].split('-')[0].strip()
    _, ind, _, ud, _, val, *_ = res.split(' ')
    return float(val)


if __name__ == '__main__':
    amt = 100
    input_currency = 'USD'
    output_currency = 'DKK'
    url = f'https://www.google.com/search?q=exchange+rate+{input_currency}+to+{output_currency}'
    html = requests.request("GET", url).text
    soup = BeautifulSoup(html, 'html.parser').find('div', id='main').text
    test = soup.split(':')[1].split('-')[0].strip()
    _, ind, _, ud, _, val, *_ = test.split(' ')
    print(int(round(float(val) * amt)))

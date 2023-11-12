import os
import requests
from urllib.parse import ParseResult, urlparse

from dotenv import load_dotenv


def is_bitlink_exist(long_bitlink: str) -> bool:
    bitlink: ParseResult = urlparse(long_bitlink)
    url = f'{API_URL}bitlinks/{bitlink.netloc}{bitlink.path}'
    response = requests.get(url=url, headers=HEADERS)
    return response.status_code == 200


def get_clicks_count(long_bitlink: str) -> str:
    bitlink: ParseResult = urlparse(long_bitlink)
    url = f'{API_URL}bitlinks/{bitlink.netloc}{bitlink.path}/clicks/summary'
    response = requests.get(url=url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        return f'По вашей ссылке прошли: {data.get("total_clicks")} раз(а)'
    else:
        return f'Ошибка при выполнении GET-запроса: {response.status_code}. Проверьте введённые данные.'


def make_short_link(long_url: str) -> str:
    json = {'long_url': long_url}
    response = requests.post(url=f'{API_URL}shorten', json=json, headers=HEADERS)
    if response.status_code in [200, 201]:
        data = response.json()
        return f'Битлинк: {data.get("link")}'
    else:
        return f'Ошибка при выполнении POST-запроса: {response.status_code}. Проверьте введённые данные.'


def main():
    long_url = input('Введите ссылку: ')
    is_bitlink = is_bitlink_exist(long_url)
    if not is_bitlink:
        print(make_short_link(long_url))
    else:
        print(get_clicks_count(long_url))


if __name__ == '__main__':
    load_dotenv('config.env')
    ACCESS_TOKEN = os.environ.get('BITLY_ACCESS_TOKEN')
    HEADERS = {"Authorization": "Bearer " + ACCESS_TOKEN}
    API_URL = 'https://api-ssl.bitly.com/v4/'
    main()

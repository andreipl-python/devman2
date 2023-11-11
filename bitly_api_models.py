from urllib.parse import ParseResult, urlparse

from aiohttp import ContentTypeError

from config_reader import config
from typing import Optional

import aiohttp


class BitlyAPI:
    def __init__(self):
        self.access_token = config.bitly_access_token.get_secret_value()
        self.headers = {
            "Authorization": "Bearer " + self.access_token
        }
        self.url = 'https://api-ssl.bitly.com/v4/'

    async def __get(self, method: str, params: Optional[dict] = None) -> dict:
        method_url = f'{self.url}{method}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url=method_url, headers=self.headers, params=params) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return {'error_message': f'Error {response.status}. Проверьте введённые данные.'}

    async def __post(self, method: str, data: Optional[dict] = None) -> dict:
        method_url = f'{self.url}{method}'
        async with aiohttp.ClientSession() as session:
            async with session.post(url=method_url, headers=self.headers, json=data) as response:
                if response.status in [200, 201]:
                    return await response.json()
                else:
                    return {'error_message': f'Error {response.status}. Проверьте введённые данные.'}

    async def get_user(self) -> dict:
        return await self.__get(method='user')

    async def get_clicks_count(self, long_bitlink: str) -> str:
        bitlink: ParseResult = urlparse(long_bitlink)
        method = f'bitlinks/{bitlink.netloc}{bitlink.path}/clicks/summary'
        result = await self.__get(method=method)
        return f'По вашей ссылке прошли: {result.get("total_clicks")} раз(а)' if result.get('total_clicks') \
            else result.get('error_message')

    async def make_short_link(self, long_url: str) -> str:
        data = {'long_url': long_url}
        result = await self.__post(method='shorten', data=data)
        return f'Битлинк: {result.get("link")}' if result.get('link') else result.get('error_message')

    async def is_bitlink_exist(self, long_bitlink: str) -> bool:
        bitlink: ParseResult = urlparse(long_bitlink)
        method = f'bitlinks/{bitlink.netloc}{bitlink.path}'
        result = await self.__get(method=method)
        return not bool(result.get('error_message'))

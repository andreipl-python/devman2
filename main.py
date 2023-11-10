import asyncio

from bitly_api_models import BitlyAPI


async def main():
    while True:
        long_url = input('Введите ссылку: ')
        is_bitlink = await BitlyAPI().is_bitlink_exist(long_url)

        if not is_bitlink:
            print(await BitlyAPI().make_short_link(long_url))
        else:
            print(await BitlyAPI().get_clicks_count(long_url))

if __name__ == '__main__':
    asyncio.run(main())

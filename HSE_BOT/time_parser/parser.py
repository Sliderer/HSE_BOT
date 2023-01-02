import requests
from bs4 import BeautifulSoup


class TimeParser:
    website_url = 'https://time100.ru/index.php'

    async def parse_time(self):
        try:
            result = requests.get(self.website_url)
        except:
            print('Error with parsing time')
        content = BeautifulSoup(result.content, 'lxml')
        return content.find_all('span')
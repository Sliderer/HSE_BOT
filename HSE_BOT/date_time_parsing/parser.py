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
        content = content.find('h3', class_='display-time monospace')
        content = content.find('span', class_='time').text
        return content

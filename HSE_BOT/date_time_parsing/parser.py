import requests
from bs4 import BeautifulSoup


class TimeParser:
    website_url = 'https://time100.ru/index.php'

    def parse_date_time(self):
        try:
            result = requests.get(self.website_url)
        except:
            print('Error with parsing time')

        content = BeautifulSoup(result.content, 'lxml')

        result = (self.parse_time(content), self.parse_date(content))
        return result

    def parse_time(self, content: BeautifulSoup):
        content = content.find('h3', class_='display-time monospace')
        content = content.find('span', class_='time').text
        return content

    def parse_date(self, content: BeautifulSoup):
        content = content.find('h3', class_='display-date monospace')
        content = content.find('span', class_='time').text
        content = content.split(':')[1]
        return content

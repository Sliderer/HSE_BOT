import requests
from bs4 import BeautifulSoup


class DateTime:
    def __init__(self, time: str, date: str):
        self.__time = time
        self.__date = date

    def get_time(self):
        return self.__time

    def get_date(self):
        return self.__date

    time = property(get_time)
    date = property(get_date)


class TimeParser:
    website_url = 'https://time100.ru/index.php'

    def parse_date_time(self) -> DateTime:
        try:
            result = requests.get(self.website_url)
        except:
            print('Error with parsing time')

        content = BeautifulSoup(result.content, 'lxml')
        time = self.parse_time(content)
        date = self.parse_date(content)
        result = DateTime(time=time, date=date)
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

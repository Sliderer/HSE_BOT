from selenium import webdriver
from selenium.webdriver.common.by import By
from logger import Logger
from time import sleep
from bs4 import BeautifulSoup


class Parser:
    web_url = "https://ruz.hse.ru/ruz/main"
    date_time_parser = None
    browser = None

    def __init__(self, time_parser):
        self.date_time_parser = time_parser
        # start = time()
        # Logger.info(f"BROWSER START TIME: {time() - start}")

    #
    # def __del__(self):
    #     self.browser.quit()

    month_to_number = {
        'январь': "01",
        'февраль': "02",
        'март': "03",
        'апрель': "04",
        'май': "05",
        'июнь': "06",
        'июль': "07",
        'август': "08",
        'сентябрь': "09",
        'октябрь': "10",
        'ноябрь': "11",
        'декабрь': "12"
    }

    def __get_ruz_page(self, full_name: str):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=options)

        self.browser.get(self.web_url)

        Logger.info(f"RUZ FOR: {full_name}")

        while len(self.browser.find_elements(By.XPATH,
                                             "//button[@class='btn btn-outline-secondary ng-star-inserted']")) == 0:
            sleep(0.1)

        Logger.info("HERE")
        button = self.browser.find_element(By.XPATH, "//button[@class='btn btn-outline-secondary ng-star-inserted']")
        button.click()

        input = self.browser.find_element(By.XPATH,
                                          "//input[@class='ng-tns-c41-3 form-control ui-inputtext ui-widget ui-state-default ui-corner-all ui-autocomplete-input ng-star-inserted']")

        input.clear()
        input.send_keys(full_name)

        Logger.info("HERE2")
        delta = 0
        while len(self.browser.find_elements(By.XPATH, "//li[@role='option']")) == 0:
            sleep(0.1)
            delta += 0.1
            if delta >= 3:
                return []
        Logger.info("HERE3")

        get = self.browser.find_element(By.XPATH, "//li[@role='option']")
        Logger.info(f"FIND RUZ FOR {get.text}")
        get.click()

        delta = 0

        while len(self.browser.find_elements(By.XPATH, "//div[@class='media item']")) == 0:
            sleep(0.1)
            delta += 0.1
            if delta >= 3:
                return 0

        return self.browser.find_elements(By.XPATH, "//div[@class='media item']")

    def get_day_schedule(self, full_name: str):

        cnt = self.__get_ruz_page(full_name)
        result = []

        cur_day = self.date_time_parser.current_date_time.get_date()[-2:]

        for ind in cnt:
            page = BeautifulSoup(ind.get_attribute("outerHTML"), "html.parser")

            date = page.find('div', {'class': 'd-lg-none date clearfix'}).findAll('span')[0].text[1:]
            if date[0:2] < cur_day:
                continue
            elif date[0:2] > cur_day:
                break

            name = page.find('span', {'class': 'ng-star-inserted'}).text
            class_type = page.find('div', {'class': 'text-muted kind ng-star-inserted'}).text
            address = page.findAll('td')[0].text
            professor = page.findAll('td')[2].text
            time = page.find('div', {'class': 'time'}).text

            lesson = {
                'name': name,
                'type': class_type,
                'address': address,
                'professor': professor,
                'time': time,
                'date': date
            }
            result.append(lesson)

        self.browser.quit()
        return result

    def get_week_schedule(self, full_name: str):

        cnt = self.__get_ruz_page(full_name)
        result = []

        for ind in cnt:
            page = BeautifulSoup(ind.get_attribute("outerHTML"), "html.parser")

            date = page.find('div', {'class': 'd-lg-none date clearfix'}).findAll('span')[0].text[1:]
            name = page.find('span', {'class': 'ng-star-inserted'}).text
            class_type = page.find('div', {'class': 'text-muted kind ng-star-inserted'}).text
            address = page.findAll('td')[0].text
            professor = page.findAll('td')[2].text
            time = page.find('div', {'class': 'time'}).text

            lesson = {
                'name': name,
                'type': class_type,
                'address': address,
                'professor': professor,
                'time': time,
                'date': date
            }
            result.append(lesson)

        self.browser.quit()
        return result

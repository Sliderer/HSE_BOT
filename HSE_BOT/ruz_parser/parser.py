from selenium import webdriver
import datetime
from selenium.webdriver.common.by import By
from logger import Logger
from time import sleep


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

        # input = self.browser.find_element(By.XPATH, "//input[@placeholder='Студент']")
        input = self.browser.find_element(By.XPATH, "//input[@class='ng-tns-c41-3 form-control ui-inputtext ui-widget ui-state-default ui-corner-all ui-autocomplete-input ng-star-inserted']")

        input.clear()
        input.send_keys(full_name)

        Logger.info("HERE2")
        delta = 0
        while len(self.browser.find_elements(By.XPATH, "//li[@role='option']")) == 0:
            sleep(0.1)
            delta += 0.1
            if delta >= 3:
                return 0
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

        return len(self.browser.find_elements(By.XPATH, "//div[@class='media item']"))

    def get_day_schedule(self, full_name: str):

        cnt = self.__get_ruz_page(full_name)
        result = []

        days = self.browser.find_elements(By.XPATH, "//div[@class='day']")
        months = self.browser.find_elements(By.XPATH, "//div[@class='month']")
        cur_date_ind = 0
        prev_time = "00:00-00:00"

        cur_day = self.date_time_parser.current_date_time.get_date()[-2:]

        for ind in range(cnt):
            name = self.browser.find_elements(By.XPATH, "//span[@class='ng-star-inserted']")[ind].text
            class_type = self.browser.find_elements(By.XPATH, "//div[@class='text-muted kind ng-star-inserted']")[ind].text
            address = self.browser.find_elements(By.XPATH, "//td")[3 * ind].text
            professor = self.browser.find_elements(By.XPATH, "//td")[3 * ind + 2].text
            time = str(self.browser.find_elements(By.XPATH, "//div[@class='time']")[ind].get_attribute("innerHTML"))
            time = time[1:6] + time[12] + time[19:-1]

            if time <= prev_time:
                cur_date_ind += 1
            prev_time = time

            day = days[cur_date_ind].get_attribute("innerHTML")
            if len(day) == 1:
                day = "0" + day

            if day < cur_day:
                continue
            if day > cur_day:
                break
            month = self.month_to_number[months[cur_date_ind].get_attribute("innerHTML")]
            year = datetime.datetime.now().year
            date = f'{day}.{month}.{year}'

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

        days = self.browser.find_elements(By.XPATH, "//div[@class='day']")
        months = self.browser.find_elements(By.XPATH, "//div[@class='month']")
        cur_date_ind = 0
        prev_time = "00:00-00:00"

        for ind in range(cnt):
            name = self.browser.find_elements(By.XPATH, "//span[@class='ng-star-inserted']")[ind].text
            type = self.browser.find_elements(By.XPATH, "//div[@class='text-muted kind ng-star-inserted']")[ind].text
            address = self.browser.find_elements(By.XPATH, "//td")[3 * ind].text
            professor = self.browser.find_elements(By.XPATH, "//td")[3 * ind + 2].text
            time = str(self.browser.find_elements(By.XPATH, "//div[@class='time']")[ind].get_attribute("innerHTML"))
            time = time[1:6] + time[12] + time[19:-1]

            if time <= prev_time:
                cur_date_ind += 1
            prev_time = time

            day = days[cur_date_ind].get_attribute("innerHTML")
            if len(day) == 1:
                day = "0" + day
            month = self.month_to_number[months[cur_date_ind].get_attribute("innerHTML")]
            year = datetime.datetime.now().year
            date = f'{day}.{month}.{year}'

            lesson = {
                'name': name,
                'type': type,
                'address': address,
                'professor': professor,
                'time': time,
                'date': date
            }
            result.append(lesson)

        self.browser.quit()
        return result

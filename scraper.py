import csv
import os
from urllib.parse import urljoin

from bs4 import BeautifulSoup, ResultSet, Tag
from selenium import webdriver
from selenium.common import (
    NoSuchElementException,
    ElementClickInterceptedException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from config import Vacancy, DJINNI_URL, COLUMNS, DJINNI_URL_JUNIOR, DJINNI_URL_MIDDLE, DJINNI_URL_SENIOR, \
    DJINNI_URL_TEAM_LEAD


class DjinniScraper:
    def __init__(self, url: str):
        self.driver = webdriver.Chrome()
        self.url = url

    def close(self):
        if self.driver:
            self.driver.quit()

    def parse_single_vacancy(self, description: str):
        return Vacancy(description)

    def parse_page(self, descriptions: list[WebElement]) -> list[Vacancy]:
        vacancies = []
        for description in descriptions:
            vacancies.append(
                self.parse_single_vacancy(
                    description.get_attribute("data-original-text").lower()
                )
            )
        return vacancies

    def find_elements_safe(self, value: str) -> list[WebElement] | list[None]:
        try:
            return self.driver.find_elements(By.CSS_SELECTOR, value)
        except NoSuchElementException:
            return [None]

    def find_element_safe(self, value: str) -> WebElement | None:
        try:
            return self.driver.find_element(By.CSS_SELECTOR, value)
        except NoSuchElementException:
            return None

    def parse(self):
        self.driver.get(self.url)
        vacancies = []
        i = 1
        while True:
            print(f"Parsing page number {i}...")
            page = self.driver.find_elements(
                By.CSS_SELECTOR, ".job-list-item__description > span"
            )
            vacancies += self.parse_page(page)
            if not self.find_element_safe("ul.pagination"):
                print("Done!")
                break
            next_page = self.find_elements_safe("a.page-link")[-1]
            if next_page:
                try:
                    next_page.click()
                except ElementClickInterceptedException:
                    print("Done!")
                    break
                i += 1

        return vacancies

    def write_to_csv(self, filename: str) -> None:
        vacancies = self.parse()
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(COLUMNS)
            writer.writerows(
                (vacancy.__getattribute__(attr) for attr in COLUMNS)
                for vacancy in vacancies
            )


if __name__ == "__main__":
    parser = DjinniScraper(DJINNI_URL)
    try:
        print("Parsing without filters!")
        parser.write_to_csv("general_vacancies.csv")

        print("Parsing vacancies for Juniors!")
        parser.url = DJINNI_URL_JUNIOR
        parser.write_to_csv("junior_vacancies.csv")

        print("Parsing vacancies for Middlers!")
        parser.url = DJINNI_URL_MIDDLE
        parser.write_to_csv("middle_vacancies.csv")

        print("Parsing vacancies for Seniors!")
        parser.url = DJINNI_URL_SENIOR
        parser.write_to_csv("senior_vacancies.csv")

        print("Parsing vacancies for Team Leads!")
        parser.url = DJINNI_URL_TEAM_LEAD
        parser.write_to_csv("team_lead_vacancies.csv")
    except Exception as e:
        print(e)
    finally:
        parser.close()

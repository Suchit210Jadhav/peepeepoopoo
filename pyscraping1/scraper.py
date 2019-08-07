from os import system
import requests 
from bs4 import BeautifulSoup

def scrap_weather():

    a = input("Enter the city name for weather info: ").strip()
    a = a.replace(" ", "+")

    url = 'https://www.google.com/search?ei=CrlKXdDQJ_Dbz7sPrr248Ao&q=how+is+weather+of+'+ a

    headers = {
        "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }

    try:
        web_page = requests.get(url, headers = headers)

        page_soup = BeautifulSoup(web_page.content, 'html.parser')

        location = page_soup.find(id = 'wob_loc').get_text().strip()
        weather = page_soup.find(id = 'wob_dc').get_text().strip()
        temperature = page_soup.find(id = 'wob_tm').get_text().strip()

        system('cls')
        print("Todays weather:")
        print("Location: ",location)
        print("Weather: ",weather)
        print("Temperature: ",temperature,"C")

    except:
        print("Enter the correct city name!")
        scrap_weather()

scrap_weather()
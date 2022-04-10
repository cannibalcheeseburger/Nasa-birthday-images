from bs4 import BeautifulSoup
from requests import get
import wget
from datetime import date

#inputs 
dates = input('Date(MMDD): ')
years = int(input('Years: '))

#const
today = date.today()
year = today.year if today.month>int(dates[:2]) else today.year-1

def download(year,dates):
    url = "https://apod.nasa.gov/apod/"
    datess = year[2:4]+dates
    datestr = "ap"+datess+".html"
    page_soup = BeautifulSoup(get(url+datestr).text,'html.parser')
    wget.download(url+page_soup.img['src'],out="./downloads/"+datess+".jpg")

for i in range(years):
    try:
        print(year)
        download(str(year),dates)
    except:
        pass
    year = year-1
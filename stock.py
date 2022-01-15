from bs4 import BeautifulSoup
import requests
import webbrowser 
import os
import shutil
import time

def get_data(YEAR, fileName):

    START_YEAR = str(YEAR)
    START_MONTH = '1'
    START_DAY = '1'
    START = START_MONTH + '/' + START_DAY + '/' + START_YEAR
    END_YEAR = str(YEAR)
    END_MONTH = '12'
    END_DAY = '31'
    END = END_MONTH + '/' + END_DAY + '/' + END_YEAR

    # data_url = f'https://www.marketwatch.com/investing/index/djia/download-data?startDate={START}&endDate={END}'
    data_url = f'https://www.marketwatch.com/investing/index/nik/download-data?startDate={START}&endDate={END}&countryCode=jp'

    page = requests.get(data_url)
    soup = BeautifulSoup( page.content, 'html.parser')
    a_tag = soup.find_all('a', {'class': 'link link--csv m100'})

    link = a_tag[0].get('href')
    split_link = link.split(' ') 
    split_by_start = split_link[0].split('?') 
    split_by_start[1] = 'startdate=' + START
    split_by_end = split_link[1].split('&')
    split_by_end[1] = 'enddate=' + END
    start = split_by_start[0] + '?' + split_by_start[1]
    end = split_by_end[0] + '&' + split_by_end[1]
    address = start + '&' + end + '&' + split_link[-1]

    new = 2
    webbrowser.open(address, new = new)
    # wait for 5 secs
    time.sleep(5)
    
    # change file name and directory
    path, dirs, files = next(os.walk('/Users/tokyo/Downloads'))
    file = files[0]
    old_file = os.path.join(path, file)
    file_new_name = fileName + '_' + END_YEAR
    new_path = path + '/' + 'data' + '/' + f"{file_new_name}.csv"
    shutil.move(old_file, new_path)

# get data for 21 years
year = 2000
while year < 2006:
    get_data(year, 'nikkei')
    year += 1
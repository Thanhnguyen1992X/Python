import pandas as pd
import requests
from bs4 import BeautifulSoup
import openpyxl


def send_to_telegram(message):

    apiToken = '6032498417:AAGWHLZ35x6w1zZSkGMCyGyZuC14pjiXTkw'
    chatID = '5591599164'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)


url = 'https://s.cafef.vn/lich-su-giao-dich-ned-6.chn'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='pricetable')
    # Extract the rows of the table
    rows = table.find_all('tr')
    for row_id, row in enumerate(rows):
        columns = row.find_all('td')
        # print(f"row={row_id}: {columns}")
        if columns:
            Gia = columns[0].text.strip()
            Khoiluong = columns[1].text.strip()
            Tytrong= columns[2].text.strip()
            
            msg = (f"NED\
                    \nGia: {Gia}\
                    \nKhoi Luong: {Khoiluong}\
                    \nTy Trong: {Tytrong}\n\n")

            print(msg)
            send_to_telegram(msg)
            
            




import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import openpyxl

from datetime import date, timedelta


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


start_date = date(2015, 1, 1)
end_date = date(2023, 8, 16)

csv_file_path = './output1.txt'

with open(csv_file_path, 'w') as f:
    for single_date in daterange(start_date, end_date):


        url = "https://tygiadola.net/TyGia?date=" + single_date.strftime("%d-%m-%Y") + ""
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table', class_='table table-hover table-bordered table-condensed')
            # Extract the rows of the table
            rows = table.find_all('tr')

            for row_id, row in enumerate(rows):
                columns = row.find_all('td')

                # print(f"row={row_id}: {columns}")
                if columns:
                    Muavao = columns[0].text.strip()
                    Banra = columns[1].text.strip()
                    date= single_date.strftime("%d-%m-%Y")
                    msg = (f"USD tu do\
                        \nMua vao: {Muavao}\
                        \nBan ra: {Banra}\n")
                    print(msg)

                    f.write(f'USD tu do {date};Mua vao :{Muavao};Ban Ra :{Banra}\n')


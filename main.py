import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup
import requests


url_stats = 'https://finance.yahoo.com/quote/{}/key-statistics?p={}'
url_profile = 'https://finance.yahoo.com/quote/{}/profile?p={}'
url_financials = 'https://finance.yahoo.com/quote/{}/financials?p={}'



stock = "F"


response = requests.get(url_financials.format(stock, stock))


soup = BeautifulSoup(response.text, 'html.parser')


pattern = re.compile(r'\s--\sData\s--\s')
script_data = soup.find('script', text=pattern).contents[0]



script_data[:500]

script_data[-500:]



start = script_data.find("context")-2

json_data = json.loads(script_data[start: -12])

json_data['context'].keys()


dict_keys(['dispatcher', 'options', 'plugins'])

json_data['context']['dispatcher']['stores']['QuoteSummaryStore'].keys()







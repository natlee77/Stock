# import stocks data  from https://www.alphavantage.co/documentation i json format or .csv
# Required: interval
# Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly

import csv
import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
#interval  15 minut
# CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=TSLA&interval=15min&slice=year1month1&apikey=BDPA07CSY1AKQO97'   

#interval day
CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=BDPA07CSY1AKQO97' 
 
with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)

  
# r = requests.get(CSV_URL)
# data = r.json()

# print(data)
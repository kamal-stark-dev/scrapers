import requests
import pandas as pd
from bs4 import BeautifulSoup 
url = 'https://finance.yahoo.com/most-active/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('div', id="fin-scr-res-table")
thead = table.find('thead')
allTh = thead.find_all('th')
heads = [th.text for th in allTh]
df = pd.DataFrame(columns = heads)
tbody = table.find('tbody')
allTr = tbody.find_all('tr')
for tr in allTr:
    rows = [td.text for td in tr]
    length = len(df)
    df.loc[length] = rows
last_column_label = df.columns[-1]
df = df.drop(columns=[last_column_label])
df.to_csv(r'stocksdata.csv', index=True)
print("Completed!")
# %%
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://ark.intel.com/content/www/us/en/ark/products/series/595/intel-xeon-processors.html"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

table = soup.find_all("table")

first_table = table[0]

table_data = []
rows = first_table.find_all("tr")
for row in rows[1:]:
    td = row.find_all('td')
    table_data.append({
        "product_name": td[0].text.strip(),
        "launch_date": td[2].text.strip(),
        "total_cores": td[3].text.strip(),
        "max_turbo_freq": td[4].text.strip(),
        "processor_base_freq": td[5].text.strip(),
        "cache": td[6].text.strip() 
    })
df = pd.DataFrame(table_data)
df.to_csv('intel.csv')

# %%

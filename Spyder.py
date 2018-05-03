import bs4 as bs
import requests
import numpy as np
import pandas as pd
import re
import os


def extractNumber(string_value):
    number = re.findall(r'\d+', string_value)
    return number


def spider(max_pages):
    page=0
    name = list()
    price = list()

    while page < max_pages:
        url = 'http://www.asos.com/men/hoodies-sweatshirts/cat/?cid=5668&nlid=mw|clothing|shop+by+product/page' + str(page+1)
        source_code = requests.get(url).text
        soup = bs.BeautifulSoup(source_code,"html.parser")

        for link in soup.find_all('a', {'class': '_3x-5VWa'}):
            name.append(link.get('aria-label'))

        for link in soup.find_all('span', {'class':'_342BXW_'}):
            data = link.text
            data = data.strip('£')
            price.append(float(data))

        page = page +1

    name = np.asanyarray(name)
    price = np.asanyarray(price)

    data = {'price':price,'title': name}
    dataFrame = pd.DataFrame(data)
    print(dataFrame)

    return


spider(10)

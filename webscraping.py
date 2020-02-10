#! python3

import requests, bs4

def getTheText(productUrl):
	headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

	res = requests.get(productUrl, headers=headers)
	res.raise_for_status

	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	elements = soup.select('body > div.w3-row.w3-white.w3-padding.w3-hide-medium.w3-hide-small > div.w3-col.s7.w3-margin-top.w3-wide.w3-hide-medium.w3-hide-small > div')
	return elements[0].text.strip()	

price = getTheText('https://www.w3schools.com')

print("The text: " + price)
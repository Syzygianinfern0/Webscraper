import requests
import bs4
res = requests.get('https://nitt.edu')
res.raise_for_status()
resSoup = bs4.BeautifulSoup(res.text)
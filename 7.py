import bs4
file = open('example.html')
fileSoup = bs4.BeautifulSoup(file, 'html.parser')
auth = fileSoup.select('#author')
print(len(auth))
print(auth[0].getText())
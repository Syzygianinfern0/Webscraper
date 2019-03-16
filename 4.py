import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
file = open('RJ PLay.txt', 'wb')
for piece in res.iter_content(100000):
    file.write(piece)
file.close()
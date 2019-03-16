import requests
result = requests.get('https://www.google.com')
try:
    result.raise_for_status()
    print(result.text[:300])
    print(len(result.text))
except Exception as exc:
    print(exc)

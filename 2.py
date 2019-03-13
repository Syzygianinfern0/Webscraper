#Takes Location qurey as argv and opens in GMaps

import webbrowser, sys

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
webbrowser.open('https://www.google.com/maps/place/' + address)
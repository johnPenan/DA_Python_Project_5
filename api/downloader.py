import requests
import json

class Downloader:
    """ This class download the open food fact products from API. """
    def __init__(self):
        for i in range(1, 5):
            r = requests.get(f"https://fr.openfoodfacts.org/cgi/search.pl?action=process&json=1&page={i}&page_size=2")
            print(r.status_code)
            print(r.json())
    


d = Downloader()
print(d)
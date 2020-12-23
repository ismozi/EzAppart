from urllib.request import urlopen as uReq
import requests
from bs4 import BeautifulSoup as soup

class WebScrape():
    def __init__(self, url, searched):
        self.url = url
        self.searched = searched
        self.parsed_page = None
    
    def parsePage(self):
        headers = {'User-Agent': 'Mozilla/5.0'}
        # Starts the scraper
        uClient2 = requests.get(self.url, headers=headers)
        html_page = uClient2.text
        uClient2.close()

        # Parse the html
        parsed_page = soup(html_page, "html.parser")

        return parsed_page

   


        


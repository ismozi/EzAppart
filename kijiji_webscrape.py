import webscrape_module as d
from bs4 import BeautifulSoup as soup

class KijijiScraper(d.WebScrape):
    def __init__(self, url, searched):
        super().__init__(url, searched)
    
    def findApparts(self):
        page = self.parsePage()
        apparts = page.findAll("div", {"class":"info-container"})

        for appart in apparts:
            title = appart.find("div", {"class":"title"}).text.strip()
            price = appart.find("div", {"class":"price"}).text.strip()
            description = appart.find("div", {"class":"description"}).text.strip()
            print("--------------------------------")
            print(f"{title}")
            print(f"Prix: {price}")
            print(f"Description: {description}")
            print("--------------------------------")
        




            

        




    
    

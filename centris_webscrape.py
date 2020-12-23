import webscrape_module as d
from bs4 import BeautifulSoup as soup

class CentrisScraper(d.WebScrape):
    def __init__(self, url, searched):
        super().__init__(url, searched)
    
    def findApparts(self):

        file_rows, address_column, price_column, link_column, img_column = [], [], [], [], []
        link_start = "https://centris.ca"
        page = self.parsePage()
        apparts = page.findAll("div", {"class":"shell"})

        for appart in apparts:

            address = appart.find("span", {"class":"address"}).text.strip()
            address_column.append(address)
            price = appart.find("span", {"itemprop":"price"}).text.strip()
            price_column.append(price)
            link = link_start+appart.find("a")["href"]
            link_column.append(link)
            img = appart.find("img", {"itemprop":"image"})["src"]
            img_column.append(img)

            print("--------------------------------")
            print(f"{address}")
            print(f"Prix: {price}")
            print(f"Lien: {link}")
            print(f"Image: {img}")
            print("--------------------------------")
        
        
        file_rows.append(address_column)
        file_rows.append(price_column)
        file_rows.append(link_column)
        file_rows.append(img_column)

        return file_rows
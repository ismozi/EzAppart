import webscrape_module as d
from bs4 import BeautifulSoup as soup

class KijijiScraper(d.WebScrape):
    def __init__(self, url, searched):
        super().__init__(url, searched)
    
    def findApparts(self):
        link_start = "https://kijiji.ca"
        file_rows, title_column, price_column, description_column, location_column, img_column, link_column = [], [], [], [], [], [], []
        page = self.parsePage()
        apparts = page.findAll("div", {"class":"search-item"})

        for appart in apparts:    
            title = appart.find("div", {"class":"title"}).text.strip()
            title_column.append(title)
            link = link_start + appart.find("div", {"class":"title"}).find("a")["href"]
            link_column.append(link)
            price = appart.find("div", {"class":"price"}).text.strip()
            price_column.append(price)
            description = appart.find("div", {"class":"description"}).text.strip()
            description_column.append(description)
            address = appart.find("div", {"class":"location"}).text.strip()
            location_column.append(address)
            img = appart.find("div", {"class":"image"}).find("img")["src"]
            img_column.append(img)

            print("--------------------------------")
            print(f"Location: {address}")
            print(f"Lien: {link}")
            print(f"Prix: {price}")
            print(f"Description: {description}")
            print(f"Image: {img}")
            print("--------------------------------")
        
    
        file_rows.append(title_column)
        file_rows.append(link_column)
        file_rows.append(price_column)
        file_rows.append(description_column)
        file_rows.append(location_column)
        file_rows.append(img_column)

        return file_rows
        




            

        




    
    

import kijiji_webscrape as scraper

if __name__ == "__main__":
    url = "https://www.kijiji.ca/b-ordinateurs/ville-de-montreal/tablette/k0c16l1700281?rb=true&dc=true"
    
    scrapin = scraper.KijijiScraper(url,"allo")

    scrapin.findApparts()

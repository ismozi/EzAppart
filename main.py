import kijiji_webscrape as scraper
import centris_webscrape as scraper2
import csv

if __name__ == "__main__":
    url = "https://www.kijiji.ca/b-ordinateurs/ville-de-montreal/tablette/k0c16l1700281?rb=true&dc=true"
    
    # url2 = "https://www.centris.ca/fr/condo-appartement~a-louer?uc=2"

    scrapin = scraper.KijijiScraper(url,"allo")
    appartz = scrapin.findApparts()

    # scrapin2 = scraper2.CentrisScraper(url2,"allo")
    # appartz2 = scrapin2.findApparts()

    # with open("EzAppart.csv", mode="w", encoding='utf-8') as f:
    #     appartz_writer = csv.writer(f, delimiter=",")
    #     appartz_writer.writerow(["Title", "Price", "Description"])

    #     for i in range(len(appartz[0])):
    #         appartz_writer.writerow([appartz[0][i], appartz[1][i], appartz[2][i]])




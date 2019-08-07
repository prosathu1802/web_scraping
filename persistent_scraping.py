import urllib.request
from bs4 import BeautifulSoup
import sqlite3


class SaveToDatabase:
    def __init__(self,data):
        self.data = data

    def create_database(self):
        conn = sqlite3.connect("persistent_scraping.db")
        conn.execute('''CREATE TABLE celebs 
                            (name text, networth int)''')

    def add_to_database(self):
        conn = sqlite3.connect("persistent_scraping.db")
        for data in self.data:
            conn.execute("INSERT INTO celebs VALUES " + str((data, self.data[data])))
        # Save (commit) the changes
        conn.commit()
        conn.close()

    def get_database(self):
        conn = sqlite3.connect("persistent_scraping.db")
        for row in conn.execute('SELECT * FROM celebs'):
            print(row)

class Scraper:
    def __init__(self, site):
        self.site = site
        self.links = set()
        self.celebs = {}

    def get_links(self, number_of_pages):
        for i in range(1, number_of_pages):
            response = urllib.request.urlopen(self.site + str(i))
            soup = BeautifulSoup(response, "html.parser")
            for a in soup.find_all("a", href=True):
                link = a['href']
                if '-net-worth/' in link:
                    self.links.add(link)

    def scrape_networth(self, number_of_pages):
        self.get_links(number_of_pages)
        for link in self.links:
            response = urllib.request.urlopen(link)
            soup = BeautifulSoup(response.read(),"html.parser")
            try:
                for c in soup.find_all('meta', { "itemprop": "name"}, content=True):
                    name = c['content']
                    networth = soup.findAll('div', {"class": 'value'})[0].text
                    self.celebs[name]=networth
            except IndexError:
                pass

    def get_networth_by_name(self, number_of_pages, name):
        self.scrape_networth(number_of_pages)
        if name in self.celebs:
            print(self.celebs[name])
        else:
            print("Data not available")


scrape = Scraper("https://www.celebritynetworth.com/category/richest-celebrities/page/")
scrape.get_networth_by_name(3, "Richard Tandy")
print(scrape.celebs)
scrape.scrape_networth
save = SaveToDatabase(scrape.celebs)
save.create_database()
save.add_to_database()
save.get_database()

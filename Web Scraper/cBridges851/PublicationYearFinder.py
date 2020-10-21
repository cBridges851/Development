class PublicationYearFinder():
    def __init__(self, soup):
        self.soup = soup

    def find(self):
        return self.soup.find("time").attrs["datetime"][0:4]
class TitleFinder():
    def __init__(self, soup):
        self.soup = soup

    def find(self):
        return self.soup.find("h1").get_text()
class PublicationYearFinder():
    def __init__(self, soup):
        self.soup = soup

    def find(self):
        if self.soup.find("time") != None:
            return self.soup.find("time").attrs["datetime"][0:4]

        websiteNameMeta = self.soup.find(attrs={"itemprop" : "datePublished"})
        return websiteNameMeta.attrs["content"][0:4]
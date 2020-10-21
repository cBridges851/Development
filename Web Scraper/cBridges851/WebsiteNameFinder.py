class WebsiteNameFinder():
    def __init__(self, soup, deserializedJson):
        self.soup = soup
        self.deserializedJson = deserializedJson

    def find(self):
        return self.deserializedJson["publisher"]["name"]
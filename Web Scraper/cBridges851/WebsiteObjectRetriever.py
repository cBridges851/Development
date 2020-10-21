import json


class WebsiteObjectRetriever():
    def __init__(self, soup):
        self.soup = soup

    def retrieve(self):
        scriptTag = self.soup.find("script")
        scriptTagContents = scriptTag.contents
        return json.loads(scriptTagContents[0])

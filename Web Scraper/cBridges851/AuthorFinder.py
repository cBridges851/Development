class AuthorFinder():
    def __init__(self, soup, deserializedJson):
        self.soup = soup
        self.deserializedJson = deserializedJson

    def find(self):
        if self.soup.findAll("link") != None:
            allLinkTags = self.soup.findAll("link")
            for linkTag in allLinkTags:
                if linkTag.get("content") != None:
                    return linkTag.get("content")

        author = self.deserializedJson["author"]["name"]
        author = author.split(" ")
        return author[2] + ", " + author[1][0] + "."
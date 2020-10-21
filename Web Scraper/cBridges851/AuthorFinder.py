class AuthorFinder():
    def __init__(self, soup, deserializedJson):
        self.soup = soup
        self.deserializedJson = deserializedJson

    def find(self):
        author = self.deserializedJson["author"]["name"]
        author = author.split(" ")
        return author[2] + ", " + author[1][0] + "."
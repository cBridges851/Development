# CB 2020-10-18 Importing the necessary libraries
from sys import argv, exit
import requests
from bs4 import BeautifulSoup
import json
from flask import Flask, render_template

app = Flask(__name__)

if len(argv) != 2:
    print("Usage: cBridges851_web-scraper.py <url>")
    exit(1)

url = argv[1]

try:
    response = requests.get(url)

except:
    print("A GET request could not be made to the URL you inputted.")

soup = BeautifulSoup(response.text, "html.parser")

# Find Author
scriptTag = soup.find("script")
scriptTagContents = scriptTag.contents
deserializedJson = json.loads(scriptTagContents[0])
author = "Author: " + deserializedJson["author"]["name"]

# Find Title
title = "Title: " + soup.find("h1").get_text()

# Find Name of Website
websiteName = "Name of Website: " + deserializedJson["publisher"]["name"]

# Find Year Of Publication
publicationYear = soup.find("time").attrs["datetime"][0:4]


@app.route("/")
def output():
    return render_template("output.html")

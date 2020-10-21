from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import json
from datetime import date

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit")
def submit():
    # CB 2020-10-19 Get the url from the url box
    url = request.args.get("urlBox")
    
    # CB 2020-10-19 try to make a GET request to the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")    

    # Find Author
    scriptTag = soup.find("script")
    scriptTagContents = scriptTag.contents
    deserializedJson = json.loads(scriptTagContents[0])
    author = deserializedJson["author"]["name"]
    author = author.split(" ")
    author = author[2] + ", " + author[1][0] + "."

    # Find Title
    title = soup.find("h1").get_text()

    # Find Name of Website
    websiteName = deserializedJson["publisher"]["name"]

    # Find Year Of Publication
    publicationYear = soup.find("time").attrs["datetime"][0:4]

    currentDate = date.today()
    
    return render_template("output.html", url=url, author=author, title=title, websiteName=websiteName, publicationYear=publicationYear, currentDate=currentDate)

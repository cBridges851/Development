from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import json

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
    soup = BeautifulSoup(response.text)    

    # Find Author
    scriptTag = soup.find("script")
    scriptTagContents = scriptTag.contents
    deserializedJson = json.loads(scriptTagContents[0])
    author = "Author: " + deserializedJson["author"]["name"]

    return render_template("output.html", url=url, author=author)

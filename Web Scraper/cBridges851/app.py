from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from TitleFinder import TitleFinder
from AuthorFinder import AuthorFinder
from WebsiteObjectRetriever import WebsiteObjectRetriever
from WebsiteNameFinder import WebsiteNameFinder
from PublicationYearFinder import PublicationYearFinder
from CurrentDateFinder import CurrentDateFinder

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

    websiteObjectRetriever = WebsiteObjectRetriever(soup)
    deserializedJson = websiteObjectRetriever.retrieve()

    # Find Author
    authorFinder = AuthorFinder(soup, deserializedJson)
    author = authorFinder.find()

    # Find Title
    titleFinder = TitleFinder(soup)
    title = titleFinder.find()

    # Find Name of Website
    websiteNameFinder = WebsiteNameFinder(soup, deserializedJson)
    websiteName = websiteNameFinder.find()

    # Find Year Of Publication
    publicationYearFinder = PublicationYearFinder(soup)
    publicationYear = publicationYearFinder.find()
    
    # Get Current Date
    currentDateFinder = CurrentDateFinder()
    currentDate = currentDateFinder.find()
    
    return render_template("output.html", url=url, author=author, title=title, websiteName=websiteName, publicationYear=publicationYear, currentDate=currentDate)

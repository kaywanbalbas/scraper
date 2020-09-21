import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

load_dotenv()
password = os.getenv("mdbpassword")

# Load cluster, database, and collection from MongoDB
cluster = MongoClient(f"mongodb+srv://admin:{password}@cluster0.hq1ye.mongodb.net/scrape-db?retryWrites=true&w=majority")
db = cluster["scrape-db"]
collection = db["blog"]

baseurl = 'https://www.cartalk.com'
url = 'https://www.cartalk.com/blogs/latest'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='col-md-4 mb-2')

nextid = 0
for post in posts:
    postinfo = post.find(class_='py-1')
    title = postinfo.find('h2').get_text()\
        .replace('\n', '')
    link = baseurl + post.find('a')['href']
    date = postinfo.find('h5').get_text()
    post = {"_id": nextid, "title": title, "link": link, "date": date}
    collection.insert_one(post)
    nextid += 1

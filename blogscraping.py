import requests
from bs4 import BeautifulSoup
from csv import writer

baseurl = 'https://www.cartalk.com'
url = 'https://www.cartalk.com/blogs/latest'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='col-md-4 mb-2')

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Link', 'Date']
    csv_writer.writerow(headers)

    for post in posts:
        postinfo = post.find(class_='py-1')
        title = postinfo.find('h2').get_text()\
            .replace('\n', '')
        link = baseurl + post.find('a')['href']
        date = postinfo.find('h5').get_text()
        csv_writer.writerow([title, link, date])
        print(title, link, date, '\n')

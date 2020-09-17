from bs4 import BeautifulSoup

html_doc = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="X-UA-Compatible" content="ie=edge" />
        <title>My Webpage</title>
    </head>
    <body>
        <div id="section-1">
            <h3 data-hello="hi">Hello</h3>
            <img src="https://source.unsplash.com/200x200/?nature,water" />
            <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto
                culpa cumque velit aperiam officia molestias maiores qui
                officiis incidunt. Omnis vitae eveniet reprehenderit excepturi
                officiis quod, eum natus voluptatem nihil fugit necessitatibus
                dolorum quae accusamus aliquid enim fuga dicta beatae!
            </p>
        </div>
        <div id="section-2">
            <ul class="items">
                <li class="item"><a href="#">Item 1</a></li>
                <li class="item"><a href="#">Item 2</a></li>
                <li class="item"><a href="#">Item 3</a></li>
                <li class="item"><a href="#">Item 4</a></li>
                <li class="item"><a href="#">Item 5</a></li>
            </ul>
        </div>
    </body>
</html>"""

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.body)

# find(): only finds first element with given parameter

# firstdiv = soup.find('div')
# print(first)

# find_all() or findAll() returns all elements with given parameter
# alldivs = soup.find_all('div')
# print(alldivs)

# seconddiv = soup.find_all('div')[1]
# print(seconddiv)

# findbyid = soup.find(id='section-1')
# print(findbyid)

# findbyclass = soup.find(class_='items')
# print(findbyclass)

# findbyattribute = soup.find(attrs={"data-hello":"hi"})
# print(findbyattribute)

# select(): similar to selenium/jquery, uses css selector and returns a list

# sel = soup.select('#section-1')
# sel = soup.select('#section-1')[0]
# sel = soup.select('.item')[0]
# print(sel)

# get_text()

# gt = soup.find(class_='item').get_text()
# print(gt)

# for item in soup.select('.item'):
#     print(item.get_text())

# Navigation

# nav = soup.body.contents[1].contents[1].find_next_sibling()
# nav = soup.find(id='section-2').find_previous_sibling()
# nav = soup.find(class_='item').find_parent()
# nav = soup.find('h3').find_next_sibling('p')
# print(nav)

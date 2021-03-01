import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


URL = 'https://losangeles.craigslist.org/search/?query={}'
IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'


def parser(search):
    final_url = URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})

    final_postings = []

    for post in post_listings:
        post_title = post.find(class_="result-title").text
        post_url = post.find('a').get('href')
        if post.find(class_="result-price"):
            post_price = post.find(class_="result-price").text
        else:
            post_price = 'N/A'

        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = IMAGE_URL.format(post_image_id)
        else:
            post_image_url = 'none'

        final_postings.append((post_title, post_url, post_price, post_image_url))

    return final_postings

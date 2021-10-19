#!/usr/bin/env python

from PIL import Image
import imgkit
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.lemon64.com/news/')
c = r.content
soup = BeautifulSoup(c, features="html.parser")
main_content = soup.find('body')
content = main_content.find('div', attrs={'id': 'rnd_review'})
all_img = content.find_all('img')
for img in all_img:
    img_url = img['src']
    content.find('img', attrs={'alt': img['alt']})['src'] = 'https://www.lemon64.com'+img_url
imgkit.from_string(content.prettify(), 'review.jpg', options={'quiet': ''})
img = Image.open('review.jpg')
img.show()

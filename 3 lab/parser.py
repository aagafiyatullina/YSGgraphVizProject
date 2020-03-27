import requests
from bs4 import BeautifulSoup
import re

def regex(soup):
    result = str(re.sub("<.*?>", "", str(soup)))
    return result

def get_page(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html5lib')
    return soup

##soup1 = get_page('https://habr.com/ru/company/mailru/blog/449416/')

def parse_page_head(soup):
    title = soup.findAll('title')
    title_text = regex(title)
    pre_author = soup.find('a', attrs={'class':"post__user-info user-info"})
    author = pre_author.findAll('span', text=True)
    author_text = regex(author)
    output = []
    output.append(title_text)
    output.append(author_text)
    return output

def parse_page_comments(soup):
    comments = soup.find_all('div', attrs={'class':'comment__head'})
    comment_authors = []
    for i in comments:
        x = i.find('a', {'class':'user-info user-info_inline'})['data-user-login']
        comment_authors.append(x)
    return comment_authors

def parse_main_page(soup):
    x = soup.findAll('a', attrs={'class':'post__title_link'})
    links = []
    for i in x:
        link = i['href']
        links.append(link)
    return links

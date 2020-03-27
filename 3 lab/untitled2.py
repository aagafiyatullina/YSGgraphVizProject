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
soup1 = get_page('https://habr.com/ru/company/yandex/blog/450376/')

title = soup1.findAll('title')
title_text = regex(title)
pre_author = soup1.find('a', attrs={'class':"post__user-info user-info"})
author = pre_author.findAll('span', text=True)
author_text = regex(author)
output = []
output.append(title_text)
output.append(author_text)
pre_article_id = soup1.find('article', attrs={'class':'post post_full'})
##article_id = pre_article_id['data-id']
##print(article_id)
article_id = pre_article_id['id']
article_id = article_id[5:]

comments = []
comments_tree = {}
pre_comments = soup1.findAll('div', attrs={'class':'comment__head'})
for i in pre_comments:
     commentator = i.find('a', {'class':'user-info user-info_inline'})['data-user-login']
     com_id = i['rel']
     pair = [commentator, com_id]
     comments.append(pair)
     comments_tree[com_id] = '0'

for i in comments_tree:
    pre_parent = soup1.find('a', attrs={'data-id':i, 'class':'icon_comment-arrow-up js-comment_parent'})
    if (pre_parent):
        parent = pre_parent['data-parent_id']
        comments_tree[i] = parent
for i in comments_tree:
    if comments_tree[i] == '0':
        comments_tree[i] = article_id

##def parse_page_comments(soup):
##comments = soup1.find_all('div', attrs={'class':'comment__head'})
##comment_authors = []
##for i in comments:
  ##  x = i.find('a', {'class':'user-info user-info_inline'})['data-user-login']
    ##comment_authors.append(x)
    ##return comment_authors

##def parse_main_page(soup):
  ##  x = soup.findAll('a', attrs={'class':'post__title_link'})
    ##links = []
    ##for i in x:
      ##  link = i['href']
        ##links.append(link)
    ##return links

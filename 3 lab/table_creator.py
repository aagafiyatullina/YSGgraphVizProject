import pandas as pd
import parser

def make_tables(link):
    users = pd.DataFrame(columns=['Nickname'])
    articles = pd.DataFrame(columns=['Title'])
    author = pd.DataFrame(columns=['Author', 'Title'])
    commentator = pd.DataFrame(columns=['Title', 'Commentator'])
    soup = get_page(link)
    links = parse_main_page(soup)
    for i in links:
        page = get_page(i)
        head = parse_page_head(page)
        comments = parse_page_comments(page)
        article = head[0]
        user = head[1]
        users = users.append(pd.Series([user]), ignore_index=True)
        articles = articles.append(pd.Series([article]), ignore_index=True)
        author = author.append(pd.Series([user, article]), ignore_index=True)
        for j in comments:
            commentator = commentator.append(pd.Series([article, j]), ignore_index=True)
    
    users.to_csv('users.csv', mode='a', header=False)
    articles.to_csv('articles.csv', mode='a', header=False)
    author.to_csv('author.csv', mode='a', header=False)
    commentator.to_csv('commentator.csv', mode='a', header=False)

for i in range(101, 185):
    print(i)
    html = 'https://habr.com/ru/hub/machine_learning/page' + str(i) + '/'
    make_tables(html)

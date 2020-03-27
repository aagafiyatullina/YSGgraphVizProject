import pandas as pd
import parser

def make_tables(link):
    users = pd.DataFrame(columns=['user'])
    content = pd.DataFrame(columns=['c_id', 'user', 'type'])
    comments_forest = {}
    soup = get_page(link)
    links = parse_main_page(soup)
    for i in links:
        page = get_page(i)
        author, article_id = parse_article(page)
        users = users.append(pd.Series([author]), ignore_index=True)
        content = content.append(pd.Series([article_id, author, 0]), ignore_index=True)
        comments, comments_tree = parse_page_comments(page)
        for j in comments:
            content = content.append(pd.Series([j[1], j[0], 1]), ignore_index=True)
        comments_forest.update(comments_tree)
    print(content)
    print(users)
    comments_forest_pd = pd.DataFrame.from_dict(comments_forest, orient='index')
    print(comments_forest_pd)
    users.to_csv('users.csv', mode='a', header=False)
    content.to_csv('content.csv', mode='a', header=False)
    comments_forest_pd.to_csv('comments_forest.csv', mode='a', header=False)

for i in range(63, 190):
    print(i)
    html = 'https://habr.com/ru/hub/machine_learning/page' + str(i) + '/'
    make_tables(html)
   
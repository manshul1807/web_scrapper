import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body.contents)

# print(soup.find_all('div'))  # to get all divs

# print(soup.find_all('a'))  # find all a tag

# print(soup.title)  # to get title

# print(soup.a)  # to get first a tag ( link )

# print(soup.find('a'))  # other way to find first a tag

# print(soup.find(id='score_23053981'))  # to get the score on the basis of id

# print(soup.select('a'))  # CSS selector

# print(soup.select('.score'))

# print(soup.select('#score_23053981'))


# To grab all the links for class storyline (top stories title)

# print(soup.select('.storylink'))  # dot notation means class

# print(soup.select('.storylink')[0])  # to pull first item from the list

# print(soup.select('.score')[0])  # to pull first item from the score

# To grab all the stories and their votes classes
links = soup.select('.storylink')
subtext = soup.select('.subtext')

# to grab score of particular id
# print(votes[0].get('id'))


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


def sort_stories_by_votes(li):
    return sorted(li, key=lambda k: k['votes'], reverse=True)


pprint.pprint(create_custom_hn(links, subtext))

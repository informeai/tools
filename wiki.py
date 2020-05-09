import requests as req
from bs4 import BeautifulSoup


def wiki(text):
    url = req.get(f'https://pt.wikipedia.org/wiki/{text}')
    soup = BeautifulSoup(url.text, 'html.parser')
    return soup.get_text()



if __name__ == '__main__':
    u = wiki('python')
    print(u)
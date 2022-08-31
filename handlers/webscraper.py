from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_job_post():
    url = input('Enter a link to the job post:\n\t')

    page = urlopen(url)
    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()

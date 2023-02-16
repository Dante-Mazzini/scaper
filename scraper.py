# libraries importation
from multiprocessing.sharedctypes import Value
import requests
import lxml.html as html

#url
HOME_URL = "https://www.larepublica.co/"

# constants
XPATH_LINK_TO_ARTICLE = '//div[@class="news V_Title_Img" or @class="V_Title"]/text-fill/a/@href'
XPATH_TITLE = '//h1[@class="headline"]/a/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="articleWrapper  "]/p[not(@class)]/text()'

# function for extracting links from news
def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            print(links_to_notices)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()



if __name__ == '__main__':
    run()


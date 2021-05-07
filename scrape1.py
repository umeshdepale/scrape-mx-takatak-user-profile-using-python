import requests
import re
from json import JSONDecoder
from bs4 import BeautifulSoup

#enter user profile link
url = 'https://www.mxtakatak.com/12112868004850123567790'

#use Proxy If needed
proxy_host = ""
proxy_port = ""
proxy_auth = ""
proxies = {
       "https": "https://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
       "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)
}

#User Agent
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

r = requests.get(url, headers=headers)
html = r.content
soup = BeautifulSoup(html, 'html.parser')
text = 'window._state'
data = soup.find(string=re.compile('.*{0}.*'.format(text)), recursive=True)

#extract json object from the script
def extract_json_objects(text, decoder=JSONDecoder()):

    pos = 0
    while True:
        match = text.find('{', pos)
        if match == -1:
            break
        try:
            result, index = decoder.raw_decode(text[match:])
            yield result
            pos = match + index
        except ValueError:
            pos = match + 1

for result in extract_json_objects(data):
    print(result)

#For any update or feature you can contact me on telegram @mr_awesome007

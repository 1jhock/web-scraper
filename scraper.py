import requests
from bs4 import BeautifulSoup

keyword = 'Stranger Things 2'

urlEncodeKeyword = keyword.replace(' ', '+')

url = 'http://1337x.to/search/'+urlEncodeKeyword+'/1/'



r = requests.get(url)

if(r.status_code == 200):
	print 'Web has been successfully scraped.'
else:
	print 'Error occured.'


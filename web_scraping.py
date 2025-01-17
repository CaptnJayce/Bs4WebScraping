from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/kingspec-1tb-xf-series/p/0D9-000D-00153?Item=9SIB1V8HP71345&cm_sp=SD-_-2812144-_-Pers_ProductSponsoredDisplay+2812149-_-9-_-9SIB1V8HP71345-_-9SIB1V8JVN5929-_--_-1"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(string="$")
parent = prices[1].parent # 1 instead of 0 as to bypass the strong tag for the advertisement
strong = parent.find("strong")
print(strong.string)
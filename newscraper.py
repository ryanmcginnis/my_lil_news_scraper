from newspaper import Article
from sys import argv

try:
	url = argv[1]
except:
	print("You need to pass in a URL. Quitting...\n"); quit()

article = Article(url)
article.download()
article.parse()
print(article.text)
import nltk
from newspaper import Article

url = input()
article = Article(url)

article.download()
article.parse()
nltk.download('punkt')
article.nlp()

print(article.authors)
print(article.publish_date)
# print(article.text)
print(article.summary)
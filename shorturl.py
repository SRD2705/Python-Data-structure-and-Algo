import pyshorteners
link = input("Enter the link: ")
shortener = pyshorteners.Shortener()
res = shortener.tinyurl.short(link)
print(res)
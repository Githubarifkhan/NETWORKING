import urllib.request

try:
    file =urllib.request.urlopen("https://www.python.org/")
    content =file.read()

except urllib.error.HTTPError:
    print("webpage does not exist")
    exit()

f= open("webpage.html",'wb')
f.write(content)

f.close()
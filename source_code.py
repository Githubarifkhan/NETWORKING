import urllib.request

file =urllib.request.urlopen("http://www.python.org/")
print(file.read())
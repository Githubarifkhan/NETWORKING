import  urllib.parse

#take any url
url = "https://eckovation.com/course/python-programing#curriculum"

tpl =urllib.parse.urlparse(url)



print("scheme =",tpl.scheme)
print("net location =", tpl.netloc)
print("parameters =",tpl.params)
print("port no.=",tpl.port)
print("total url=",tpl.geturl)
import urllib
from urllib.request import urlopen
url="http://az.lib.ru/d/dostoewskij_f_m/"
html1=urlopen(url)
page=html1.read()
fh=open('text.txt','w')
fh.write(str(page))
fh.close()
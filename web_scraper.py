import urllib.request

response = urllib.request.urlopen('https://www.eimj.org/uplode/images/photo/%D8%A3%D9%86%D9%85%D8%A7%D8%B7_%D8%A7%D9%84%D9%82%D9%8A%D8%A7%D8%AF%D8%A9_%D8%A7%D9%84%D9%85%D8%AF%D8%B1%D8%B3%D9%8A%D8%A9_%D9%88%D8%AF%D9%88%D8%B1%D9%87%D8%A7_%D9%81%D9%8A_%D8%AA%D8%B9%D8%B2%D9%8A%D8%B2_%D8%B9%D9%84%D8%A7%D9%82%D8%A9_%D8%A3%D9%88%D9%84%D9%8A%D8%A7%D8%A1_%D8%A7%D9%84%D8%A3%D9%85%D9%88%D8%B1_%D8%A8%D8%A7%D9%84%D9%85%D8%AF%D8%B1%D8%B3%D8%A9..pdf')    
file = open("FILENAME.pdf", 'wb')
file.write(response.read())
file.close()

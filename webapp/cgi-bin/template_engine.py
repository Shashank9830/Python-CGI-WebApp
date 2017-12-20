def cgi_content(type="text/html"):
	return('Content type: ' + type + '\n\n')

def webpage_start():
	return('<html>')

def web_title(title):
	return('<head><title>' + title + '</title></head>')

def body_start(h1_message):
	return('<h1 align="center">' + h1_message + '</h1><p align="center">')

def body_end():
	return("</p><br><p align='center'><a href='../index.html'>HOME</a></p></body>")

def webpage_end():
	return('</html>')
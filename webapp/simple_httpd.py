
from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8080

try:
    httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
    print("Starting simple_httpd on port: " + str(httpd.server_port))
    httpd.serve_forever()
    
except KeyboardInterrupt as err:
    print("User pressed Ctrl + C : " + str(err))


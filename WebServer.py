import http.server
import socketserver

# Run simple http server that will make content of current directory (location of the python script file) accessible to web browser
# alternative to this code is run following code from command line:     python -m http.server --cgi 8000

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
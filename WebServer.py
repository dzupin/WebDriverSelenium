import http.server
import socketserver

# Run simple http server that will make content of local directory (where is the script) accessible to web browser
# alternative to this code is run following code from command line:     python -m http.server --cgi 8000
PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
from http.server import BaseHTTPRequestHandler

 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        text="Hello Toto98"
        self.wfile.write( text.encode('utf-8'))
        return
"""
This is a python program to test GET/POST requests for a custom python web server.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

server_name = ''
server_port = 8008

class CustomRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(file_to_open), 'utf-8')
        except:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 - Not Found!')

    def do_POST(self):
        '''Parse the form data'''
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'Content-type': self.headers['Content-type']
            }
        )

        # Get the form values
        first_name = form.getvalue('first_name')
        last_name = form.getvalue('last_name')

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, ' + first_name.encode() + b' ' + last_name.encode())

if __name__=='__main__':
    httpd = HTTPServer((server_name, server_port), CustomRequestHandler)
    httpd.serve_forever()

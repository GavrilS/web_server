"""
Python custom web server.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

host_name = 'localhost'
server_port = 8088

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://localhost.com</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))



if __name__=='__main__':
    web_server = HTTPServer((host_name, server_port), MyServer)
    print('Server started https://%s:%s' % (host_name, server_port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    web_server.server_close()
    print('Server stopped!')

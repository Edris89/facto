import http.server
import socketserver
from io import BytesIO

PORT = 8084
Handler = http.server.SimpleHTTPRequestHandler


    

class S(Handler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    # def do_GET(self):
    #     self._set_headers()
    #     self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        #self._set_headers()
        #self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())

# def run(server_class=http.server, handler_class=S, port=PORT):
#     server_address = ('', port)
#     httpd = server_class(server_address, handler_class)
#     print('Starting httpd...')
#     httpd.serve_forever()


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), S) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


# from http.server import HTTPServer, BaseHTTPRequestHandler


# from io import BytesIO
# import os.path

# class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

#     def do_GET(self):
#         possible_name = self.path.strip("/")+'.html'
#         self.send_response(200)
#         self.end_headers()
#         #self.wfile.write(b'Hello, world!')
#         if self.path == '/':
#             # default routing, instead of "index.html"
#             self.path = '/index.html'
#         elif os.path.isfile(possible_name):
#             # extensionless page serving
#             self.path = possible_name

        

#     def do_POST(self):
#         content_length = int(self.headers['Content-Length'])
#         body = self.rfile.read(content_length)
#         self.send_response(200)
#         self.end_headers()
#         response = BytesIO()
#         response.write(b'This is POST request. ')
#         response.write(b'Received: ')
#         response.write(body)
#         self.wfile.write(response.getvalue())


# httpd = HTTPServer(('localhost', 8081), SimpleHTTPRequestHandler)
# httpd.serve_forever()
import BaseHTTPServer
import urlparse

class MyHTTPServer(BaseHTTPServer.HTTPServer):
    def __init__(self,server_address, handler_class):
        BaseHTTPServer.HTTPServer.__init__(self,server_address, handler_class)

    def i(self):
        try:
            self._i
        except AttributeError:
            self._i = 0

        self._i+=1
        return self._i
        
class MyHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
            
            message = urlparse.urlparse(self.path)
            message = list("0123")
            
            self.wfile.write(message[self.server.i() % len(message)])
            print self.client_address
            

    def do_POST(self):
        print "post"

def run(server_class=MyHTTPServer,
        handler_class=MyHTTPRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run(MyHTTPServer,MyHTTPRequestHandler)

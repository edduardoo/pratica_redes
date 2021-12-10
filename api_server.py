import http.server
import socketserver
import json

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api':
            self.send_response (200)
            self.send_header("Content -type", "text/html")
            self.end_headers()
            resposta = {"movie":"Back to the future II"}
            content = json.dumps(resposta)
            self.wfile.write(bytes(content , "utf8"))
            return

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()
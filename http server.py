import http.server
import socketserver

PORT=8000

Handler=http.server.SimpleHTTPRequestHandler
httpd=socketserver.TCPServer(("",PORT),Handler)
print("server at PORT",PORT)
httpd.serve_forever()

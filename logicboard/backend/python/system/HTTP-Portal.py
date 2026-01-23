from http.server import HTTPServer, BaseHTTPRequestHandler

Host = "192.168.0.1"

Port = 6969





class ServerTTP(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")

		self.end_headers()




server = HTTPServer((Host, Port), HTTPServer)

server.serve_forever()
server.server_close()
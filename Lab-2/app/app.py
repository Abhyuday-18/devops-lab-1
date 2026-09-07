from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = os.environ.get("MESSAGE", "DevOps Lab 1 - CI/CD Pipeline is Working!").encode()

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-Length", str(len(message)))
        self.end_headers()
        self.wfile.write(message)

    def log_message(self, format, *args):
        return


def run_server():
    server = HTTPServer(("0.0.0.0", 8000), AppHandler)
    print("Application running on http://localhost:8000")
    server.serve_forever()


if __name__ == "__main__":
    run_server()

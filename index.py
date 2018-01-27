import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

class HandlerClass(BaseHTTPRequestHandler):
    def do_GET(self):
        print('Get request received')
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send the html message
        htmlMessage = self.build_html()
        self.wfile.write(htmlMessage.encode())
        return

    def build_html(self):

        time_now = datetime.now()
        ts = time_now.strftime('%Y-%m-%d %H:%M:%S')

        ipAddress = self.get_public_ip_address()

        htmlString = "<!DOCTYPE html> <html> <body><center><h1>Ip address</h1></center> \n" \
                     "<center><p style=\"font-size:100%\">last updated: {} &gt publicIp: &lt<font color=\"blue\">{}</font>&gt</p></center> \n" \
                     "</body> </html>".format(str(ts), ipAddress);

        return htmlString

    def get_public_ip_address(self):
        try:
            res = requests.get("https://api.ipify.org/")
            return res.text
        except Exception as e:
            pass
            return str(e)

if __name__ == '__main__':
    try:
        Protocol     = "HTTP/1.0"
        addr = "0.0.0.0"
        port = 80
        HandlerClass.protocol_version = Protocol
        httpd = HTTPServer((addr, port), HandlerClass)
        sa = httpd.socket.getsockname()
        print("Serving HTTP on", sa[0], "port", sa[1], "...")
        httpd.serve_forever()
    except:
        exit()
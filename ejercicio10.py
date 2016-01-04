import SimpleHTTPServer
import SocketServer
from urlparse import urlparse, parse_qs

PORT = 8000

class HttpHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        print "REQUESTED RESOURCE: " , self.path
        if 'search' in self.path:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            query_components = parse_qs(urlparse(self.path).query)
            print query_components['term'][0]
            self.wfile.write('<!DOCTYPE html>')
            self.wfile.write('<html>')
            self.wfile.write('  <head>')
            self.wfile.write('    <title>CSSAI - Practica III</title>')
            self.wfile.write('  </head>')
            self.wfile.write('<body>')
            self.wfile.write('  <h1>Pratica III - Ejercicio 8</h1>')
            self.wfile.write('  <form action="/search">')
            self.wfile.write('    <input type="text" name="term"/>')
            self.wfile.write('    <input type="submit" value="buscar"/>')
            self.wfile.write('  </form>')
            self.wfile.write('  <table>')
            if query_components['term'][0] in "bigbuckbunny":
                self.wfile.write('<tr><td>')
                self.wfile.write('  <video src="http://download.blender.org/peach/bigbuckbunny_movies/big_buck_bunny_480p_surround-fix.avi"')
                self.wfile.write('           poster ="http://media.xiph.org/BBB/BBB-360-png/big_buck_bunny_00703.png"')
                self.wfile.write('            width=400/>')
                self.wfile.write('</td></tr>')
            if query_components['term'][0] in "sintel":
                self.wfile.write('<tr><td>')
                self.wfile.write('    <video src="http://media.w3.org/2010/05/sintel/trailer.webm"')
                self.wfile.write('           poster="http://media.w3.org/2010/05/sintel/poster.png" width=400 controls/>')
                self.wfile.write('</td></tr>')
            if query_components['term'][0] in "chrome":
                self.wfile.write('<tr><td>')
                self.wfile.write('    <video  src="http://simpl.info/video/video/chrome.webm"')
                self.wfile.write('       poster = "http://simpl.info/video/images/poster.jpg" width=400 controls/>')
                self.wfile.write('</td></tr>')
            self.wfile.write('    </table>')
            self.wfile.write('  </body>')
            self.wfile.write('</html>')
        else:
            return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpd = SocketServer.TCPServer(("", PORT), HttpHandler)
print "serving at port", PORT
httpd.serve_forever()

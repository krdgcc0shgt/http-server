#!/usr/bin/env python3
import http.server
import ssl

HOST='127.0.0.1'
PORT=8001
Handler = http.server.SimpleHTTPRequestHandler
with http.server.HTTPServer((HOST, PORT), Handler) as httpd:
    print("Web Server listening at => " + HOST + ":" + str(PORT))
    sslcontext = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    sslcontext.load_cert_chain(keyfile="key.pem", certfile="cert.pem")
    httpd.socket = sslcontext.wrap_socket(httpd.socket, server_side=True)
    httpd.serve_forever()

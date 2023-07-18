k150411936

rgc

# Create your site certificates
mkcert from https://github.com/FiloSottile/mkcert

release 1.4.4

https://github.com/FiloSottile/mkcert/releases/download/v1.4.4/mkcert-v1.4.4-linux-amd64

https://github.com/FiloSottile/mkcert/releases/download/v1.4.4/mkcert-v1.4.4-windows-amd64.exe


LINUX

[1] install (and create a root CA)
```
$ mkcert-v1.4.4-linux-amd64 -install
```

[2] create site certificates
```
$ mkcert-v1.4.4-linux-amd64 localhost 127.0.0.1 ::1
```

Created a new certificate valid for the following names 📜
 - "localhost"
 - "127.0.0.1"
 - "::1"

The certificate is at "./localhost+2.pem" and the key at "./localhost+2-key.pem" ✅

It will expire on 18 October 2025 🗓

- Common/simple security practice.
  - Please consider "./localhost+2.pem" as public.
  - Please consider "./localhost+2-key.pem" as private. Do not share.

[3] where is the root CA certificate
```
$ mkcert-v1.4.4-linux-amd64 -CAROOT
/home/rgc/.local/share/mkcert
$ ls -la /home/rgc/.local/share/mkcert
total 20
drwxr-sr-x  2 rgc rgc 4096 Jul  4 12:38 ./
drwxr-sr-x 11 rgc rgc 4096 Jul  7 11:45 ../
-r--------  1 rgc rgc 2488 Jul  4 12:20 rootCA-key.pem
-rw-r--r--  1 rgc rgc 1700 Jul  4 12:20 rootCA.pem
```

- Common/simple security practice.
 - Please consider "rootCA-key.pem" as private. Never share.


WINDOWS

Same procedure as above but change the executable file!


# <M-Up>Running the server

You have node.js
- HTTP
  - bin/http-server.sh
- HTTPS
  - bin/http-server.sh secure


You have python
- HTTPS
  - bin/http-server.ph

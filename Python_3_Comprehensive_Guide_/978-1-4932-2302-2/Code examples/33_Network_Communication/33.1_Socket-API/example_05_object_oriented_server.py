#!/usr/bin/env python

import socketserver

class ChatRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        addr = self.client_address[0]
        print("[{}] Connection established".format(addr))
        while True:
            s = self.request.recv(1024)
            if s:
                print("[{}] {}".format(addr, s.decode()))
            else:
                print("[{}] Connection closed".format(addr))
                break


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("", 50000), ChatRequestHandler)
    server.serve_forever()

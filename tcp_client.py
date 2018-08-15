#!/usr/bin/python
import socket
import time
import argparse

parser = argparse.ArgumentParser(description="Simple Server for N/w Delays")
parser.add_argument('-s', '--server', type=str, required=True)
parser.add_argument('-p', '--port', type=int, default=9999)
parser.add_argument('-c', '--count', type=int, default=10)
parser.add_argument('-d', '--delay', type=int, default=5)
parser.add_argument('-b', '--buffer', type=int, default=50)
args = parser.parse_args()

ip_addr = args.server
port = args.port
count = args.count
delay = args.delay
buffer = args.buffer

srvr_addr = (ip_addr, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(srvr_addr)

for i in range(1,count):
    msg = chr(64 + i) * buffer
    print "Sending: " + msg
    sent = sock.send(msg)
    time.sleep(delay)

sock.close()


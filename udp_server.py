#!/usr/bin/python
import socket
import time
import argparse

parser = argparse.ArgumentParser(description="Simple Server for N/w Delays")
parser.add_argument('-s', '--server', type=str, default="0.0.0.0")
parser.add_argument('-p', '--port', type=int, default=9999)
parser.add_argument('-b', '--buffer',  type=int, default=20)
parser.add_argument('-d', '--delay',  type=int, default=1)
args = parser.parse_args()

ip_addr = args.server
port = args.port
buffer = args.buffer
delay = args.delay

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srvr_addr = (ip_addr, port)

sock.bind(srvr_addr)

while True:
    data, addr = sock.recvfrom(buffer)
    if data:
        print data 
	time.sleep(delay)


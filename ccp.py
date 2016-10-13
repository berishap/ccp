#!/usr/bin/env python
# -*- coding: utf-8 -*-

# One block
s1 = s.find('Device ID')
s2 = s.find('Device ID', s1+1)
t1 = s[s1:s2]

# Device ID
s1 = t1.find('Device ID: ')
s2 = t1.find('\n', s1)
device_name = t1[s1+len('Device ID: '):s2]
s1 = s2

# IP Address
s1 = t1.find('IP address: ', s1)
s2 = t1.find('\n', s1)
ip_address = t1[s1+len('IP address: '):s2]
s1 = s2

# Local Interface
s1 = t1.find('Interface: ', s1)
s2 = t1.find(',', s1)
local_int = t1[s1+len('Interface: '):s2]
s1 = s2

# Remote Interface
s1 = t1.find('Port ID (outgoing port): ', s1)
s2 = t1.find(',', s1)
local_int = t1[s1+len('Port ID (outgoing port): '):s2]
s1 = s2

class CDPNeighbor(object):
	
	def __init__(self, device_id, ip_address, local_int, remote_int):
		self.device_id = device_id
		self.ip_address = ip_address
		self.local_int = local_int
		self.remote_int = remote_int

n1 = CDPNeighbor('sw1', '20.1.2.3', 'Eth0', 'Eth5')


Port ID (outgoing port): 
def main():
	
	return 0

if __name__ == '__main__':
	main()


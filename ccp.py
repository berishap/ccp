#!/usr/bin/env python
# -*- coding: utf-8 -*-

# One block



class CDPNeighbor(object, log_file):

  def __init__(self, device_id, ip_address, local_int, remote_int):
    self.device_id = device_id
    self.ip_address = ip_address
    self.local_int = local_int
    self.remote_int = remote_int
  
  def getCDP(file_name):
    PATTERN = 'Device ID: '
    neighbors = []
    a = 0
    z = 0
    with open(file_name) as fp:
      s = ''.join(fp.readlines())
    while True:
      a = s.find(PATTERN, a)
      if a == -1:
        break
      z = s.find(PATTERN, a+1)
      neighbors.append(s[a:z])
      a = z
    return neighbors

  def getDeviceID(cdp_neighbor):
    PATTERN = 'Device ID: '
    a = 0
    z = 0
    a = cdp_neighbor.find(PATTERN, a)
    z = cdp_neighbor.find('\n', a)
    return cdp_neighbor[a+len(PATTERN):z].strip()

  def getIPAddres(cdp_neighbor):
    PATTERN = 'IP address: '
    a = 0
    z = 0
    a = cdp_neighbor.find(PATTERN, a)
    z = cdp_neighbor.find('\n', a)
    return cdp_neighbor[a+len(PATTERN):z].strip()
  
  
  def getLocalInterface(cdp_neighbor):
    PATTERN = 'Interface: '
    a = 0
    z = 0
    a = cdp_neighbor.find(PATTERN, a)
    z = cdp_neighbor.find(',', a)
    return cdp_neighbor[a+len(PATTERN):z].strip()

  def getRemoteInterface(cdp_neighbor):
    PATTERN = 'Port ID (outgoing port): '
    a = 0
    z = 0
    a = cdp_neighbor.find(PATTERN, a)
    z = cdp_neighbor.find('\n', a)
    return cdp_neighbor[a+len(PATTERN):z].strip()


n1 = CDPNeighbor('sw1', '20.1.2.3', 'Eth0', 'Eth5')
def main():

    return 0

if __name__ == '__main__':
    main()


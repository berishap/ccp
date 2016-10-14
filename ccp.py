#!/usr/bin/env python
# -*- coding: utf-8 -*-



class CDPNeighbors(object):

    def __init__(self, log_file):
        global log_output
        with open(log_file) as fp:
            log_output = ''.join(fp.readlines())

    def showCDPNeighbors(self):
        return self.getCDPNeighbors()

    def getCDPNeighbors(self):
        PATTERN = 'Device ID: '
        cdp_neighbors = []
        a = 0
        z = 0
        while True:
            a = log_output.find(PATTERN, a)
            if a == -1:
                break
            z = log_output.find(PATTERN, a + 1)
            cdp_neighbors.append(log_output[a:z])
            a = z
        return cdp_neighbors

    def __getDeviceID(self, cdp_neighbor_text):
        PATTERN = 'Device ID: '
        a = 0
        z = 0
        a = cdp_neighbor_text.find(PATTERN, a)
        z = cdp_neighbor_text.find('\n', a)
        return cdp_neighbor_text[a + len(PATTERN):z].strip()

    def getIPAddres(self, cdp_neighbor_text):
        PATTERN = 'IP address: '
        a = 0
        z = 0
        a = cdp_neighbor_text.find(PATTERN, a)
        z = cdp_neighbor_text.find('\n', a)
        return cdp_neighbor_text[a + len(PATTERN):z].strip()

    def getLocalInterface(self, cdp_neighbor_text):
        PATTERN = 'Interface: '
        a = 0
        z = 0
        a = cdp_neighbor_text.find(PATTERN, a)
        z = cdp_neighbor_text.find(',', a)
        return cdp_neighbor_text[a + len(PATTERN):z].strip()

    def getRemoteInterface(self, cdp_neighbor_text):
        PATTERN = 'Port ID (outgoing port): '
        a = 0
        z = 0
        a = cdp_neighbor_text.find(PATTERN, a)
        z = cdp_neighbor_text.find('\n', a)
        return cdp_neighbor_text[a + len(PATTERN):z].strip()



class CDPNeighbor(object):

  def __init__(self, device_id, ip_address, local_int, remote_int):
    self.device_id = device_id
    self.ip_address = ip_address
    self.local_int = local_int
    self.remote_int = remote_int



def main():

    return 0

if __name__ == '__main__':
    main()


#!/usr/bin/python
from traceback import print_tb
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import OVSController

class SingleSwitchTopo(Topo):
    # "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1')
        # Python's range(N) generates 0..N-1
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)

def simpleTest():
    "Create and test a simple network"
    topo = SingleSwitchTopo(n=4)
    net = Mininet(topo=topo, controller = OVSController)
    net.start()
    print ("=======Dumping host connections=======")
    dumpNodeConnections(net.hosts)
    print ("=======Testing network connectivity=======")
    net.pingAll()
    print("=======Stop all devices=======")
    net.stop()

topos = {"mytopo": SingleSwitchTopo}

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSKernelSwitch, RemoteController

class MyTopo(Topo):

    def build(self):
        # Add switches
        s1 = self.addSwitch('s1', cls=OVSKernelSwitch, protocols='OpenFlow13')
        s2 = self.addSwitch('s2', cls=OVSKernelSwitch, protocols='OpenFlow13')
        s3 = self.addSwitch('s3', cls=OVSKernelSwitch, protocols='OpenFlow13')

        # Add hosts
        h1 = self.addHost('h1', cpu=1.0 / 20, mac="00:00:00:00:00:01", ip="10.0.0.1/24")
        h2 = self.addHost('h2', cpu=1.0 / 20, mac="00:00:00:00:00:02", ip="10.0.0.2/24")
        h3 = self.addHost('h3', cpu=1.0 / 20, mac="00:00:00:00:00:03", ip="10.0.0.3/24")
        h4 = self.addHost('h4', cpu=1.0 / 20, mac="00:00:00:00:00:04", ip="10.0.0.4/24")

        # Add links between hosts and switches
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s3)

        # Add links between switches
        self.addLink(s1, s2)
        self.addLink(s2, s3)

def startNetwork():
    topo = MyTopo()
    c0 = RemoteController('c0', ip='192.168.29.138', port=6653)
    net = Mininet(topo=topo, link=TCLink, controller=c0)

    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    startNetwork()

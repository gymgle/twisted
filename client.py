from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor, threads


class SenzClientProtocol(DatagramProtocol):
    def startProtocol(self):
        print 'client started'
        self.transport.connect('10.2.2.132', 9999)
        self.transport.write('init senz client')

    def stopProtocol(self):
        # Called when transport is disconnected
        print 'client stopped'
        pass

    def datagramReceived(self, datagram, host):
        print 'Datagram received: ', repr(datagram)
        handler = Handler(self.transport)
        d = threads.deferToThread(handler.handleMessage, datagram)
        d.addCallback(handler.postHandle)


class Handler():
    def __init__(self, transport):
        self.transport = transport

    def handleMessage(self, datagram):
        print 'Handler Message: ', repr(datagram)
        #self.transport.write('senz')

    def postHandle(self, arg):
        print 'post handling'


def main():
    protocol = SenzClientProtocol()
    reactor.listenUDP(0, protocol)
    reactor.run()

if __name__ == '__main__':
    main()

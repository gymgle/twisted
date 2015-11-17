from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor, threads
import time


class SenzServerProtocol(DatagramProtocol):
    def __init__(self, name, host, port):
        self.name = name
        self.loopObj = None
        self.host = host
        self.port = port

    def startProtocol(self):
        # Called when transport is connected
        print 'server started'

    def stopProtocol(self):
        # Called when transport is disconnected
        print 'server stoped'
        pass

    def datagramReceived(self, data, (host, port)):
        # Called when datagram received
        print "received %r from %s:%d" % (data, host, port)
        handler = Handler(self.transport, host, port)
        d = threads.deferToThread(handler.handleMessage)
        d.addCallback(handler.postHandle)


class Handler():
    def __init__(self, transport, host, port):
        self.host = host
        self.port = port
        self.transport = transport

    def handleMessage(self):
        while True:
            self.transport.write('balll', (self.host, self.port))
            time.sleep(3)

    def postHandle(self, arg):
        print 'post handling'


def main():
    reactor.listenUDP(9999, SenzServerProtocol('server', '', 9999))
    reactor.run()

if __name__ == '__main__':
    main()

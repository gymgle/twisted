import time
from twisted.internet import reactor, protocol


class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""

    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print('date received ' + data)
        time.sleep(6)
        self.transport.write(data)


def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(8200,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()

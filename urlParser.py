class urlParser:
    def __init__(self, url):
        protocol, rest = url.split('://')
        self.protocol = protocol

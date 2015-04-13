class urlParser:
    def __init__(self, url):
        if url[0] == 'h':
            self.protocol = 'http'
        else:
            self.protocol = 'ftp'
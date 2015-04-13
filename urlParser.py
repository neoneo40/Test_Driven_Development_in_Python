class urlParser:
    def __init__(self, url):
        protocol, site_and_path = url.split('://')
        self.protocol = protocol
        self.site = site_and_path.split('/')[0]

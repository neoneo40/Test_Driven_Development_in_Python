class urlParser:
    def __init__(self, url):
        protocol, site_and_path = url.split('://')
        self.protocol = protocol
        site_and_path_list = site_and_path.split('/')
        self.site = site_and_path_list[0]
        if len(site_and_path_list) > 1:
            self.path = site_and_path_list[1]
        else:
            self.path = ''

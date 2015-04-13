class urlParser:
    def __init__(self, url):
        self.protocol, site_and_path = url.split('://')
        site_and_path_list = site_and_path.split('/')
        self.site = site_and_path_list[0]
        self.path = '/'.join(site_and_path_list[1:])
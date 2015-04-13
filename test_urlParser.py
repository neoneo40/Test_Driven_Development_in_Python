import unittest

from urlParser import urlParser


class basicProtocolParsing(unittest.TestCase):
    def assertProtocol(self, url, expected_protocol):
        purl = urlParser(url)
        self.assertEqual(purl.protocol, expected_protocol)

    def test_html_protocol(self):
        self.assertProtocol('http://www.essex.ac.uk', 'http')

    def test_ftp_protocol(self):
        self.assertProtocol('ftp://ftp.essex.ac.uk', 'ftp')

    def test_other_protocol(self):
        self.assertProtocol('w61xw://some.site.com', 'w61xw')


class basicSiteParsing(unittest.TestCase):
    def assertSite(self, url, expected_site):
        purl = urlParser(url)
        self.assertEqual(purl.site, expected_site)

    def test_site_without_path(self):
        self.assertSite('http://www.essex.ac.uk', 'www.essex.ac.uk')

    def test_site_with_simple_path(self):
        self.assertSite('http://www.essex.ac.uk/home.html', 'www.essex.ac.uk')

    def test_site_with_complex_path(self):
        self.assertSite('http://www.essex.ac.uk/csee/home.html', 'www.essex.ac.uk')
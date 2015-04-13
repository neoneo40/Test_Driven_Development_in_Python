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

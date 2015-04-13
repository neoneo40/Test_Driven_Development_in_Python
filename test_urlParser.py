import unittest

from urlParser import urlParser

class basicProtocolParsing(unittest.TestCase):
    def test_protocol(self, ):
        purl = urlParser('http://www.essex.ac.uk')
        self.assertEqual(purl.protocol, 'http')


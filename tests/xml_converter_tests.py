import unittest
from context import XMLConverter

class xml_converter_test(unittest.TestCase):
    def setUp(self):
        self.filepath = "/text_analyzer/res/test.xml"
        self.converter = XMLConverter(self.filepath)
    
    


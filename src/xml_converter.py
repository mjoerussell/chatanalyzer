import pandas as pd 
import xml.etree.cElementTree as et 

class XMLConverter:
    def __init__(self, xml_data):
        self.root = et.XML(self.open_xml(xml_data))

    def parse_root(self, root):
        return [self.parse_element(child) for child in iter(root)]
    
    def parse_element(self, element, parsed = None):
        if parsed is None:
            parsed = dict()
        
        parsed["tag"] = element.tag

        for key in element.keys():
            parsed[key] = element.attrib.get(key)

        for child in list(element):
            self.parse_element(child, parsed)
        
        return parsed
        
    def get_dataframe(self):
        structure_data = self.parse_root(self.root)
        return pd.DataFrame(structure_data, columns=["tag", "type", "body", "readable_date"])

    def open_xml(self, filepath):
        with open(filepath) as f:
            return f.read()

'''
converter = XMLConverter("text_analyzer/res/krissy_conversation.xml")
convo_dataframe = converter.get_dataframe()
print(convo_dataframe["readable_date"][0])
'''

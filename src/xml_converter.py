import pandas as pd 
import xml.etree.cElementTree as et 



class XMLConverter:

    timestamp = "readable_date"
    text = "body"
    sender = "type"
    message_type = "tag"

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

        parsed["children"] = [self.parse_element(child) for child in iter(list(element))]
        
        return parsed
        
    def get_dataframe(self, columns = None):
        structure_data = self.parse_root(self.root)
        if columns is not None:
            return pd.DataFrame(structure_data, columns=columns)
        else:
            return pd.DataFrame(structure_data)

    def open_xml(self, filepath):
        with open(filepath) as f:
            return f.read()


# converter = XMLConverter("text_analyzer/res/krissy_conversation.xml")
# convo_dataframe = converter.get_dataframe(["tag", "type", "body", "readable_date"])
# print(convo_dataframe[0:10])

# test_converter = XMLConverter("text_analyzer/res/test.xml")
# print(test_converter.get_dataframe())


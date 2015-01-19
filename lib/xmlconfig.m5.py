\_{*}+=
from xml.etree import ElementTree

class config(object):
    config_items = {}

    def __init__(self,xmlconfigfile):
        config_file = open(xmlconfigfile).read()
        self.add_items(config_file)

    def add_items(self,reader):
        root = ElementTree.fromstring(reader)
        for node in root.findall('item'):
            self.convert_to_dict(node)

    def convert_to_dict(self,node):
        if node.attrib.has_key("key") > 0 and node.attrib.has_key("value") > 0:
            self.config_items[node.attrib['key']] = node.attrib['value']

    def get_items(self):
        return self.config_items
@>

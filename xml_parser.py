import json
import xml.etree.ElementTree as ET
import xml.dom.minidom

def convert_json_to_xml(json_data):
    root = ET.Element("youtubeApiData")
    for key, value in json_data.items():
        if key == "items":
            items = ET.SubElement(root, "items")
            for item in value:
                item_elem = ET.SubElement(items, "item")
                for sub_key, sub_value in item.items():
                    if sub_key == "snippet":
                        snippet = ET.SubElement(item_elem, "snippet")
                        for sub_sub_key, sub_sub_value in sub_value.items():
                            ET.SubElement(snippet, sub_sub_key).text = str(sub_sub_value)
                    else:
                        ET.SubElement(item_elem, sub_key).text = str(sub_value)
        else:
            ET.SubElement(root, key).text = str(value)
    
    return root


# Read JSON data from file
with open("json_data.json", "r") as json_file:
    json_data = json.load(json_file)

# Convert JSON to XML
xml_tree = convert_json_to_xml(json_data)
xml_string = ET.tostring(xml_tree, encoding="unicode", method="xml")

# Format XML for readability
xml_dom = xml.dom.minidom.parseString(xml_string)
formatted_xml = xml_dom.toprettyxml(indent="    ")

# Store formatted XML data into a file
with open("youtube_data.xml", "w") as xml_file:
    xml_file.write(formatted_xml)

print("XML data has been stored in youtube_data.xml")

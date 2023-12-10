#
# Generate a valid xml file at /tmp/vulnerable-countries.xml.
# It should contain a list of country nodes attached to a root node.
# Each country node should have a name attribute.
# The third node name should be Panama.
#
import xml.etree.ElementTree as ET

def generate_xml():
    # Create the root element
    root = ET.Element("countries")

    # List of countries
    countries = ["USA", "Canada", "Panama", "Germany", "Japan"]

    # Create country nodes and add them to the root
    for country_name in countries:
        country_node = ET.SubElement(root, "country")
        country_node.set("name", country_name)

    # Create the ElementTree object
    tree = ET.ElementTree(root)

    # Save the XML file to /tmp/vulnerable-countries.xml
    file_path = "/tmp/vulnerable-countries.xml"
    tree.write(file_path)

    print(f"XML file generated at: {file_path}")

if __name__ == "__main__":
    generate_xml()

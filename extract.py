import xml.etree.ElementTree as ET

tree = ET.parse('ECFR-title47.xml')
root = tree.getroot()

print(root.tag)
for child in root:
    print(child.tag, child.attrib)
print(root[0][0][0][0].text)

file1 = open("test.txt", "w")
for h in root.iter('HEAD'):
        file1.write(h.text)
file1.close
import xml.etree.ElementTree as ET 
tree = ET.parse('Task1.xml')
root = tree.getroot()
arr = []
for x in root.iter():
    if x.text is None:
        pass
    else:
        arr.append(x.text.split("|"))


print(arr)
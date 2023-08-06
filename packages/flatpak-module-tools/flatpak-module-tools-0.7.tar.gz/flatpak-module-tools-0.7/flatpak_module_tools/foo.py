import os, sys
import xml.etree.ElementTree as ET

root = ET.parse(os.path.join(sys.argv[1], 'repodata', 'repomd.xml'))

ns = {'repo': 'http://linux.duke.edu/metadata/repo'}
print root.find("./repo:data[@type='modules']/repo:location", ns)


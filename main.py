import pprint
import xml.etree.ElementTree as ET


# 1st step: importing data from xml file_________________________________________

tree = ET.parse('post.xml')
root = tree.getroot()


def etree_to_dict(tree):
    posts = []
    for i in range(len(tree)):
        posts.append(tree[i].attrib)
    return posts


posts = etree_to_dict(root)

# 2nd step: Adding RFM variables _________________________________________

# 2.1 Recency

posts = sorted(posts, key = lambda i: i['CreationDate'])

number_Of_Segments = 5
number_Of_Items_In_Segments = int(len(posts)/5)

global list_Counter
list_Counter=0

for i in range(number_Of_Segments):
    for j in range(number_Of_Items_In_Segments):
        posts[list_Counter]['Recency'] = i+1
        list_Counter+=1


# 2.2 Frequency


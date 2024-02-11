import xml.etree.ElementTree as et 
import re
import sys
import pandas 
import pandas as pd 
import json
from pandas import json_normalize
import os, sys


xtree = et.parse('IRTSystemX.net.xml')
root = xtree.getroot()

df_cols = ["idjunc", "typejunc", "xjunc", "yjunc", "incLanes", "intLanes"]
rows = []

for element in root.iter(tag='junction'):
    
    idjunc = element.attrib['id']
        
    typejunc = element.attrib['type']
    posx = element.attrib['x']
    posy = element.attrib['y']
    inclanejunc = element.attrib['incLanes']
    inclanejunc = list(inclanejunc.split())
    intlanejunc = element.attrib['intLanes']
    intlanejunc = list(intlanejunc.split())
    rows.append({"idjunc": idjunc, "typejunc": typejunc, "xjunc":posx , "yjunc":posy,
                 "incLanes": inclanejunc, "intLanes": intlanejunc})
    junction_df = pd.DataFrame(rows, columns = df_cols)

    intersections_df = pd.DataFrame(rows, columns=df_cols)

    #juncID = junction.text
        #print (juncID, end=' ')
        #for junction in element.iter():
            #junctionID = junction.text
            #if (junction.tag=='junction'):
                #print (junction.text)
print (junction_df)
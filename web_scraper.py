import urllib.request
import pandas as pd
import os


df = pd.read_csv('mecsj_volumeOne.csv')

directory_name = "arabic_papers"


idx = 403
for link in df['pdf_link-href']:
    
    response = urllib.request.urlopen(link)    
    filename = os.path.join(directory_name, f'file_{idx}.pdf')
    with open(filename, 'wb') as file:
        file.write(response.read())
    idx += 1


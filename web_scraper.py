import urllib.request
import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
import os
import time

df = pd.read_csv('qsience.csv')

directory_name = "arabic_papers_qs"



for idx, link in enumerate(df['pdf_link-href']):
    
    response = urllib.request.urlopen(link)    
    filename = os.path.join(directory_name, f'qsciencefile_{idx}.pdf')
    with open(filename, 'wb') as file:
        file.write(response.read())

    
    
    
    
    


# import urllib.request
# import os
# import requests
# from bs4 import BeautifulSoup
# import time

# def download_pdfs(search_query, base_url, search_url, download_folder):
#     if not os.path.exists(download_folder):
#         os.makedirs(download_folder)

#     for start in range(0, 991, 10):
#         search_payload = {'start': start, 'q': search_query, 'hl': 'en', 'as_sdt': '0,5'}
#         try:
#             search_response = requests.get(search_url, params=search_payload)
#             if search_response.status_code != 200:
#                 print(f"Failed to get search results: {search_response.status_code}")
#                 continue

#             soup = BeautifulSoup(search_response.text, 'html.parser')
            
#             pdf_urls = []
#             for link in soup.find_all('a'):
#                 url = link.get('href')
#                 if url and 'pdf' in url:
#                     pdf_urls.append(url if url.startswith('http') else base_url + url)

#             for link in pdf_urls:
#                 try:
#                     original_filename = os.path.basename(link)
#                     print(f"Attempting to download {original_filename}...")
                    
#                     response = urllib.request.urlopen(link)
#                     filename = os.path.join(download_folder, original_filename)
#                     with open(filename, 'wb') as file:
#                         file.write(response.read())
                    
#                     print(f"Successfully downloaded {original_filename}")
#                 except Exception as e:
#                     print(f"Failed to download {link}: {e}")
#         except Exception as e:
#             print(f"Failed to search: {e}")

#         time.sleep(10000)


# # Usage
# base_url = 'https://scholar.google.com/'  # Replace with the actual base URL
# search_url = 'https://scholar.google.com/scholar'  # Modify this to the correct search URL
# download_folder = 'downloaded_pdfs'  # Folder where PDFs will be saved

# search_query = 'الادب'  # Replace with the actual search term

# download_pdfs(search_query, base_url, search_url, download_folder)



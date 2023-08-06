import requests
from bs4 import BeautifulSoup
import re
from cs200.core import BASE_SEARCH_URL, BASE_DELIMITER

# This is a function to properly create a url for searching wikipedia pages.
def build_url(url):
        
        final_url = ""
        
        spaces = re.split(" ", url)
        # Iterate over the spaces list but exclude the last item. 
        for item in range(len(spaces)-1):
                
                # Add an underscore between spaces in the search query
                final_url += spaces[item] + BASE_DELIMITER
                
        # To avoid adding an extra underscore after the final search term in the
        # url, we only add the last item of the spaces list to the final_url 
        # variable after breaking out of the loop.
        final_url += spaces[-1]
        
        return BASE_SEARCH_URL + final_url


def get_url(url):
        
        url = build_url(url)

        print(url)

        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
                }
        
        req = requests.get(url, headers=headers)

        resp = req.text

        soup = BeautifulSoup(resp, features="html5lib")
        
        return soup.getText()

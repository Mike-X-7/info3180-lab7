import requests
from bs4 import BeautifulSoup
import urlparse

def getImages():
    url = "http://www.amazon.com/gp/product/1783551623"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    
    images = []
    og_image = (soup.find('meta', property='og:image') or
                        soup.find('meta', attrs={'name': 'og:image'}))
    if og_image and og_image['content']:
        images.append(og_image['content'])

    thumbnail_spec = soup.find('link', rel='image_src')
    if thumbnail_spec and thumbnail_spec['href']:
        images.append(thumbnail_spec['href'])

    
    for img in soup.findAll("img", src=True):
        images.append(img["src"])
     
    # remove # below and prints the list of images if necessary.  
    #print images
    
    #Returns images
    return images
    

getImages()    
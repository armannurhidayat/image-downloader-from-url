import pandas as pd
import requests

filename = 'images_url.csv'
path_image = 'images/'

links = pd.read_csv(filename)
for i, url in enumerate(links.values):
    r = requests.get(url[0])
    with open(f'{path_image}/image-{i}.jpg', 'wb') as f:
        f.write(r.content)
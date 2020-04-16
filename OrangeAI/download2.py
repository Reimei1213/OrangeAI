from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

#APIkey
key = '092d1719313dd5579c7e156205fdd2d9'
secret = '20c9835c4e030e5c'
wait_time = 1

#SaveFolder
image_name = sys.argv[1]
savedir = './Image/NoOrange'

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = image_name,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

photos = result['photos']
#pprint(photos)

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath):
        continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)

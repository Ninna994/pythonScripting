# Find how many photos havel duplicate url values from https://jsonplaceholder.typicode.com/photos
import requests
url = 'https://jsonplaceholder.typicode.com/photos'

# get data about the photos
response = requests.get(url)

# read that data into a variable
photosJson = response.json()

# make a empty list that will contain all urls
url_list = []

for photo in photosJson:
# add all urls to list
  url_list.append(photo['url'])

# print length of the list
print('Full list length: ',len(url_list))

# delete duplicated
print('Unique URLs in list: ',len(set(url_list)))
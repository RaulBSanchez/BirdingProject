import requests 
import json 
import pprint


# url and header
url = 'https://api.ebird.org/v2/data/obs/US-PA-101/recent'
headers = {'X-eBirdApiToken': }


# request for the information 
request = requests.get(url, headers = headers)

#variable to hold information
request_list = request.json()

print('print the reuqests')

# pprint.pprint(request_list)



#create new dictionary to convert lists of dictionraries from json to 

bird_dict = {item['comName']:item for item in request_list}



pprint.pprint(bird_dict)


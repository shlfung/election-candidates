import json
import urllib.request
import sys
import csv

	

if __name__ == "__main__":
	
    BASE_URL = "https://represent.opennorth.ca"
        
    full_url = BASE_URL + "/candidates/house-of-commons/" + "?limit=1000&offset=0"
	
    response = urllib.request.urlopen(full_url)
	
    json_object = json.loads(response.read().decode('utf8'))
    print(json_object['meta'])
    list_of_candidates = json_object['objects']

    BASE_URL = "https://represent.opennorth.ca"
        
    full_url = BASE_URL + "/candidates/house-of-commons/" + "?limit=1000&offset=1000"
	
    response = urllib.request.urlopen(full_url)
	
    json_object = json.loads(response.read().decode('utf8'))
    print(json_object['meta'])

    list_of_candidates.extend(json_object['objects'])


    f = open('candidates.csv', 'wt', newline='')
    counter = 0
    try:
        writer = csv.writer(f)
        writer.writerow(('Name', 'Party', 'District', 'Email'))
        for candidate in list_of_candidates:
            writer.writerow((candidate['name'], candidate['party_name'], candidate['district_name'], candidate['email']))
            counter = counter + 1
    finally:
        f.close()

    print(counter)

    


	

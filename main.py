import json
import urllib.request
import sys
import csv

	

if __name__ == "__main__":

    district_dic = {}

    reader = csv.reader(open('NHS2013.csv'))

    for row in reader:
        if row[1] not in district_dic:
            district_dic[row[1]] = row[0]    


    print(district_dic)
    print(len(district_dic))
	
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

    '—'
    

    f = open('candidates.csv', 'wt', newline='')
    counter = 0
    try:
        writer = csv.writer(f)
        writer.writerow(('Name', 'Party', 'District', 'Province', 'Email'))
        for candidate in list_of_candidates:
            try:
                district_key = candidate['district_name'].replace('—', '--')
                province = district_dic[district_key]
            except KeyError:
                province = ''
            writer.writerow((candidate['name'], candidate['party_name'], candidate['district_name'], province, candidate['email']))
            counter = counter + 1
    finally:
        f.close()

    print(counter)

    


	

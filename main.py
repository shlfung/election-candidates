import json
import urllib.request

BASE_URL="https://represent.opennorth.ca"


	

if __name__ == "__main__":
	
	BASE_URL = "https://represent.opennorth.ca"
	full_url = BASE_URL + "/candidates/house-of-commons/"
	response = urllib.request.urlopen(full_url)
	
	json_object = json.loads(response.read().decode('utf8'))
	
	print(json_object)

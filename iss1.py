#for finding the current Latitude and Longitude of The Space Station

import urllib.request, urllib.parse, urllib.error
import json

base_url = "http://api.open-notify.org/iss-now.json";
n = 10;
list1 = [];

for i in range(n):
	connection = urllib.request.urlopen(base_url);
	data = connection.read().decode();
	data = json.loads(data);
	list1.append(data);

print(list1[0]);

for i in list1:
	print(i["iss_position"]["longitude"]);
	print(i["iss_position"]["latitude"]);
	print("\n");

import urllib.request, urllib.parse, urllib.error
import json

base_url = "http://api.open-notify.org/iss-pass.json";

lat  = input("enter latitude");
log = input("enter longitude");

params = {"lat" : lat, "lon" : log};

query_string = urllib.parse.urlencode(params);
url = base_url + "?" + query_string;

connection = urllib.request.urlopen(url);
data = connection.read().decode();

print(data);

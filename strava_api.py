import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': "86521",
    'client_secret': 'a6778e8cc680cd6b7094c87a85ab1dfc69e80604',
    'refresh_token': '72f9e696ea3e96237ad452093aa9aa07e79fb9e3',
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n") 
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}

request_page_num = 1
all_activities = []

while True:
    param = {'per_page': 200, 'page': request_page_num}
    my_dataset = requests.get(activites_url, headers=header, params=param).json()
    if len(my_dataset) == 0:
        print("breaking")
        break
    
    if all_activities:
        print("pievieno")
        all_activities.extend(my_dataset)
    else:
        print("jauns")
        all_activities = my_dataset
    
    request_page_num += 1
print(len(all_activities))
attalums = 0
for k in all_activities:
    if k["type"] == "Run":
        attalums += 1
print(attalums)
# print(len(my_dataset))
# for dataset in my_dataset:
#     print(dataset["name"])
# #  sito liek pie ta dataset ja vajag kartes enryptionu, pectam google polyline encryption var atsifret

import csv
import json
import requests
from requests.auth import HTTPBasicAuth

url = 'https://rest.iad-06.braze.com/users/export/ids'
API_KEY = 'Bearer 2c324fa9-7629-4b0a-9527-7ac6e8b1e0d5'
headers = {
    'Content-Type': 'application/json',
    'Authorization': API_KEY
}

alldata = []
with open('batch_test_9_result.csv', 'w') as file:
    # str1 = ""
    with open('batch_test_9.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if len(row)==0:
               continue
            temp = row[0].split(",")
            if temp[0]=="external_id":
                continue
            body = json.dumps({"email_address": temp[0]
                             })
            response = requests.post(url, data=body, headers=headers)
            a = response.json()
            all = []

            if len(a['users']) == 0:
                continue
            if len(a['users']) != 0:
                all.append([a['users'][0]['email']])
            for x in a['users']:
                all.append([x['external_id']])
            if 'custom_attributes' in a['users'][0]:
                if 'app_current_series_name' in a['users'][0]['custom_attributes']:
                    all.append([a['users'][0]['custom_attributes']['app_current_series_name']])
                else:
                    all.append('')
            if 'custom_attributes' in a['users'][0]:
                if 'app_subscription_platform' in a['users'][0]['custom_attributes']:
                    all.append([a['users'][0]['custom_attributes']['app_subscription_platform']])
                else:
                    all.append('')
            if 'custom_attributes' in a['users'][0]:
                if 'app_workouts_completed_count' in a['users'][0]['custom_attributes']:
                    all.append([a['users'][0]['custom_attributes']['app_workouts_completed_count']])
                else:
                    all.append('')
            if 'custom_attributes' in a['users'][0]:
                if 'clicked_past_365d' in a['users'][0]['custom_attributes']:
                    all.append([a['users'][0]['custom_attributes']['clicked_past_365d']])
                else:
                    all.append('')
            # if 'custom_attributes' in a['users'][0]:
            #     if 'subscription_interval' in a['users'][0]['custom_attributes']:
            #         all.append([a['users'][0]['custom_attributes']['subscription_interval']])
            #     else:
            #         all.append('')
            # if 'custom_attributes' in a['users'][0]:
            #     if 'total_videos_watched' in a['users'][0]['custom_attributes']:
            #         all.append([a['users'][0]['custom_attributes']['total_videos_watched']])
            #     else:
            #         all.append('')
            # if 'custom_attributes' in a['users'][0]:
            #     if 'user_created_date' in a['users'][0]['custom_attributes']:
            #         all.append([a['users'][0]['custom_attributes']['user_created_date']])
            #     else:
            #         all.append('')
            alldata.append(all)
            print(all)

with open("batch_test_9_result.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    for x in alldata:
        writer.writerow(x)
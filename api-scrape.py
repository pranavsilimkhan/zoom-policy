import requests
import os
import json


current_page = 1
pdf_policies = []
page_size = 30
categories = ["analytics", "business-system-integrator", "crm", "carrier-provider-exchange", "team-collaborations", "customer-service", "eCommerce", "education", "eventmanagement", "financialServices", "games"]
bad_request = []

for category in categories:
    os.makedirs(f"data/{category}", exist_ok=True)
    while True:
        all_apps = f"https://marketplace.zoom.us/api/v1/apps/filter?pageNum={current_page}&pageSize=30&category=analytics"
        response = requests.get(all_apps)
        json_response = response.json()
        print(f"{current_page} - {category}")

        for app in json_response['apps']:
            app_id = app['id']
            app_name = app['name']
            app_details_url = f"https://marketplace.zoom.us/api/v1/marketplace/apps/{app_id}"

            app_details = requests.get(app_details_url)
            app_details = app_details.json()
            privacy_url = app_details['privacyUrl']

            if ".pdf" in privacy_url:
                pdf_policies.append({'app_name': app_name, 
                                        'privacy_url': privacy_url})
            else:
                try:
                    policy = requests.get(privacy_url)
                    if policy.status_code == 404:
                        raise Exception()
                    with open(f"./data/{category}/{app_name}.html", "wb") as file:
                        file.write(policy.content)
                except:
                    bad_request.append({'app_name': app_name, 
                                        'privacy_url': privacy_url})
        if current_page*page_size >= json_response["total"]:
            break

        current_page += 1

    with open(f"./data/pdf_plocies_{category}.json", "w") as file:
        json.dump(pdf_policies, file)

    with open(f"./data/bad_request_{category}.json", "w") as file:
        json.dump(bad_request, file)
    break

print("Successful")



"""
This file contains the functions to generate and send the alert to Microsoft Teams
"""

import json
import requests
import os

billingDashboardUrl = os.environ.get('billingDashboardUrl')

def generate_alert(template_path, projects, services):
    global billingDashboardUrl
    
    with open(template_path, "r") as read_file:
        template = json.load(read_file)

    projects = ', '.join(projects)
    services = ', '.join(services)

    template["body"][2]["rows"][1]["cells"][0]["items"][0]["text"] = projects
    template["body"][2]["rows"][1]["cells"][1]["items"][0]["text"] = services
    
    template["body"][3]["actions"][0]["url"] = billingDashboardUrl

    return template

def send_alert(teams_alert):
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(os.environ.get('webhookURL'), headers=headers, json=teams_alert)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    
    print("Teams alert successfully sent")
    
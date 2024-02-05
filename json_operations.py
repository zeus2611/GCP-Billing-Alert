"""
This file contains the functions to generate and send the alert to Microsoft Teams
"""

import os
import json
import requests

def generate_alert(template_path, projects, services):
    """
    This function receives the path of the template file and the data to be inserted in the alert.
    """
    billing_dashboard_url = os.environ.get('billingDashboardUrl')
    with open(template_path, "r", encoding="utf-8") as read_file:
        template = json.load(read_file)

    projects = ', '.join(projects["project"])
    services = ', '.join(services["service"])

    template["body"][2]["rows"][1]["cells"][0]["items"][0]["text"] = projects
    template["body"][2]["rows"][1]["cells"][1]["items"][0]["text"] = services
    template["body"][3]["actions"][0]["url"] = billing_dashboard_url

    return template

def send_alert(teams_alert):
    """
    This function receives the alert and sends it to Microsoft Teams.
    """
    headers = {"Content-Type": "application/json"}
    webhook_url = os.environ.get('webhookURL')

    try:
        response = requests.post(webhook_url, headers=headers, json=teams_alert, timeout=5)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err) from err
    print("Teams alert successfully sent")

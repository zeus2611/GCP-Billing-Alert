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
    billing_dashboard_url = os.environ.get('BILLING_DASHBOARD_URL')
    with open(template_path, "r", encoding="utf-8") as read_file:
        template = json.load(read_file)

    projects = ', '.join(projects["project"])
    services = ', '.join(services["service"])

    condition_name = "GCP Budget Alert"
    summary = "The costs of the following projects and services are higher than expected."

    template["summary"] = condition_name
    template["sections"][0]["activityTitle"] = condition_name
    template["sections"][0]["activitySubtitle"] = summary
    template["sections"][0]["facts"][0]["value"] = projects
    template["sections"][0]["facts"][1]["value"] = services
    template["potentialAction"][0]["targets"][0]["uri"] = billing_dashboard_url

    return template

def send_alert(teams_alert):
    """
    This function receives the alert and sends it to Microsoft Teams.
    """
    headers = {"Content-Type": "application/json"}
    # webhook_url = os.environ.get('WEBHOOK_URL')

    webhook_url = "https://whizlabsindia.webhook.office.com/webhookb2/14b2cc4e-2537-4ecc-a251-b2a43cb5953a@a34de549-3862-4aa2-94c8-7dfd72abb0a8/IncomingWebhook/992d4871d3a84a4aaccea22c32e6186f/c6a9b98f-9db4-4ef2-b206-29980d5c7dac"

    try:
        response = requests.post(webhook_url, headers=headers, json=teams_alert, timeout=5)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err) from err
    print("Teams alert successfully sent")

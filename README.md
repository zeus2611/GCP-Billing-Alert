# GCP Automated Billing Alert System
## Overview
The Automated Billing Alert System is a Python application designed to monitor billing data from Google Cloud Platform (GCP) using BigQuery, identify projects and services exceeding a specified cost threshold, and send alerts to Microsoft Teams via webhooks. This system provides real-time billing alerts to ensure efficient cost management and budget adherence.

## Features
* Queries billing data from Google Cloud's BigQuery.
* Identifies projects and services with costs exceeding a predefined threshold.
* Generates alerts in JSON format using customizable templates.
* Sends alerts to Microsoft Teams channels via webhook integration.
* Automated deployment and invocation using GitHub Actions.
* Scheduled alert generation and delivery at specified intervals.

## Architecture
The system consists of the following components:

1. **Main Script (main.py):** Executes the core functionality of the system. It queries billing data, processes it, generates alerts, and sends them to Microsoft Teams.
2. **JSON Operations (json_operations.py):** Contains functions to manipulate JSON templates and send alerts to Microsoft Teams.
3. **Template (template.json):** Defines the structure and content of the alert message in JSON format.
4. **Environment Variables:** Utilized for sensitive data such as webhook URLs and billing dashboard URLs.
5. **Google Cloud Platform:** Billing data is stored in BigQuery, which is queried by the system to fetch billing information.
6. **Microsoft Teams:** Alerts are sent to designated channels using incoming webhooks.

## Usage
1. Setup:
    * Ensure Python 3.10 is installed.
    * Install required dependencies: google-cloud-bigquery, requests.
    * Set up environment variables for webhook URLs and other sensitive data.
2. Configuration:
    * Customize the SQL queries in main.py to match specific billing requirements.
    * Modify the JSON template (template.json) to adjust the format and content of the alerts.
3. Deployment:
    * Deploy the project on a cloud platform (e.g., Google Cloud Functions) for automated execution.
    * Configure GitHub Actions for automated testing, deployment, and invocation at specified intervals.
4. Monitoring:
    * Monitor execution logs for any errors or anomalies.
    * Set up monitoring tools for tracking system health and performance.
4. Maintenance:
    * Regularly review and update SQL queries, JSON templates, and other configurations as needed.
    * Perform routine maintenance tasks such as dependency updates, security patches, etc.

## Future Enhancements
* Integration with additional cloud providers for multi-cloud billing monitoring.
* Implementation of advanced analytics and visualization features for deeper cost analysis.
* Support for custom alert thresholds based on user-defined criteria.
* Enhancement of error handling and logging mechanisms for improved reliability.

## License
This project is licensed under the MIT License. More details can be found in [LICENSE](./LICENSE)

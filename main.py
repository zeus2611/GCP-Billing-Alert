"""
This is the main file of the project. It is responsible for the execution of the project. It uses the BigQuery client to perform a query and get the data. Then, it uses the json_operations.py file to generate the alert and send it to Microsoft Teams.
"""

from google.cloud import bigquery
import json_operations as json_op

client = bigquery.Client()

# Perform a query.
QUERY_FOR_PROJECT = """
    SELECT project.id as project, ROUND(SUM(cost_at_list), 2) as costs FROM `whizlabs-billing.billing_dataset.gcp_billing_export_resource_v1_0156CB_EB84C5_448E52`
    WHERE export_time >= TIMESTAMP(DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
    GROUP BY project
    HAVING costs > 100 AND project != 'whizlabs-development'
    ORDER BY costs DESC
"""

QUERY_FOR_SERVICE = """
    SELECT service.description as service, ROUND(SUM(cost_at_list), 2) as costs FROM `whizlabs-billing.billing_dataset.gcp_billing_export_resource_v1_0156CB_EB84C5_448E52`
    WHERE export_time >= TIMESTAMP(DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
    GROUP BY service
    HAVING costs > 100
    ORDER BY costs DESC
"""

higherCostProject = client.query_and_wait(QUERY_FOR_PROJECT).to_dataframe()
higherCostService = client.query_and_wait(QUERY_FOR_SERVICE).to_dataframe()

template_path = "template.json"
# teams_alert = json_op.generate_alert(template_path, higherCostProject["project"], higherCostService["service"])

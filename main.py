from google.cloud import bigquery

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

print(higherCostProject)
print(higherCostService)
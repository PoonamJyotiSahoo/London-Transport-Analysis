import os
from google.cloud import bigquery
import pandas as pd
import matplotlib.pyplot as plt


# Construct a BigQuery client object.


from google.oauth2 import service_account

# Replace the path with your exact file path.
credentials_path = "D:\\Projects\\London-Transport-Analysis\\london-transport-analysis-fc168a33db6d.json"
credentials = service_account.Credentials.from_service_account_file(credentials_path)
client = bigquery.Client(credentials=credentials)

# Define your SQL query
query = """
SELECT
  start_station_name,
  COUNT(rental_id) AS total_trips
FROM
  bigquery-public-data.london_bicycles.cycle_hire
GROUP BY
  start_station_name
ORDER BY
  total_trips DESC
LIMIT 10
"""

# Run the query
query_job = client.query(query)
results = query_job.result()

# Convert results to a pandas DataFrame for analysis and plotting
df = results.to_dataframe()

# Plot the data
df.plot(kind='bar', x='start_station_name', y='total_trips', legend=None)
plt.title('Top 10 Busiest London Bicycle Stations')
plt.xlabel('Station Name')
plt.ylabel('Number of Trips')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

print(df)
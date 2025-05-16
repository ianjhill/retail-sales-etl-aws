# retail-sales-etl-aws

Retail Sales ETL Pipeline (AWS Project)
A cloud-based data engineering project that simulates daily retail sales processing using AWS.

Tools Used

AWS S3 – for raw and cleaned data lake storage
AWS Glue – for PySpark-based ETL pipeline
AWS Athena – for serverless querying
AWS QuickSight – for dashboard visualization
Python & Faker – for generating mock retail data

ETL Pipeline Flow

Raw Data uploaded to s3://retail-sales-data-ian/raw/
Glue Crawler registered raw CSVs as a table in the Glue Catalog
Glue Job transformed the data with PySpark (added total_price, cleaned date)
Transformed Data saved as Parquet to s3://retail-sales-data-ian/cleaned/
Crawler registered cleaned data table
Athena Queries calculated KPIs: revenue, units sold, top products
QuickSight Dashboard visualized sales trends and departmental insights

Sample Insights from Athena
SELECT product_name, SUM(total_price) AS total_revenue
FROM cleaned_cleaned
GROUP BY product_name
ORDER BY total_revenue DESC
LIMIT 5;
<img width="1273" alt="Screenshot 2025-05-16 at 1 38 11 PM" src="https://github.com/user-attachments/assets/2b58785c-dd59-45c9-aa5e-b972425101d7" />

📷 QuickSight Dashboard
<img width="628" alt="Screenshot 2025-05-16 at 1 38 34 PM" src="https://github.com/user-attachments/assets/67707cdf-e6b0-45d1-b845-af8056f19b82" />

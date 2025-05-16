import sys
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, round as round_col

# Boilerplate
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read from the raw table
raw_df = glueContext.create_dynamic_frame.from_catalog(
    database="retail_sales_db",
    table_name="raw"
)

# Convert to DataFrame to apply transformations
df = raw_df.toDF()

# Add total_price column
df = df.withColumn("total_price", round_col(col("quantity_sold") * col("unit_price"), 2))

# Optional: ensure date column is cast correctly (just in case)
df = df.withColumn("date", col("date").cast("date"))

# Convert back to DynamicFrame
transformed_dyf = DynamicFrame.fromDF(df, glueContext, "transformed_dyf")

# Write cleaned data to new S3 location
glueContext.write_dynamic_frame.from_options(
    frame=transformed_dyf,
    connection_type="s3",
    connection_options={"path": "s3://retail-sales-data-ian/cleaned/"},
    format="parquet"
)

job.commit()

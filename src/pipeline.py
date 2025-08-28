from etl import pipeline_calculate_sales_kpi

database_path = "../data"
file_format = "parquet"  # Choose between csv and parquet formats to save your data

pipeline_calculate_sales_kpi(database_path, file_format)

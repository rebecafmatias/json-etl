from pathlib import Path

from src.utils.etl import pipeline_calculate_sales_kpi

path_dir = Path(__file__).resolve().parent.parent

database_path = path_dir / "data"
file_format = "parquet"  # Choose between csv and parquet formats to save your data

pipeline_calculate_sales_kpi(database_path, file_format)

import glob
import os

import pandas as pd

from .log import log_decorator

"""Creating a func to find json files and read them:"""


@log_decorator
def read_json_files(directory_path: str) -> pd.DataFrame:

    json_files = glob.glob(os.path.join(directory_path, "*.json"))
    if not json_files:
        print(f'JSON file path "{directory_path}" not found.')
    else:
        dfs = []
        for file in json_files:
            sales_df = pd.read_json(file)
            dfs.append(sales_df)
        return pd.concat(dfs, ignore_index=True)


"""Creating a func to calculate a dataframe total sales
value using unit price and quantity sold:"""


@log_decorator
def calculate_sales(df_to_calculate_total_sales: pd.DataFrame) -> pd.DataFrame:
    df_to_calculate_total_sales["total_sale"] = (
        df_to_calculate_total_sales["Quantidade"] * df_to_calculate_total_sales["Venda"]
    )
    return df_to_calculate_total_sales


"""Creating a func to save a dataframe as a csv or a parquet file:"""


@log_decorator
def save_df_as_parquet(df_to_save: pd.DataFrame, path_to_save: str, file_type: str):
    if file_type == "parquet":
        df_to_save.to_parquet(path=path_to_save + ".parquet", index=False)
    elif file_type == "csv":
        df_to_save.to_csv(path_to_save + ".csv", index=False)
    else:
        print("File type not found. It must be parquet or csv.")


"""Function to call everything"""


@log_decorator
def pipeline_calculate_sales_kpi(database_path: str, file_format: str):
    test_read_json_df = read_json_files(database_path)
    total_sales_df = calculate_sales(test_read_json_df)
    save_df_as_parquet(total_sales_df, str(database_path) + "/sales_data", file_format)

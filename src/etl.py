import glob
import os

import pandas as pd

"""Creating a func to find json files and read them:"""


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


def calculate_sales(
    df_to_calculate_total_sales: pd.DataFrame, qty_column: int, price_column: int
) -> pd.DataFrame:
    df_to_calculate_total_sales["total_sale"] = (
        df_to_calculate_total_sales[qty_column]
        * df_to_calculate_total_sales[price_column]
    )
    return df_to_calculate_total_sales


"""Creating a func to save a dataframe as a csv or a parquet file:"""


def save_df_as_parquet(df_to_save: pd.DataFrame, path_to_save: str, file_type: str):
    if file_type == "parquet":
        df_to_save.to_parquet(path=path_to_save + ".parquet", index=False)
    elif file_type == "csv":
        df_to_save.to_csv(path_to_save + ".csv", index=False)
    else:
        print("File type not found. It must be parquet or csv.")


if __name__ == "__main__":
    database_path = "../data"
    path_to_save = "../data/sales_data"
    file_type = "csv"
    qty_column = "Quantidade"
    unit_price = "Venda"
    test_read_json_df = read_json_files(database_path)
    total_sales_df = calculate_sales(test_read_json_df, qty_column, unit_price)
    save_df_as_parquet(total_sales_df, path_to_save, file_type)

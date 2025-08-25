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

"""Creating a func to save a dataframe as a csv or a parquet file:"""

if __name__ == "__main__":
    test_read_json = read_json_files("../data")

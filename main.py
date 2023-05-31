import io
import sys

import pandas as pd
import requests

DATA_DIR = "./data/"

def cache_gsheet(url, name, check_function):
    content = requests.get(url).content

    df = pd.read_csv(io.StringIO(content.decode('utf-8')))

    if check_function:

        data_passed_check = check_function(df)
        if data_passed_check:
            df.to_csv(DATA_DIR + name)
        else:
            print(f"File {name} did not pass the check.", sys.stderr)
            sys.exit(1)

    else:
        df.to_csv(DATA_DIR + name)

    df.to_csv(DATA_DIR + name)


def main():

    cache_gsheet(
        url="https://docs.google.com/spreadsheets/d/18dMo5d89HkyzFGnsQaCPw843LPUG-czAneBR7rVThHI/export?format=csv",
        name="htcss_user_registry.csv",
        check_function=htcss_user_registry_check
    )


def htcss_user_registry_check(df: pd.DataFrame):
    return not any(df['Latitude'].isna()) and not any(df['Longitude'].isna())


if __name__ == "__main__":
    main()

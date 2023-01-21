# Extract Data

from typing import List
from datetime import date, timedelta

import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine

from settings import Settings

def extract_data(
        start_date:str = str(date.today() - timedelta(days=365 * 1)),
        end_date:str = str(date.today()),
        tech_list:List[str] = ["AAPL", "GOOG", "MSFT", "AMZN"],
        company_list:List[str] = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZON"]
    ):

    # yfinance 데이터 download
    stock_list = [
        yf.download(tech, start = start_date, end = end_date)
        for tech in tech_list
    ]

    # 각 DataFrame에 회사명 추가하기
    for company, com_name in zip(stock_list, company_list):
        company["company_name"] = com_name

    df = pd.concat(stock_list, axis=0)

    df = df.reset_index(drop=False)

    return df

if __name__ == "__main__":
    TABLE_NAME = "stock_ohlcv"
    df = extract_data()

    engine = create_engine(Settings.POSTGRES_HOST)

    df.to_sql(TABLE_NAME, con=engine, if_exists="append", index=False)
from datetime import date, timedelta

from pykrx import stock
from sqlalchemy import create_engine

from settings import Settings


def extract_data(
    start_date: str = str(date.today() - timedelta(days=365 * 1)),
    end_date: str = str(date.today()),
    ticker: str = "005930",
):

    df = stock.get_market_ohlcv_by_date(start_date, end_date, ticker)
    df["Ticker"] = ticker

    df = df.reset_index()
    df.columns = Settings.COLUMNS

    return df


if __name__ == "__main__":
    TABLE_NAME = "stock"
    df = extract_data()

    engine = create_engine(Settings.POSTGRES_HOST)

    df.to_sql(TABLE_NAME, con=engine, if_exists="append", index=False)

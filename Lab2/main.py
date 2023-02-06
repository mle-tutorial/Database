from datetime import date, timedelta

from pykrx import stock

from settings import Settings


def extract_data(
    start_date: str = str(date.today() - timedelta(days=365 * 1)),
    end_date: str = str(date.today()),
    ticker: str = "005930",
):

    # Download Data
    df = stock.get_market_ohlcv_by_date(start_date, end_date, ticker)

    # Preprocessing Data
    df["Ticker"] = ticker
    df = df.reset_index()
    df.columns = Settings.COLUMNS

    return df


if __name__ == "__main__":

    # Extract Data
    df = extract_data()

    # DataFrame to csv
    df.to_csv("stock.csv", index=False)

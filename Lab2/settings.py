import os
import dotenv

dotenv.load_dotenv()


class Settings:

    COLUMNS = [
        "Date",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
        "Value",
        "Change",
        "Ticker",
    ]

#!/bin/bash

# Load Data

docker cp yfinance.csv postgresql:/

docker exec -it postgresql \
psql -U postgres \
-c "CREATE DATABASE stock"

docker exec -it postgresql \
psql \
-U postgres \
-d stock \
-c "CREATE TABLE stock_ohlcv (
    STOCK_DATE DATE NULL,
    Open FLOAT NULL,
    High FLOAT NULL,
    Low FLOAT NULL,
    Close FLOAT NULL,
    AdjClose FLOAT NULL,
    Volume BIGINT NULL,
    Company_name VARCHAR(20) NULL
 )"
 
docker exec -it postgresql\
 psql \
 -U postgres \
 -d stock \
 -c "COPY stock_ohlcv FROM '/yfinance.csv' WITH (FORMAT csv, header)"
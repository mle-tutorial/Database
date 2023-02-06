#!/bin/bash

docker cp stock.csv postgresql:/

docker exec -it postgresql \
psql -U postgres \
-c "CREATE DATABASE stock"

docker exec -it postgresql \
psql \
-U postgres \
-d stock \
-c "CREATE TABLE stock (
    Date DATE NULL,
    Open INT NULL,
    High INT NULL,
    Low INT NULL,
    Close INT NULL,
    Volume INT NULL,
    Value BIGINT NULL,
    Change FLOAT NULL,
    Ticker FLOAT NULL
 )"
 
docker exec -it postgresql\
 psql \
 -U postgres \
 -d stock \
 -c "COPY stock FROM '/stock.csv' WITH (FORMAT csv, header)"
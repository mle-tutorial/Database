# Lab1

## Database 구축

- 실습에서는 편의를 위해 Docker로 Database를 띄워 운영하지만 Production환경에서는 Database가 이미 존재하거나 클라우드 DB를 사용합니다.
- `bash postgres_docker.sh`

## Data Download & Data Load

- `python main.py` 명령어로 yfinance데이터를 다운로드 받습니다.
- `python main.py` 명령어로 다운받은 데이터를 Database에 insert합니다.

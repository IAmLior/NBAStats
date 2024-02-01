# NBAStats
Using Kaggle "NBA games data" for achieving interesting insights over this data

## Getting started:
1. create a Cassandra DB instance. You can do it using docker.
    ```docker pull cassandra:latest```
    ```docker run -p 9042:9042 --rm --name cassandra -d cassandra:latest```
    ```docker exec -it cassandra cqlsh```
2. Configure the NBAStats keyspace on your cassandra cluster.
    ```CREATE KEYSPACE IF NOT EXISTS NbaTests WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': 1 };```

## Steps (Internal):
1. our dataset https://www.kaggle.com/datasets/nathanlauga/nba-games?select=games.csv
2. select at least 3 tables and list their columns - build full scheme
3. create insertion scripts - figure out how to make it correctly according to the scheme
4. use GPT for selecting complicated queries over the data
5. create the queries (data analysis)
6. create python scripts for data (integrate)

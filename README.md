# NBAStats
Using Kaggle "NBA games data" for achieving interesting insights over this data

## Getting started:
1. create a Cassandra DB instance. You can do it using docker.
    ```docker pull cassandra:latest```
    ```docker run -p 9042:9042 --rm --name cassandra -d cassandra:latest```
    ```docker exec -it cassandra cqlsh```
2. Configure the NBAStats keyspace on your cassandra cluster.
    ```CREATE KEYSPACE IF NOT EXISTS NbaTests WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': 1 };```

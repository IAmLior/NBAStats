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


## Plots
![starting_five_vs_bench](https://github.com/IAmLior/NBAStats/assets/153426809/51bffb8d-126a-4095-b7b9-ff14a6a8351f)

![ratio_fgpct_vs_fg3pct](https://github.com/IAmLior/NBAStats/assets/153426809/9772b6d0-edc1-49bf-b8c1-1533b360b4b3)

![positions_avg](https://github.com/IAmLior/NBAStats/assets/153426809/95b51704-84fe-46f9-9996-17770a59f98e)

![points_per_minutes](https://github.com/IAmLior/NBAStats/assets/153426809/8515ee6f-29d5-4e10-b63b-ccda3f13432e)

![home_w_vs_road_w_ratio2](https://github.com/IAmLior/NBAStats/assets/153426809/a33336e6-6afb-4727-93d7-7593e855d55f)

![best_attacking_team_per_season](https://github.com/IAmLior/NBAStats/assets/153426809/1353a2c6-af02-44f8-bb11-b9bec4836adb)

![avg_points_per_season_per_team](https://github.com/IAmLior/NBAStats/assets/153426809/f82c640e-9d61-4fa7-b34f-ae12e0a6b6e7)


# NBAStats
Using Kaggle "NBA games data" for achieving interesting insights over this data

## Getting started:
1. create a Cassandra DB instance. You can do it using docker.
    ```docker pull cassandra:latest```
    ```docker run -p 9042:9042 --rm --name cassandra -d cassandra:latest```
    ```docker exec -it cassandra cqlsh```
2. Configure the NBAStats keyspace on your cassandra cluster.
    ```create keyspace NBATests with replication = { 'class': 'SimpleStrategy', 'replication_factor': 1 };```

1.	Our Database Schema
•	Games – aims to retrieve data for games of a team in each season.
 
o	game_id | Integer | Primary key.
o	game_date | Date.
o	season | Integer | Partition key.
o	team_id | Integer | Partition key.
o	team_nickname | Text.
o	pts | Integer.
o	fg_pct | Float.
o	ft_pct | Float.
o	fg3_pct | Float.
o	ast | Integer.
o	reb | Integer.
o	is_win | Boolean.
o	is_home_team | Boolean.
 

•	Ranking – aims to retrieve data for ranking of a team in each season.
 
o	team_id | Integer | Partition key.
o	team_nickname | Text.
o	season | Integer | Partition key.
o	standing_date | Date |        Primary key.
o	conference | Text.
o	games | Integer.
o	wins | Integer.
o	losses | Integer.
o	win_pct | Float.
o	home_record | Text
o	road_record | Text
 

•	Game Per Player – aims to retrieve data for players statistics playing in specific positions.
 
o	game_id | Integer | Primary key.
o	game_date | Date.
o	team_id | Integer | Primary key.
o	player_id | Integer | Primary key.
o	player_name | Text.
o	start_position | text | partition key.
o	minutes_played | time.
o	fg_made | float.
o	fg_attempted | float.
o	fg_precentage | float.
o	fg3_made | float.
o	fg3_attempted | float.
o	fg3_precentage | float.
o	ft_made | float.
o	ft_attempted | float.
o	ft_precentage | float.
o	rebounds |float.
o	assists | float.
o	steals | float.
o	blocks | float.
o	turnovers | float.
o	personal_fouls | float.
o	points | float.



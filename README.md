# NBAStats
Using Kaggle "NBA games data" for achieving interesting insights over this data

## Getting started:
1. create a Cassandra DB instance. You van do it using docker.
    ```docker pull cassandra:latest```
    ```docker run...```
2. Configure the NBAStats keyspace on your cassandra cluster.
    ```create keyspace if not exists NBAStats with replication = { 'class': 'SimpleStrategy', replication_factor': 1 };```

## Steps (Internal):
1. our dataset https://www.kaggle.com/datasets/nathanlauga/nba-games?select=games.csv
2. select at least 3 tables and list their columns - build full scheme
3. create insertion scripts - figure out how to make it correctly according to the scheme
4. use GPT for selecting complicated queries over the data
5. create the queries (data analysis)
6. create python scripts for data (integrate)

## Tables:
### teams table
* Team ID
* ABBREVIATION
* NICKNAME
* YEARFOUNDED
* CITY
* ARENA
* ARENACAPACITY

### games table
* GAME_DATE_EST
* GAME_ID
* HOME_TEAM_ID
* VISITOR_TEAM_ID
* SEASON
* PTS_home
* FG_PCT_home
* FT_PCT_home
* FG3_PCT_home
* AST_home
* REB_home
* PTS_away
* FG_PCT_away
* FT_PCT_away
* FG3_PCT_away
* AST_away
* REB_away
* HOME_TEAM_WINS

### ranking table
* TEAM_ID
* SEASON_ID (startwith 2 only)
* STANDINGSDATE
* CONFERENCE
* TEAM
* G (games)
* W (wins)
* L (looses)
* W_PCT

### players table
* PLAYER_NAME
* TEAM_ID
* PLAYER_ID
* SEASON

### games details (game per player) table
* GAME_ID
* PLAYER_ID
* START_POSITION
* MIN
* FGM
* FGA
* FG_PCT
* FG3M
* FG3A
* FG3_PCT
* FTM
* FTA
* FT_PCT
* REB
* AST
* STL
* BLK
* TO
* PF
* PTS
* PLUS_MINUS

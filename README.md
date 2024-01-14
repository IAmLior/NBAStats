# NBAStats
Using Kaggle "NBA games data" for achieving interesting insights over this data


##Steps:
1. open a git repo with scripts divided for each project task
2. dataset https://www.kaggle.com/datasets/nathanlauga/nba-games?select=games.csv
3. select at least 3 tables and list their columns - build full scheme
4. create insertion scripts - figure out how to make it correctly according to the scheme
5. use GPT for selecting complicated queries over the data
6. create the queries (data analysis)
7. create python scripts for data (integrate)

##Tables:
###teams table
* Team ID
* ABBREVIATION
* NICKNAME
* YEARFOUNDED
* CITY
* ARENA
* ARENACAPACITY

###games table
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

###ranking table
* TEAM_ID
* SEASON_ID (startwith 2 only)
* STANDINGSDATE
* CONFERENCE
* TEAM
* G (games)
* W (wins)
* L (looses)
* W_PCT

###players table
* PLAYER_NAME
* TEAM_ID
* PLAYER_ID
* SEASON

###games details (game per player) table
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

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
import csv

class Game(Model):
    game_id = columns.Integer(primary_key=True)
    game_date = columns.Date()
    home_team_id = columns.Integer()
    visitor_team_id = columns.Integer()
    season = columns.Integer()
    pts_home = columns.Integer()
    fg_pct_home = columns.Float()
    ft_pct_home = columns.Float()
    fg3_pct_home = columns.Float()
    ast_home = columns.Integer()
    reb_home = columns.Integer()
    pts_away = columns.Integer()
    fg_pct_away = columns.Float()
    ft_pct_away = columns.Float()
    fg3_pct_away = columns.Float()
    ast_away = columns.Integer()
    reb_away = columns.Integer()
    home_team_wins = columns.Boolean()

    __table_name__ = "Games"

connection.setup(['127.0.0.1'], 'nbatests2')
sync_table(Game)
csv_file_path = '/Users/dviryomtov/NBAStats/Data/games.csv'

with open(csv_file_path, mode='r') as data:
    csv_reader = csv.DictReader(data)
    games_mapping = []
    for row in csv_reader:
        games_mapping.append(row)

for game in games_mapping:
    for key, value in game.items():
        if value == '':
            game[key] = None

    team_model = Game.create(
        game_id = game['GAME_ID'],
        game_date = game['GAME_DATE_EST'],
        home_team_id = game['HOME_TEAM_ID'],
        visitor_team_id = game['VISITOR_TEAM_ID'],
        season = game['SEASON'],
        pts_home = game['PTS_home'] if isinstance(game['PTS_home'], int) else 0,
        fg_pct_home = game['FG_PCT_home'],
        ft_pct_home = game['FT_PCT_home'],
        fg3_pct_home = game['FG3_PCT_home'],
        ast_home = game['AST_home'] if isinstance(game['AST_home'], int) else 0,
        reb_home = game['REB_home'] if isinstance(game['REB_home'], int) else 0,
        pts_away = game['PTS_away'] if isinstance(game['PTS_away'], int) else 0,
        fg_pct_away = game['FG_PCT_away'],
        ft_pct_away = game['FT_PCT_away'],
        fg3_pct_away = game['FG3_PCT_away'],
        ast_away = game['AST_away'] if isinstance(game['AST_away'], int) else 0,
        reb_away = game['REB_away'] if isinstance(game['REB_away'], int) else 0,
        home_team_wins = game['HOME_TEAM_WINS']
    )
    print(f"Created game {game['GAME_ID']}")

print(f"Created {Game.objects.count()} games.")


from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
import csv

def get_valid_number(number: str):
    if number.isdigit():
        return int(number)
    
    if number[:-2].isdigit():
        return int(number[:-2])
    
    return 0

class Game(Model):
    game_id = columns.Integer(primary_key=True)
    game_date = columns.Date()
    season = columns.Integer(partition_key=True)
    team_id = columns.Integer(partition_key=True)
    pts = columns.Integer()
    fg_pct = columns.Float()
    ft_pct = columns.Float()
    fg3_pct = columns.Float()
    ast = columns.Integer()
    reb = columns.Integer()
    is_win = columns.Boolean()
    is_home_team = columns.Boolean()

    __table_name__ = "Games"

connection.setup(['127.0.0.1'], 'nbatests')
sync_table(Game)
csv_file_path = 'Data\\games.csv'

with open(csv_file_path, mode='r') as data:
    csv_reader = csv.DictReader(data)
    games_mapping = []
    for row in csv_reader:
        games_mapping.append(row)

for game in games_mapping:
    for key, value in game.items():
        if value == '':
            game[key] = None

    game_home_model = Game.create(
        game_id = game['GAME_ID'],
        game_date = game['GAME_DATE_EST'],
        team_id = game['HOME_TEAM_ID'],
        season = game['SEASON'],
        pts = get_valid_number(game['PTS_home']),
        fg_pct = game['FG_PCT_home'],
        ft_pct = game['FT_PCT_home'],
        fg3_pct = game['FG3_PCT_home'],
        ast = get_valid_number(game['AST_home']),
        reb = get_valid_number(game['REB_home']),
        is_win = game['HOME_TEAM_WINS'],
        is_home_team = True
    )
    game_away_model = Game.create(
        game_id = game['GAME_ID'],
        game_date = game['GAME_DATE_EST'],
        team_id = game['VISITOR_TEAM_ID'],
        season = game['SEASON'],
        pts = get_valid_number(game['PTS_away']),
        fg_pct = game['FG_PCT_away'],
        ft_pct = game['FT_PCT_away'],
        fg3_pct = game['FG3_PCT_away'],
        ast = get_valid_number(game['AST_away']),
        reb = get_valid_number(game['REB_away']),
        is_win = not game['HOME_TEAM_WINS'],
        is_home_team = False
    )
    print(f"Created game {game['GAME_ID']}")

print(f"Created {Game.objects.count()} games.")
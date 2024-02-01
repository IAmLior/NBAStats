from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from datetime import datetime
import csv

def get_valid_number(number: str):
    if number.isdigit():
        return int(number)
    
    if number[:-2].isdigit():
        return int(number[:-2])
    
    return 0

class GamePerPlayer(Model):
    game_id = columns.Integer(primary_key=True)
    game_date = columns.Date()
    team_id = columns.Integer(primary_key=True)
    player_id = columns.Integer(primary_key=True)
    start_position = columns.Text(partition_key=True, max_length=1)
    minutes_played = columns.Time()
    fg_made = columns.Float()
    fg_attempted = columns.Float()
    fg_precentage = columns.Float()
    fg3_made = columns.Float()
    fg3_attempted = columns.Float()
    fg3_precentage = columns.Float()
    ft_made = columns.Float()
    ft_attempted = columns.Float()
    ft_precentage = columns.Float()
    rebounds = columns.Float()
    assists = columns.Float()
    steals = columns.Float()
    blocks = columns.Float()
    turnovers = columns.Float()
    personal_fouls = columns.Float()
    points = columns.Float()
    plus_minus = columns.Float()

connection.setup(['127.0.0.1'], 'nbatests')
sync_table(GamePerPlayer)
gpp_csv_file_path = 'Data\\games_details.csv'
games_csv_file_path = 'Data\\games.csv'

with open(games_csv_file_path, mode='r') as data:
    csv_reader = csv.DictReader(data)
    games_dates_mapping = {}
    for row in csv_reader:
        games_dates_mapping[row['GAME_ID']] = row['GAME_DATE_EST']

with open(gpp_csv_file_path, mode='r') as data:
    csv_reader = csv.DictReader(data)
    game_per_player_mapping = []
    for row in csv_reader:
        game_per_player_mapping.append(row)

for gpp in game_per_player_mapping:
    for key, value in gpp.items():
        if value == '':
            gpp[key] = None
    try:
        min_played = datetime.strptime(gpp['MIN'], '%M:%S').time() if gpp['MIN'] is not None else gpp['MIN']
    except:
        min_played = None

    gpp_model = GamePerPlayer.create(
        game_id = gpp['GAME_ID'],
        game_date = games_dates_mapping[gpp['GAME_ID']],
        team_id = gpp['TEAM_ID'],
        player_id = gpp['PLAYER_ID'],
        start_position = gpp['START_POSITION'] if gpp['START_POSITION'] is not None else 'B',
        minutes_played = min_played,
        fg_made = gpp['FGM'],
        fg_attempted = gpp['FGA'],
        fg_precentage = gpp['FG_PCT'],
        fg3_made = gpp['FG3M'],
        fg3_attempted = gpp['FG3A'],
        fg3_precentage = gpp['FG3_PCT'],
        ft_made = gpp['FTM'],
        ft_attempted = gpp['FTA'],
        ft_precentage = gpp['FT_PCT'],
        rebounds = gpp['REB'],
        assists = gpp['AST'],
        steals = gpp['STL'],
        blocks = gpp['BLK'],
        turnovers = gpp['TO'],
        personal_fouls = gpp['PF'],
        points = gpp['PTS'],
        plus_minus = gpp['PLUS_MINUS']
    )
    print(f"Created GAM for game {gpp['GAME_ID']} for player {gpp['PLAYER_ID']}")

print(f"Created {GamePerPlayer.objects.count()} GamesPerPlayer.")


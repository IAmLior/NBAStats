from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
import csv

class Player(Model):
    player_id = columns.Integer(primary_key=True)
    team_id = columns.Integer(primary_key=True)
    player_name = columns.Text()
    season = columns.Integer()

    __table_name__ = "Players"


connection.setup(['127.0.0.1'], 'nbatests')
sync_table(Player)
csv_file_path = 'Data\\players.csv'

with open(csv_file_path, mode='r') as data:
    csv_reader = csv.DictReader(data)
    players_mapping = []
    for row in csv_reader:
        players_mapping.append(row)

for player in players_mapping:
    for key, value in player.items():
        if value == '':
            player[key] = None

    team_model = Player.create(
        player_id = player['PLAYER_ID'],
        team_id = player['TEAM_ID'],
        player_name = player['PLAYER_NAME'],
        season = player['SEASON']
    )
    print(f"Created player {player['PLAYER_NAME']} for team {player['TEAM_ID']}")

print(f"Created {Player.objects.count()} players.")


from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
import csv

class Rank(Model):
    team_id = columns.Integer(primary_key=True)
    season = columns.Integer(primary_key=True)
    standing_date = columns.Date(primary_key=True)
    conference = columns.Text()
    games = columns.Integer()
    wins = columns.Integer()
    losses = columns.Integer()
    win_pct = columns.Float()

    __table_name__ = "Ranking"

connection.setup(['127.0.0.1'], 'nbatests22')
sync_table(Rank)
csv_file_path = '/Users/dviryomtov/NBAStats/Data/ranking.csv'

with open(csv_file_path, mode='r') as data:
    csv_reader = csv.DictReader(data)
    ranking_mapping = []
    for row in csv_reader:
        ranking_mapping.append(row)
for rank in ranking_mapping:
    for key, value in rank.items():
        if value == '':
            rank[key] = None
    
    if rank['SEASON_ID'][0] == '1':
        continue

    rank_model = Rank.create(
        team_id = rank['TEAM_ID'],
        season = rank['SEASON_ID'][1:],
        standing_date = rank['STANDINGSDATE'],
        conference = rank['CONFERENCE'],
        games = rank['G'],
        wins = rank['W'],
        losses = rank['L'],
        win_pct = rank['W_PCT']
    )
    print(f"Created rank for team {rank['TEAM_ID']} by date {rank['STANDINGSDATE']} in season{rank['SEASON_ID'][1:]}")

print(f"Created {Rank.objects.count()} ranks.")


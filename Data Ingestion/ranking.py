from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
import csv  
from pathlib import Path


class Rank(Model):
    team_id = columns.Integer(partition_key=True)
    team_nickname = columns.Text()
    season = columns.Integer(partition_key=True)
    standing_date = columns.Date(primary_key=True)
    conference = columns.Text()
    games = columns.Integer()
    wins = columns.Integer()
    losses = columns.Integer()
    win_pct = columns.Float()
    home_record = columns.Text()
    road_record = columns.Text()

    __table_name__ = "Ranking"

connection.setup(['127.0.0.1'], 'nbatests')
sync_table(Rank)
ranking_csv_file_path = Path(__file__).parent.parent / 'Data/ranking.csv'
teams_csv_file_path = Path(__file__).parent.parent / 'Data/teams.csv'

with open(teams_csv_file_path, mode='r') as data:
    csv_reader = csv.DictReader(data)
    teams_nicknames_mapping = {}
    for row in csv_reader:
        teams_nicknames_mapping[row['TEAM_ID']] = row['NICKNAME']

with open(ranking_csv_file_path, mode='r') as data:
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
        team_nickname = teams_nicknames_mapping[rank['TEAM_ID']],
        season = rank['SEASON_ID'][1:],
        standing_date = rank['STANDINGSDATE'],
        conference = rank['CONFERENCE'],
        games = rank['G'],
        wins = rank['W'],
        losses = rank['L'],
        win_pct = rank['W_PCT'],
        home_record = rank['HOME_RECORD'],
        road_record = rank['ROAD_RECORD']
    )
    print(f"Created rank for team {rank['TEAM_ID']} by date {rank['STANDINGSDATE']} in season{rank['SEASON_ID'][1:]}")

print(f"Created {Rank.objects.count()} ranks.")


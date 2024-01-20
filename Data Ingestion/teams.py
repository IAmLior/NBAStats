from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
import csv

class Team(Model):
    team_id = columns.Integer(primary_key=True)
    abbreviation = columns.Text(max_length=3, min_length=3)
    nickname = columns.Text()
    year_founded = columns.Integer()
    city = columns.Text()
    arena = columns.Text()
    arena_capacity = columns.Integer(default=0)

connection.setup(['127.0.0.1'], 'nbatests')
sync_table(Team)
csv_file_path = 'Data\\teams.csv'

with open(csv_file_path, mode='r') as data:
    csv_reader = csv.DictReader(data)
    teams_mapping = []
    for row in csv_reader:
        teams_mapping.append(row)

# empty_values = []
# for team in teams_mapping:
#     for key, value in team.items():
#         if value == '':
#             empty_values.append({
#                 'team': team,
#                 'key': key
#             })

# for item in empty_values:
#     del item['team'][item['key']]

for team in teams_mapping:
    for key, value in team.items():
        if value == '':
            team[key] = None

    team_model = Team.create(team_id = team['TEAM_ID'],
                                  abbreviation = team['ABBREVIATION'],
                                  nickname = team['NICKNAME'],
                                  year_founded = team['YEARFOUNDED'],
                                  city = team['CITY'],
                                  arena = team['ARENA'],
                                  arena_capacity = team['ARENACAPACITY'] if  team['ARENACAPACITY'] is not None else 0)
    print(f"Created team {team['NICKNAME']}")

print(f"Created {Team.objects.count()} teams.")

# over_20k = Team.objects(arena_capacity>20000)
# for instance in over_20k:
#     print(instance.nickname)


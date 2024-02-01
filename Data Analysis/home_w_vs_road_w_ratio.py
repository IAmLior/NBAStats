from cassandra.cluster import Cluster
import matplotlib.pyplot as plt

cassandra_cluster = Cluster()
cassandra_session = cassandra_cluster.connect()
cassandra_keyspace_name = 'nbatests'
cassandra_session.set_keyspace(cassandra_keyspace_name),

query = " SELECT team_id, team_nickname, season, HOME_RECORD, ROAD_RECORD FROM Ranking WHERE games = 82 GROUP BY TEAM_id, SEASON ALLOW FILTERING ;"
prepared_query = cassandra_session.prepare(query)
results = cassandra_session.execute(prepared_query)

teams = {}
r = results.current_rows
for row in results:
    if row.team_nickname in teams:
        teams[row.team_nickname].append({'season': row.season, 'home_record': row.home_record, 'road_record': row.road_record})
    else:
        teams[row.team_nickname] = [{'season': row.season, 'home_record': row.home_record, 'road_record': row.road_record}]

team_ratios = {}
for team, data in teams.items():
    ratios = []
    seasons = []
    for season in data:
        home_wins, home_losses = map(int, season['home_record'].split('-'))
        road_wins, road_losses = map(int, season['road_record'].split('-'))
        if road_wins != 0:
            ratio = home_wins / road_wins
        else:
            ratio = 0
        ratios.append(ratio)
        seasons.append(str(season['season']))
    # Sort the seasons in ascending order
    seasons, ratios = zip(*sorted(zip(seasons, ratios)))
    team_ratios[team] = (seasons, ratios)

# Determine the maximum ratio value across all teams
max_ratio = max(max(ratios) for _, (_, ratios) in team_ratios.items())

# Create a full-screen figure
plt.figure(figsize=(20, 10))  # You may adjust the figsize according to your screen resolution

# Plotting
for team, (seasons, ratios) in team_ratios.items():
    plt.scatter(seasons, ratios, label=f'{team}', marker='o')

plt.xlabel('Season')
plt.ylabel('Ratio (Home Wins / Road Wins)')
plt.title('Ratio of Home Wins to Road Wins for Each Team Over Seasons')
plt.xticks(rotation=45)
plt.grid(True)

# Place legend under the plot
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), shadow=True, ncol=5)
plt.subplots_adjust(bottom=0.3)  # Adjust bottom margin to make room for the legend

# Set y-axis ticks to start from 0 and display intervals of 0.2
plt.yticks([i / 5 for i in range(int(max_ratio * 5) + 2)])

plt.show()
cassandra_cluster.shutdown()


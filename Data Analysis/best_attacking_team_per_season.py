from cassandra.cluster import Cluster
import matplotlib.pyplot as plt

cassandra_cluster = Cluster()
cassandra_session = cassandra_cluster.connect()
cassandra_keyspace_name = 'nbatests'
cassandra_session.set_keyspace(cassandra_keyspace_name),

query =  "SELECT season, team_id, team_nickname, AVG(pts) AS avg_points FROM games GROUP BY season, team_id"

prepared_query = cassandra_session.prepare(query)
results = cassandra_session.execute(prepared_query)
# Store the highest average points for each season
highest_avg_points = {}

for row in results:
    season = row.season
    team_nickname = row.team_nickname
    avg_points = row.avg_points

    if season not in highest_avg_points or avg_points > highest_avg_points[season][1]:
        highest_avg_points[season] = (team_nickname, avg_points)

sorted_data = sorted(highest_avg_points.items())
seasons, teams_avg_points = zip(*sorted_data)
teams, avg_points = zip(*teams_avg_points)

# Creating the bar plot
plt.figure(figsize=(15, 8))
plt.bar(range(len(seasons)), avg_points, color='skyblue')

# Adding labels and title
plt.xlabel('Season')
plt.ylabel('Average Points')
plt.title('Highest Average Points for Each Season')
plt.xticks(range(len(seasons)), seasons, rotation=45, ha='right')

# Adding data labels
for i in range(len(seasons)):
    plt.text(i, avg_points[i], f"{teams[i]}: {avg_points[i]}", ha='center', va='bottom')

# Adding description
plt.figtext(0.5, 0.01, 'Data Source: Your Data Source', wrap=True, horizontalalignment='center', fontsize=10)

# Displaying the plot
plt.tight_layout()
plt.show()
cassandra_cluster.shutdown()
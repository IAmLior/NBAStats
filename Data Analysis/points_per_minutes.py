from cassandra.cluster import Cluster
from cassandra.query import dict_factory
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

cassandra_cluster = Cluster()
cassandra_session = cassandra_cluster.connect()
cassandra_keyspace_name = 'nbatests'
cassandra_session.set_keyspace(cassandra_keyspace_name)
cassandra_session.row_factory = dict_factory

player_query = "select player_name as name, points, minutes_played from game_per_player limit 100 ALLOW FILTERING;"
player_prepared_query = cassandra_session.prepare(player_query)
player_results = cassandra_session.execute(player_prepared_query)
player_df = pd.DataFrame(player_results)

player_df['minutes_played'] = pd.to_datetime(player_df['minutes_played'], format='%H:%M:%S.%f')
player_df['minutes_played']
player_df = player_df.sort_values(by='minutes_played')

plt.figure(figsize=(10, 6))
plt.plot(player_df['minutes_played'], player_df['points'], marker='o', label='Points')
plt.fill_between(player_df['minutes_played'], player_df['points'], alpha=0.2, color='skyblue', label='Area Under Graph')

plt.title('Points vs. Time Played')
plt.xlabel('Time Played')
plt.ylabel('Points')
plt.legend()
plt.show()
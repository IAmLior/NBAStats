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

home_games_query = f"select season, team_id, team_nickname as nickname, avg(pts) as avg from games where is_home_team = True group by season, team_id ALLOW FILTERING;"
home_games_prepared_query = cassandra_session.prepare(home_games_query)
home_games_results = cassandra_session.execute(home_games_prepared_query)
home_df = pd.DataFrame(home_games_results).rename(columns={'avg': 'avg_home'})

away_games_query = f"select season, team_id, team_nickname as nickname, avg(pts) as avg from games where is_home_team = False group by season, team_id ALLOW FILTERING;"
away_games_prepared_query = cassandra_session.prepare(away_games_query)
away_games_results = cassandra_session.execute(away_games_prepared_query)
away_df = pd.DataFrame(away_games_results).rename(columns={'avg': 'avg_away'})

games_df = pd.merge(home_df[['season', 'team_id', 'nickname',  'avg_home']], away_df[['season', 'team_id', 'nickname', 'avg_away']], on=['season', 'team_id', 'nickname'])
games_df['ratio_diff'] = games_df['avg_home'] / games_df['avg_away']

plt.figure(figsize=(12, 8))
sns.scatterplot(x='season', y='ratio_diff', hue='nickname', data=games_df, marker='o', s=100)
plt.axhline(y=1, color='grey', linestyle='--', label='y = 1')
plt.title('Ratio Difference between avg_home and avg_away by Team and Year')
plt.xlabel('Season')
plt.ylabel('Ratio Difference (avg_home / avg_away)')
plt.legend(title='Team', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.show()

cassandra_cluster.shutdown()
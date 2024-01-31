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

games_query = "select season, team_id, avg(pts) as avg, is_home_team from games group by season, team_id, is_home_team ALLOW FILTERING;"
games_prepared_query = cassandra_session.prepare(games_query)
games_results = cassandra_session.execute(games_prepared_query)
games_df = pd.DataFrame(games_results)
home_df = games_df[games_df['is_home_team'] == True].rename(columns={'avg': 'avg_home'}).drop(columns=['is_home_team'])
away_df = games_df[games_df['is_home_team'] == False].rename(columns={'avg': 'avg_away'}).drop(columns=['is_home_team'])
games_df = pd.merge(home_df[['season', 'team_id', 'avg_home']], away_df[['season', 'team_id', 'avg_away']], on=['season', 'team_id'])

teams_query = "select team_id, abbreviation, nickname from teams"
teams_prepared_query = cassandra_session.prepare(teams_query)
teams_results = cassandra_session.execute(teams_prepared_query)
teams_df = pd.DataFrame(teams_results)


merged_df = pd.merge(games_df, teams_df, on='team_id')
merged_df['ratio_diff'] = merged_df['avg_home'] / merged_df['avg_away']
heatmap_data = merged_df.pivot(index='nickname', columns='season', values='ratio_diff')

plt.figure(figsize=(12, 8))
# sns.lineplot(x='season', y='ratio_diff', hue='nickname', data=merged_df, marker='o')
# sns.scatterplot(x='season', y='ratio_diff', hue='nickname', data=merged_df, marker='o', s=100)
sns.heatmap(heatmap_data, cmap='coolwarm', center=1, annot=True, linewidths=.5, fmt=".2f", cbar_kws={'label': 'Ratio Difference'})

plt.axvspan(2, 3, color='gray', alpha=0.2)


# Adding labels and title
plt.title('Ratio Difference between avg_home and avg_away by Team and Year')
plt.xlabel('Season')
plt.ylabel('Ratio Difference (avg_home / avg_away)')
plt.legend(title='Team', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.xticks(rotation=45)
plt.yticks(rotation=0)

plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

plt.show()


cassandra_cluster.shutdown()
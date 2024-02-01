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

home_games_query = f"select season, team_id, avg(pts) as avg from games where is_home_team = True group by season, team_id ALLOW FILTERING;"
home_games_prepared_query = cassandra_session.prepare(home_games_query)
home_games_results = cassandra_session.execute(home_games_prepared_query)
home_df = pd.DataFrame(home_games_results).rename(columns={'avg': 'avg_home'})

away_games_query = f"select season, team_id, avg(pts) as avg from games where is_home_team = False group by season, team_id ALLOW FILTERING;"
away_games_prepared_query = cassandra_session.prepare(away_games_query)
away_games_results = cassandra_session.execute(away_games_prepared_query)
away_df = pd.DataFrame(away_games_results).rename(columns={'avg': 'avg_away'})

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
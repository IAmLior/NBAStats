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

scoring_pct_query = f"select season, team_id, team_nickname as nickname, avg(fg_pct) as avg_fg, avg(fg3_pct) as avg_fg3 from games group by season, team_id ALLOW FILTERING;"
scoring_pct_prepared_query = cassandra_session.prepare(scoring_pct_query)
scoring_pct_results = cassandra_session.execute(scoring_pct_prepared_query)
scoring_pct_df = pd.DataFrame(scoring_pct_results)

plt.figure(figsize=(12, 6))
plt.scatter(scoring_pct_df['season'], scoring_pct_df['avg_fg'], label='Field Goal Percentage (avg_fg)', marker='o', alpha=0.7)
plt.scatter(scoring_pct_df['season'], scoring_pct_df['avg_fg3'], label='Three-Point Percentage (avg_fg3)', marker='s', alpha=0.7)
plt.xlabel('Season')
plt.ylabel('Percentage')
plt.title('Field Goal Percentage and Three-Point Percentage Over the Years')
plt.legend()
plt.grid(True)
plt.show()

cassandra_cluster.shutdown()
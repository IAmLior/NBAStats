from cassandra.cluster import Cluster
from cassandra.query import dict_factory
import numpy as np
import matplotlib.pyplot as plt

cassandra_cluster = Cluster()
cassandra_session = cassandra_cluster.connect()
cassandra_keyspace_name = 'nbatests'
cassandra_session.set_keyspace(cassandra_keyspace_name)
cassandra_session.row_factory = dict_factory

queries = {}
fg_precentage_starting_5_query = "select avg(fg_precentage) as fg_precentage_starting_5 from Game_Per_Player where start_position > 'B' AND fg_attempted > 0  ALLOW FILTERING;"
fg3_precentage_starting_5_query = "select avg(fg3_precentage) as fg3_precentage_starting_5 from Game_Per_Player where start_position > 'B' AND fg3_attempted > 0  ALLOW FILTERING;"
ft_precentage_starting_5_query = "select avg(ft_precentage) as ft_precentage_starting_5 from Game_Per_Player where start_position > 'B' AND ft_attempted > 0  ALLOW FILTERING;"

fg_precentage_bench_query = "select avg(fg_precentage) as fg_precentage_bench from Game_Per_Player where start_position > 'C' AND fg_attempted > 0  ALLOW FILTERING;"
fg3_precentage_bench_query = "select avg(fg3_precentage) as fg3_precentage_bench from Game_Per_Player where start_position > 'C' AND fg3_attempted > 0  ALLOW FILTERING;"
ft_precentage_bench_query = "select avg(ft_precentage) as ft_precentage_bench from Game_Per_Player where start_position > 'C' AND ft_attempted > 0  ALLOW FILTERING;"

queries['fg_precentage_starting_5'] = {'query' :fg_precentage_starting_5_query}
queries['fg3_precentage_starting_5'] = {'query' :fg3_precentage_starting_5_query}
queries['ft_precentage_starting_5'] = {'query' :ft_precentage_starting_5_query}
queries['fg_precentage_bench'] = {'query' :fg_precentage_bench_query}
queries['fg3_precentage_bench'] = {'query' :fg3_precentage_bench_query}
queries['ft_precentage_bench'] = {'query' :ft_precentage_bench_query}

for key, value in queries.items():
    prepared_query = cassandra_session.prepare(value['query'])
    results = cassandra_session.execute(prepared_query)
    value['results'] = results.current_rows[0][key]

metrics = ['FG', 'FG3', 'FT']
starting_5_results = [queries[f'{metric.lower()}_precentage_starting_5']['results'] for metric in metrics]
bench_results = [queries[f'{metric.lower()}_precentage_bench']['results'] for metric in metrics]

# Setting up the position of bars
bar_width = 0.35
index = np.arange(len(metrics))

# Plotting
plt.bar(index, starting_5_results, bar_width, label='Starting 5')
plt.bar(index + bar_width, bench_results, bar_width, label='Bench')

plt.xlabel('Metrics')
plt.ylabel('Percentage')
plt.title('Comparison of Metrics between Starting 5 and Bench')
plt.xticks(index + bar_width / 2, metrics)
plt.legend()

plt.tight_layout()
plt.show()
print(queries)

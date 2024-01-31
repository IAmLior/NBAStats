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

positions_query = "select start_position, avg(points) as points_avg, avg(assists) as assists_avg, avg(rebounds) as rebounds_avg, avg(steals) as steals_avg, avg(blocks) as avg_blocks, avg(plus_minus) as avg_plus_minus from Game_Per_Player where start_position > 'B' group by start_position ALLOW FILTERING;"
positions_prepared_query = cassandra_session.prepare(positions_query)
positions_results = cassandra_session.execute(positions_prepared_query)
positions_df = pd.DataFrame(positions_results)

# positions_df.set_index('start_position', inplace=True)

# # Plotting the data
# ax = positions_df.plot(kind='bar', figsize=(10, 6))

# # Customize the plot
# ax.set_ylabel('Average Value')
# ax.set_title('Average Performance by Position')
# plt.legend(title='Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.show()

# Set the start_position column as the index for better plotting
positions_df.set_index('start_position', inplace=True)

# Plotting the data
ax = positions_df.plot(kind='bar', figsize=(10, 6))

# Adding vertical labels
for p in ax.patches:
    ax.annotate(
        f'{p.get_height():.2f}', 
        (p.get_x() + p.get_width() / 2., p.get_height() / 2), 
        ha='center', va='center',
        xytext=(0, 10), 
        textcoords='offset points',
        rotation=90, 
        color='black',
        fontsize=8
    )

# Customize the plot
ax.set_ylabel('Average Value')
ax.set_title('Average Performance by Position')
plt.legend(title='Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


cassandra_cluster.shutdown()
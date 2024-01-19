from cassandra.cluster import Cluster

cassandra_keyspace_name = 'University'

# Connect to the Cassandra cluster
host_ip = 'localhost'
cassandra_nodes_ip = [host_ip]
cluster = Cluster(cassandra_nodes_ip, port=9042)
session = cluster.connect()

# Create keyspace query
create_keyspace_query = f"CREATE KEYSPACE IF NOT EXISTS {cassandra_keyspace_name} WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': 1}}"

# Execute the query to create the keyspace
session.execute(create_keyspace_query)

# Switch to the new keyspace
session.set_keyspace(keyspace_name)

# # Define your insert query
# insert_query = "INSERT INTO your_table_name (column1, column2, column3) VALUES (%s, %s, %s)"

# # Prepare and execute the insert statement
# prepared_query = session.prepare(insert_query)

# # Data to insert
# data_to_insert = ('value1', 'value2', 'value3')

# # Execute the prepared query with the data
# session.execute(prepared_query, data_to_insert)

# Close the connection
cluster.shutdown()
